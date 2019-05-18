import os
from django.conf import settings
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from django.shortcuts import render

def index(request):
    if 'to_email' in request.POST:
        if 'from_email' in request.POST:
            from_email = request.POST.get('from_email')
            to_email = request.POST.get('to_email')
            if 'msg' in request.POST:
                msg = request.POST.get('msg')
                sub = request.POST.get('sub')
                print("added")
                message = Mail(
                    from_email=from_email,
                    to_emails=to_email,
                    subject=sub,
                    html_content=msg)
                try:
                    sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
                    response = sg.send(message)
                    print(response.status_code)
                    print(response.body)
                    print(response.headers)
                except Exception as e:
                    print(e)

    return render(request, 'app/index.html', {})
