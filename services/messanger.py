import yagmail
import argparse
from datetime import datetime
from twilio.rest import Client

# APP_EMAIL = 'exceptionapplication@gmail.com'
account_sid='AC2827b6e38732f90a376e2c53f846fcdb'
auth_token='5c8b10c2431f61a7389b92ee70dfd26a'
DEFUALT_SMS="You've just recieved an exception request"
DEFUALT_RESPONSE='Exception sent'

def sendmail(sender, manager, agent, start_time, end_time, description="LEFT EMPTY", recipient = 'pastrana.steven.az@gmail.com', when = datetime.now()):
    yag = yagmail.SMTP('exceptionapplication', '!Qaz#Edc')
    title = '<h2>Exception Submission</h2>'
    time_sent = '<p><b>Time Sent: </b>{}</p>'.format(when)
    manager = '<p><b>Manager: </b>{}</p>'.format(manager)
    agent = '<p><b>Agent: </b>{}</p>'.format(agent)
    agent_email = '<p><b>Agent Email: </b>{}</p>'.format(sender)
    start_time = '<p><b>Start Time: </b>{}</p>'.format(start_time)
    end_time = '<p><b>End Time: </b>{}</p>'.format(end_time)
    description = '<p><b>Description: </b>{}</p>'.format(description)
    email_footer = '<br><p>=====================================</p></br><p>This email was automagically created and sent to {} using python 3, yag, and some coding judo.'.format(recipient)
    contents = [title, time_sent, manager, agent, start_time, end_time, description, email_footer]
    # Send the email to the manager | Change the email in the functiion to the variable recipient
    yag.send('pastrana.steven.az@gmail.com', 'Exception Submission', contents)
    # Send the confirmation email
    yag.send(sender, 'Exception Confirmation', 'Your exception was successfuly submited.')

def sendtext(text_message):
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        to='+14805277459',
        from_="+14804705774",
        body=text_message
    )
    print(message.sid)


def main():
    # Using Argparse to test dynamic content
    parser = argparse.ArgumentParser()
    parser.add_argument('sender', help='The sender of the message | ex: sender@email.com', type=str, default='agent@email.com')
    # parser.add_argument('recipient', help='The recipient of the message | ex: recipient@email.com', type=str, default='pastrana.steven.az@gmail.com')
    parser.add_argument('manager', help='The manager | ex: Jane Manager', type=str, default='Jane Manager')
    parser.add_argument('agent', help='The agent | ex: Tom Agent', type=str, default='Tom Agent')
    parser.add_argument('start_time', help='The start time of the exception | ex: 12:30', type=str, default=None)
    parser.add_argument('end_time', help='The enbd time of the exception | ex: 13:00', type=str, default=None)
    parser.add_argument('description', help='The text describing the exception', type=str, default='NOT FILLED IN')
    args = parser.parse_args()

    sendmail(args.sender, args.manager, args.agent, args.start_time, args.end_time, args.description)
    sendtext(DEFUALT_SMS)
#
# if __name__ == '__main__':
#     main()
