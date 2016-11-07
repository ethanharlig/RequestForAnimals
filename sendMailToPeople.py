from __future__ import print_function
import smtplib
import sched, time
import random
import datetime

def send_email(username):
    server.sendmail(username, "2094068179@vtext.com", msg) # random (geoff)
    server.sendmail(username, "8185994321@mms.att.net", msg) # shayan
    server.sendmail(username, "9253896304@mms.att.net", msg) # pledge
    print('Sent: %s\n' % msg)

with open('comein.txt') as f:
    pre = f.readlines()

animals = []
for p in pre:
    animals.append(p.rstrip('\n'))

with open('credentials.txt') as f:
    content = f.readlines()
username = content[0].rstrip('\n')
password = content[1].rstrip('\n')

while 1:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(username, password)

    my_int = int(random.random() * (len(animals) - 1));
    msg = "Need a cute pic of " + animals[my_int]

    minute_delay = 10 # number of minutes between each text (approx because server.sendmail takes a while)

    s = sched.scheduler(time.time, time.sleep(60 * minute_delay))

    print (datetime.datetime.now())
    s.enter(minute_delay, 1, send_email(username), None)

    server.quit()
