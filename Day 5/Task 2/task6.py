class Notification:
    def send(self):
        print("Sending notification")


class EmailNotification(Notification):
    def send(self):
        print("Sending email")


class SMSNotification(Notification):
    def send(self):
        print("Sending SMS")


notifications = [
    EmailNotification(),
    SMSNotification(),
    EmailNotification(),
    SMSNotification()
]

for notification in notifications:
    notification.send()