from smtplib import SMTP as Client

client = Client("127.0.0.1", 14001)

r = client.sendmail('abc@taoz.xyz', ['taogl3@163.com'], """\
From: Anne Person <anne@example.com>
To: Bart Person <bart@example.com>
Subject: A test
Message-ID: <ant>

https://visa.vfsglobal.com/chn/en/deu/activateemail?q=E09l1wtg/DhUgfhH9QxTF/OC6WoFw7+pJsVhJGi3h6aE2tZAmUbSBV3c99N+RY4ec6M8Abq4E0b+7+HZQWIZcDyVZwAGRtENucDAMwBs2u8gz8iVFMdq2NgBjbqY2AYdBXewZYwi9npgEjmunkqUb9Ksyyl10RAxpS2s64MaPYw=
""")
