import smtplib
from email.mime.text import MIMEText
from config import Config


class EmailSender:
    def __init__(self):
        self.sender = Config.EMAIL_SENDER
        self.password = Config.EMAIL_PASSWORD
        self.receiver = Config.EMAIL_RECEIVER

    def send_alert(self, coin_name, old_price, new_price, percent_change):
        direction = "increased 🚀" if new_price > old_price else "decreased 📉"
        subject = f"ALARM: {coin_name} {direction} by {abs(percent_change):.2f}%!"

        body = f"""
        Alert for {coin_name}!
        Old Price: ${old_price:.2f}
        New Price: ${new_price:.2f}
        Change: {direction} by {abs(percent_change):.2f}%
        """
        msg = MIMEText(body)
        msg["Subject"] = subject
        msg["From"] = self.sender
        msg["To"] = self.receiver

        try:
            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
                server.login(self.sender, self.password)
                server.send_message(msg)
                print(f"Alert email about {coin_name} sent successfully.")
        except Exception as e:
            print(f"Failed to send alert email: {e}")
