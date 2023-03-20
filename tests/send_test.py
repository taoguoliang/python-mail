from smtplib import SMTP as Client

client = Client("127.0.0.1", 14001)

r = client.sendmail('abc@taoz.xyz', ['taogl3@163.com'], """\
From: Anne Person <anne@example.com>
To: Bart Person <bart@example.com>
Subject: A test
Message-ID: <ant>

Hi Bart, this is Anne.
""")
