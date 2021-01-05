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
        "/Users/geongupark/opt/anaconda3/envs/GSA/DailyReport/database/contacts.txt"
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
        message = message_template.substitute(
            PERSON_NAME=name.title(), NEWS_TABLE=news_entries
        )

        # Prints out the message body for our sake
        print(message)

        # setup the parameters of the message
        msg["From"] = MY_ADDRESS
        msg["To"] = email
        msg["Subject"] = today + ": Daily Stock News Report by GunGoo"

        # add in the message body
        msg.attach(MIMEText(message, "plain"))

        # send the message via the server set up earlier.
        s.send_message(msg)
        del msg

    # Terminate the SMTP session and close the connection
    s.quit()


if __name__ == "__main__":
    main()
