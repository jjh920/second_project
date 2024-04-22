import smtplib
from email.message import EmailMessage
import os
GMAIL_PASS = os.getenv("GMAIL_PASS")

class MailService:
    @staticmethod
    def mail_accepted(visitor_name, visitor_email, time):
        smtp = smtplib.SMTP("smtp.gmail.com", 587)
        smtp.ehlo()
        smtp.starttls()

        smtp.login("seoseungjae20209@gmail.com", GMAIL_PASS)
        email = EmailMessage()
        email["Subject"] = f"{visitor_name}님의 방문자 예약 서비스가 승인되었습니다"
        email["From"] = "seoseungjae20209@gmail.com"
        email["To"] = f"{visitor_email}"
        email.set_content(f'''{visitor_name}님이 {time}에 신청하신 방문자 예약 서비스가 승인되었습니다.''')
        smtp.send_message(email)
        smtp.quit()

    @staticmethod
    def mail_regected(visitor_name, visitor_email, time, reason):
        smtp = smtplib.SMTP("smtp.gmail.com", 587)
        smtp.ehlo()
        smtp.starttls()

        smtp.login("seoseungjae20209@gmail.com", GMAIL_PASS)
        email = EmailMessage()
        email["Subject"] = f"{visitor_name}님의 방문자 예약이 거절되었습니다"
        email["From"] = "seoseungjae20209@gmail.com"
        email["To"] = f"{visitor_email}"
        email.set_content(f'''{visitor_name}님이 {time}에 신청하신 방문자 예약이 거절되었습니다.
사유 : {reason}
문의 : 02-1234-5678
''')
        smtp.send_message(email)
        smtp.quit()