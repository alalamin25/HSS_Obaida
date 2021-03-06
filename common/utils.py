import logging
from django.conf import settings
from django.core.mail import EmailMessage
from celery_app.celery import app

logger = logging.getLogger(__name__)

ADMIN_EMAILS = settings.ADMIN_EMAILS
PRIMARY_ADMIN_EMAIL = settings.PRIMARY_ADMIN_EMAIL


@app.task
def send_mail(subject, body, to_email=ADMIN_EMAILS,
              from_email=PRIMARY_ADMIN_EMAIL, bcc=None, attachment=None):
    email_success = False
    email = EmailMessage(subject, body, from_email, to_email, bcc)

    # This content_subtype is added to properly render html in email_body
    # email.content_subtype = "html"

    if attachment is not None:
        email.attach(attachment.name, attachment.read(), attachment.content_type)
    try:
        email.send()
    except Exception as e:
        msg = 'mail failed to {0}'.format(to_email)
        logger.exception(msg)
    else:
        email_success = True
        logger.info('mail sent to {0}'.format(to_email))

    return email_success
