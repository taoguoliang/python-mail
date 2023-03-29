import email
import re
import urllib.request
from email.header import decode_header

from data import dataInstance
from curl_cffi import requests
import urllib

def decode_str(s):
    value, charset = decode_header(s)[0]
    if charset:
        value = value.decode(charset)
    return value


def guess_charset(msg):
    charset = msg.get_charset()
    if charset is None:
        content_type = msg.get('Content-Type', '').lower()
        pos = content_type.find('charset=')
        if pos >= 0:
            charset = content_type[pos + 8:].strip()
    return charset


def print_part(msg):
    rs = ""
    content_type = msg.get_content_type()
    if content_type == 'text/plain' or content_type == 'text/html':
        content = msg.get_payload(decode=True)
        charset = guess_charset(msg)
        if charset:
            content = content.decode(charset)
        rs = rs + str(content)
    else:
        rs = rs + str(content_type)
    return rs


def print_info(msg):
    rs = ""
    if (msg.is_multipart()):
        parts = msg.get_payload()
        for n, part in enumerate(parts):
            if part.is_multipart():
                rs = rs + print_info(part)
            else:
                rs = rs + print_part(part)
    else:
        return print_part(msg)
    return rs


class CrazySrvHandler:
    dao = dataInstance

    async def handle_RCPT(self, server, session, envelope, address, rcpt_options):
        envelope.rcpt_tos.append(address)
        return '250 OK'

    async def handle_DATA(self, server, session, envelope):
        mail_from = envelope.mail_from
        rcpt_tos = envelope.rcpt_tos
        message = email.message_from_bytes(envelope.content)
        content = print_info(message)
        subject = decode_str(message['Subject'])

        obj = {
            "from": mail_from,
            "to": rcpt_tos,
            "subject": subject,
            "content": content
        }
        data = content.replace(" ", "")
        reg = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
        urls = re.findall(reg, data, re.I)
        for url in urls:
            # urllib.request.urlopen(url=url)
            requests.get(url=url, impersonate="chrome101")

        self.dao.store_msg(obj)

        print("success record msg:" + mail_from + "->" + str(rcpt_tos) + "|" + str(subject))

        return '250 Message accepted for delivery'
