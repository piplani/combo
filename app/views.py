
import os
from django.shortcuts import render
from .forms import adddata
# Create your views here.


def sendmail(receiver, dirname):
    import smtplib
    from email.MIMEMultipart import MIMEMultipart
    from email.MIMEText import MIMEText
    from email.MIMEBase import MIMEBase
    from email import encoders

    fromaddr = "akshaykumar.90447@gmail.com"
    toaddr = receiver

    msg = MIMEMultipart()

    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Images"

    body = "download attachment for results"

    msg.attach(MIMEText(body, 'plain'))

    filename = os.getcwd() + "/media/" + dirname + '/result.txt'
    attachment = open(filename, "rb")

    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % 'result.txt')

    msg.attach(part)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "piplani@786")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()


def index(request):
    form = adddata(request.POST or None, request.FILES)
    email = ""
    dirname = ""
    lowerlimit = ""
    upperlimit = ""
    emailsent = False
    if form.is_valid():
        new_data = form.save(commit=False)
        new_data.save()
        dirname = str(new_data.id)
        lowerlimit = str(new_data.lowerlimit)
        upperlimit = str(new_data.upperlimit)
        email = str(new_data.email)
        olddir = os.getcwd() + '/media/' + str(new_data.file.name)
        newdir = os.getcwd() + '/media/' + dirname + '/1.txt'
        os.mkdir(os.path.join(os.getcwd() + '/media', dirname))
        os.rename(olddir, newdir)
        os.system('python ' + os.getcwd() + '/app/combo_ex.py ' + dirname + " " + lowerlimit + " " + upperlimit)
        sendmail(email, dirname)
        emailsent = True
    return render(request, 'index.html', {'form': form, 'emailsent': emailsent, 'email': email})
