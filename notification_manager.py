import smtplib

my_email = "REPLACE"
password = "REPLACE"

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def send_email(self, message):
        with smtplib.SMTP("smtp.gmail.com") as self.connection:
            self.connection.starttls()
            self.connection.login(user=my_email, password=password)
            encoded_message = message.encode('utf-8')
            self.connection.sendmail(from_addr=my_email, to_addrs="REPLACE", msg=f"subject:Message of the Day\n\n{encoded_message}")
            # Prints if successfully sent.
        print(message)
