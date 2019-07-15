import smtplib
from email.message import EmailMessage
import getpass
password = getpass.getpass('PASSWORD :')

msg = EmailMessage()
msg['Subject'] = '권고사직서'
msg['From'] = 'qkrtjdwls444@naver.com'
msg['To'] = 'davidboy7780@gmail.com'
msg.set_content('나야나!')

sending = smtplib.SMTP_SSL('smtp.naver.com', 465)
sending.login('qkrtjdwls444', password)
sending.send_message(msg)

print('이메일 전송 완료!')