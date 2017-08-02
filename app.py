from chalice import Chalice
from datetime import datetime
import smtplib
from chalice import CORSConfig

cors_config = CORSConfig(
    allow_origin='https://foo.example.com',
    allow_headers=['X-Special-Header'],
    max_age=600,
    expose_headers=['X-Special-Header'],
    allow_credentials=True
)

# APP_EMAIL = 'exceptionapplication@gmail.com'
# DEFUALT_RESPONSE='Exception sent'

app = Chalice(app_name='teamsite-chalice')


@app.route('/')
def index():
    return {'hello': 'world'}

@app.route('/test/{form}', methods=['POST'], cors=cors_config)
def test(form):
    return {'name: ':form.name}


@app.route('/sendex', methods=['POST'])
def sendexception(agent='Bob', supervisor="Tyler"):
    gmail_user = 'exappv2@gmail.com'
    gmail_password = '!Qaz#Edc'
    sent_from = gmail_user
    to = 'pastrana.steven.az@gmail.com'
    subject = 'Fixing'
    body = "Hey, what's up?"

    agent = agent
    supervisor = supervisor

    form = """
    Exception form
    ===============

    Agent: %s
    Supervisor: %s
    """ % (agent, supervisor)

    message = """From: %s
    To: %s
    MIME-Version: 1.0
    Content-type: text/html
    Subject: %s

    %s

    """ % (sent_from, to, subject, form)

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        # UNcoment this to send the mail
        # server.sendmail(sent_from, to, message)
        server.close()
        # return {'success': 'Yay!!'}
        return{'agent': agent}
    except:
        return {'error': 'happened'}

# @app.route('/exform', methods=['POST'])
# def send_mail(sender, sender_email, manager, approved_by, exception_date, start_time, end_time, reason="LEFT EMPTY", recipient="steven.antonio.dev@gmail.com", when=datetime.now()):
#     yag = yagmail.SMTP('exceptionapplication', '!Qaz#Edc')
#     title = '<h2>Exception Submission</h2>'
#     time_sent = '<p><b>Time Sent: </b>{}</p>'.format(when)
#     sender = '<p><b>Agent: </b>{}</p>'.format(sender)
#     sender_email = '<p><b>Agent Email: </b>{}</p>'.format(sender_email)
#     manager = '<p><b>Manager: </b>{}</p>'.format(manager)
#     exception_date = '<p><b>Date: <b>{}</p>'.format(exception_date)
#     start_time = '<p><b>Start Time: </b>{}</p>'.format(start_time)
#     end_time = '<p><b>End Time: </b>{}</p>'.format(end_time)
#     reason = '<p><b>Reason: </b>{}</p>'.format(reason)
#     email_footer = '<br><p>=====================================</p></br><p>This email was automagically created and sent to {} using python 3, yag, and some coding judo.'.format(recipient)
#     contents = [title, time_sent, sender, sender_email, manager, exception_date, start_time, end_time, reason, email_footer]
#     # Send the email to the manager | Change the email in the functiion to the variable recipient
#     yag.send('pastrana.steven.az@gmail.com', 'Exception Submission', contents)
#     # Send the confirmation email
#     yag.send(sender, 'Exception Confirmation', 'Your exception was successfuly submited.')


# The view function above will return {"hello": "world"}
# whenever you make an HTTP GET request to '/'.
#
# Here are a few more examples:
#
@app.route('/hello/{name}', cors=cors_config)
def hello_name(name):
   # '/hello/james' -> {"hello": "james"}
   return {'hello': name}
#
@app.route('/users', methods=['POST'], cors=cors_config)
def create_user():
    # This is the JSON body the user sent in their POST request.
    user_as_json = app.json_body
    # Suppose we had some 'db' object that we used to
    # read/write from our database.
    # user_id = db.create_user(user_as_json)
    return {'user_id': '2'}
#
# See the README documentation for more examples.
#
