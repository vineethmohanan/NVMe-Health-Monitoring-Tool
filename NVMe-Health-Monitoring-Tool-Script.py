import psutil
import smtplib
from email.mime.text import MIMEText

def send_alert(subject, body):
    sender = 'your_email@example.com'
    receiver = 'alert_receiver@example.com'
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = receiver

    with smtplib.SMTP('smtp.example.com') as server:
        server.login(sender, 'your_email_password')
        server.sendmail(sender, receiver, msg.as_string())

def check_nvme_health():
    for disk in psutil.disk_partitions():
        if 'nvme' in disk.device:
            usage = psutil.disk_usage(disk.mountpoint)
            if usage.percent > 80:
                send_alert('NVMe Health Alert', f'{disk.device} usage is at {usage.percent}%')

if __name__ == '__main__':
    check_nvme_health()