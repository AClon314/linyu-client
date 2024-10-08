import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr

# 创建邮件对象
message = MIMEText('邮件正文', 'plain', 'utf-8')

# 设置 From 头
from_name = "AClon"
from_email = "aclon@qq.com"
message['From'] = formataddr((str(Header(from_name, 'utf-8')), from_email))

# 设置其他邮件头
message['To'] = "aclon@qq.com"
message['Subject'] = "邮件主题"

# 发送邮件
smtp_server = 'smtp.qq.com'
smtp_port = 587
smtp_user = from_email
smtp_password = '授权码'

try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  # 启用TLS加密
    server.login(smtp_user, smtp_password)
    server.sendmail(from_email, [message['To']], message.as_string())
    print("邮件发送成功")
except Exception as e:
    print(f"邮件发送失败: {e}")
finally:
    server.quit()