from django.contrib.admin.widgets import AdminFileWidget
from django.utils.html import format_html
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from parkcoastsite.settings import EMAIL_HOST_USER
import threading

class EmailThread(threading.Thread):
    def __init__(self,emails):
        self.emails = emails
        threading.Thread.__init__(self)

    def run(self) -> None:
        self.emails.send()

def sendEmailContact(obj,content,request):
        # email for user 
        subject = "User Inquiry - Park Coast Capital Site"
        to=obj.email
        text_content = ''
        print([EMAIL_HOST_USER],subject)
        html_content = render_to_string('email_template.html',{'obj':obj})
        msg = EmailMultiAlternatives(subject, text_content, 'parkcoastholdings@gmail.com', [obj.email])
        msg.attach_alternative(html_content, "text/html")
        EmailThread(msg).start()

        # email for administrator
        subject = "User Inquiry - Park Coast Capital Site"
        to = obj.email
        text_content = ''
        html_content = render_to_string('admin_email_template.html',{'obj':obj})
        msg = EmailMultiAlternatives(subject, text_content, 'parkcoastholdings@gmail.com', [EMAIL_HOST_USER])
        msg.attach_alternative(html_content, "text/html")
        EmailThread(msg).start()

def sendEmail(email,content,request):
        subject = "Subscription - Park Coast Capital Site"
        to=email
        text_content = ''
        print([EMAIL_HOST_USER],subject)
        html_content = render_to_string('email.html',{'obj':email})
        msg = EmailMultiAlternatives(subject, text_content, 'parkcoastholdings@gmail.com', [email])
        msg.attach_alternative(html_content, "text/html")
        EmailThread(msg).start()

        # email for administrator
        subject = "User subscribe - Park Coast Capital Site"
        to = email
        text_content = ''
        html_content = render_to_string('admin_email.html',{'obj':email})
        msg = EmailMultiAlternatives(subject, text_content, 'parkcoastholdings@gmail.com', [EMAIL_HOST_USER])
        msg.attach_alternative(html_content, "text/html")
        EmailThread(msg).start()
        

class AdminImageWidget(AdminFileWidget):
    """Admin widget for showing clickable thumbnail of Image file fields"""

    def render(self, name, value, attrs=None, renderer=None):
        html = super().render(name, value, attrs, renderer)
        if value and getattr(value, 'url', None):
            html = format_html('<a href="{0}" target="_blank"><img src="{0}" alt="{1}" width="150" height="150" style="object-fit:cover;margin-bottom:30px; border:0.5px solid black;"/></a>', value.url, str(value)) + html
            # html = format_html('<a href="{0}" target="_blank"><img src="{0}" alt="{1}" width="150" height="150" style="object-fit:cover;margin-bottom:30px;"/></a> <br/><button id="img-delete" class="btn btn-sm btn-outline-danger mb-2"><i class="fas  fa-trash-alt"></i> </button>', value.url, str(value)) + html
        return html 
