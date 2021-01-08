import smtplib, ssl
import pandas as pd
from string import Template

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from database import config

import daily_report

import daily_report

MY_ADDRESS = config.email_address
PASSWORD = config.app_password

from datetime import date

from lxml import html

# for ticker, title in daily_report.daily_report().items():
#     print(ticker, title)
# print(MY_ADDRESS, PASSWORD)
def get_contacts(filename):
    """
    Return two lists names, emails containing names and email addresses
    read from a file specified by filename.
    """

    names = []
    emails = []
    contact_list = open(filename, mode="r", encoding="utf-8")
    for contact in contact_list:
        name, email = contact.split(",")[0], contact.split(",")[1]
        names.append(name)
        emails.append(email)
    return names, emails


def read_template(filename):
    """
    Returns a Template object comprising the contents of the
    file specified by filename.
    """
    content_file = open(filename, "r", encoding="utf-8")
    template_file_content = content_file.read()
    return Template(template_file_content)


def main():
    names, emails = get_contacts(
        "/Users/geongupark/opt/anaconda3/envs/GSA/DailyReport/database/test_contact.txt"
    )  # read contacts
    message_template = read_template(
        "/Users/geongupark/opt/anaconda3/envs/GSA/DailyReport/database/message.txt"
    )
    today = date.today().strftime("%b-%d-%Y")
    news_entries = daily_report.daily_report()

    # set up the SMTP server
    s = smtplib.SMTP(host="smtp.gmail.com", port=587)
    s.starttls()
    s.login(MY_ADDRESS, PASSWORD)

    # For each contact, send the email:
    for name, email in zip(names, emails):
        msg = MIMEMultipart()  # create a message

        # add in the actual person name to the message template
        # message = message_template.substitute(
        #     PERSON_NAME=name.title(), NEWS_TABLE=news_entries
        # )
        html_message = html_template()
        # Prints out the message body for our sake
        # print(message)

        # setup the parameters of the message
        msg["From"] = MY_ADDRESS
        msg["To"] = email
        msg["Subject"] = today + ": Daily Stock News Report by GunGoo"

        # add in the message body
        # msg.attach(MIMEText(message, "plain"))
        msg.attach(MIMEText(html_message, "html"))
        # send the message via the server set up earlier.
        s.send_message(msg)
        del msg

    # Terminate the SMTP session and close the connection
    s.quit()


def html_template():
    html_message = """\
<html>

<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">

<title>Tutsplus Email Newsletter</title>
<style type="text/css">
a {color: #d80a3e;}
body, #header h1, #header h2, p {margin: 0; padding: 0;}
#main {border: 1px solid #cfcece;}
img {display: block;}
#top-message p, #bottom p {color: #3f4042; font-size: 12px; font-family: Arial, Helvetica, sans-serif; }
#header h1 {color: #ffffff !important; font-family: "Lucida Grande", sans-serif; font-size: 24px; margin-bottom: 0!important; padding-bottom: 0; }
#header p {color: #ffffff !important; font-family: "Lucida Grande", "Lucida Sans", "Lucida Sans Unicode", sans-serif; font-size: 12px;  }
h5 {margin: 0 0 0.8em 0;}
h5 {font-size: 18px; color: #444444 !important; font-family: Arial, Helvetica, sans-serif; }
p {font-size: 12px; color: #444444 !important; font-family: "Lucida Grande", "Lucida Sans", "Lucida Sans Unicode", sans-serif; line-height: 1.5;}
</style>
</head>

<body>


<table width="100%" cellpadding="0" cellspacing="0" bgcolor="e4e4e4"><tr><td>
<table id="top-message" cellpadding="20" cellspacing="0" width="600" align="center">
<tr>
<td align="center">
<p><a href="#">View in Browser</a></p>
</td>
</tr>
</table>

<table id="main" width="600" align="center" cellpadding="0" cellspacing="15" bgcolor="ffffff">
<tr>
<td>
<table id="header" cellpadding="10" cellspacing="0" align="center" bgcolor="8fb3e9">
<tr>
<td width="570" align="center"  bgcolor="#d80a3e"><h1>Evanto Limited</h1></td>
</tr>
<tr>
<td width="570" align="right" bgcolor="#d80a3e"><p>November 2017</p></td>
</tr>
</table>
</td>
</tr>

<tr>
<td>
<table id="content-3" cellpadding="0" cellspacing="0" align="center">
<tr>
<td width="250" valign="top" bgcolor="d0d0d0" style="padding:5px;">
<img src="https://thumbsplus.tutsplus.com/uploads/users/30/posts/29520/preview_image/pre.png" width="250" height="150"  />
</td>
<td width="15"></td>
<td width="250" valign="top" bgcolor="d0d0d0" style="padding:5px;">
<img src="https://cms-assets.tutsplus.com/uploads/users/30/posts/29642/preview_image/vue-2.png" width ="250" height="150" />
</td>
</tr>
</table>
</td>
</tr>
<tr>
<td>
<table id="content-4" cellpadding="0" cellspacing="0" align="center">
<tr>
<td width="200" valign="top">
<h5>How to Get Up and Running With Vue</h5>
<p>In the introductory post for this series we spoke a little about how web designers can benefit by using Vue. In this tutorial we will learn how to get Vue up..</p>
</td>
<td width="15"></td>
<td width="200" valign="top">
<h5>Introducing Haiku: Design and Create Motion</h5>
<p>With motion on the rise amongst web developers so too are the tools that help to streamline its creation. Haiku is a stand-alone..</p>
</td>
</tr>
</table>
</td>
</tr>


</table>
<table id="bottom" cellpadding="20" cellspacing="0" width="600" align="center">
<tr>
<td align="center">
<p>Design better experiences for web & mobile</p>
<p><a href="#">Unsubscribe</a> | <a href="#">Tweet</a> | <a href="#">View in Browser</a></p>
</td>
</tr>
</table><!-- top message -->
</td></tr></table><!-- wrapper -->

</body>
</html>
	"""
    return html_message


if __name__ == "__main__":
    main()
