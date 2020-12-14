import smtplib
from datetime import datetime
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
fromaddr = "FROM SENDER"
toaddr = "TO RECIPIENT"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Motion Detected"
body = 'A motion has been detected.\nTime: %s' % str(datetime.now())
msg.attach(MIMEText(body, 'plain'))
server = smtplib.SMTP('smtp.aol.com', 587)
server.starttls()
server.login(fromaddr, "PASSWORD")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()