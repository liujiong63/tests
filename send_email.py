from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr(( \
        Header(name, 'utf-8').encode(), \
        addr.encode('utf-8') if isinstance(addr, unicode) else addr))

from_addr = raw_input('From: ')
password = raw_input('Password: ')
to_addr = raw_input('To: ')
smtp_server = raw_input('SMTP server: ')

msg = MIMEText('Hello, send by liujiong...', 'plain', 'utf-8')
msg['From'] = _format_addr(u'Sender nick name <%s>' % from_addr)
msg['To'] = _format_addr(u'Receiver nick name <%s>' % to_addr)
msg['Subject'] = Header(u'This is the subject', 'utf-8').encode()

server = smtplib.SMTP(smtp_server, 25)
# receive debug logs
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
