#!/usr/bin/env python
from time import strftime,sleep
import smtplib

FROM_ADDR = 'postmaster@oregonstate.edu'

f = open('smarthosts.txt')
SMART_HOSTS = f.readlines()
f.close()

f = open('recipients.txt')
TO_ADDRS = f.readlines()
f.close()
print TO_ADDRS
print SMART_HOSTS

for recipient in TO_ADDRS:
    for host in SMART_HOSTS:
        host = host.strip('\r\n')
        msg = "From: %s\r\nTo: %s\r\n" % (FROM_ADDR, recipient.strip('\r\n'))
        msg = msg + "Subject: Testing via {0}\r\nDate: {1}\r\n\r\nThis is a mail flow test message.".format(host,strftime('%a, %d %b %Y %X PDT'))
        server = smtplib.SMTP(host)
        server.set_debuglevel(1)
        server.sendmail(FROM_ADDR, recipient, msg)
        server.quit()
        sleep(5)

