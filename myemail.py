import smtplib
import urllib

smtpUser='assassin.persia@gmail.com'
smtpPass='abhishektherocker'

toAdd='abhishek.doit@gmail.com'
fromAdd=smtpUser

subject='Gas Leakage'
header='To:' + toAdd + '\n' + 'From:' + fromAdd + '\n' + 'Subject:' + subject
body='Gas Leakage Detected and Knob has been turned off'

print header + '\n' + body

s=smtplib.SMTP('smtp.gmail.com',587)

s.starttls()

s.login(smtpUser,smtpPass)
s.sendmail(fromAdd, toAdd, header + '\n\n' + body)
s.quit()
execfile('/home/pi/push.py')
