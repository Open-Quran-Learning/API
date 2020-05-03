from ayat import mail
from flask_mail import Message
from ayat import app


# -----------------------------------------------------------
# demonstrates how to send email to recipients
#
# Parameters:
#
# subject:         stands for the subject of the email.
# recipients:      stands for email addresses which you want to send to.
#                  it must be a list.
# content:         text content only is available at this parameter.
# html_content:    stands for html content.
# resource:        must be the name of the resource followed by its extension.
#                  example: 'image.pdf' or 'document.pdf'
# resource_type:   just put your attachment extension here.
#
# hint:
# all parameters must be passed to the function even if you don't need one of them
# (you can leave it as an empty string), subject and recipients is a must and you can't leave it blank.


def send_message(subject, recipients, content, html_content, resource, resource_type):
    msg = Message(subject,
                  sender='ayatquraancenter@gmail.com',
                  recipients=recipients)
    try:

        if content:
            msg.body = content
        if msg.html:
            msg.html = html_content
        if resource:
            with app.open_resource("res/" + resource) as fp:
                msg.attach(resource, "application/" + resource_type, fp.read())

        mail.send(msg)
        return True
    except:
        return False
# -----------------------------------------------------------
