import smtplib
import os

def sendReminder(message):
    '''
    Sends a text to the subjects phone number
    :param message: The text content to send
    :return:
    '''
    # SMTP_SSL Example
    server_ssl = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server_ssl.ehlo()  # optional, called by login()
    server_ssl.login(os.environ['EMAIL_USERNAME'], os.environ['EMAIL_PASSWORD'])
    # ssl server doesn't support or need tls, so don't call server_ssl.starttls()
    server_ssl.sendmail(os.environ['EMAIL_USERNAME'], os.environ['PHONE_NUMBER_EMAIL'], "Please reply with your homework!")
    # server_ssl.quit()
    server_ssl.close()


sendReminder("Please reply with your homework!: ")
