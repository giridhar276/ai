class EmailNotification:
    def send(self):
        print("Sending email")

class SMSNotification:
    def send(self):
        print("Sending SMS")

for notification in [EmailNotification(), SMSNotification()]:
    notification.send()
