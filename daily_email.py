import smtplib, ssl
import pandas as pd
from string import Template

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from database import config

import daily_report

MY_ADDRESS = config.email_address
PASSWORD = config.app_password

from datetime import date

from lxml import html

import nlp_model

news_entries = nlp_model.result()


def get_contacts(filename):
    names = []
    emails = []
    contact_list = open(filename, mode="r", encoding="utf-8")
    for contact in contact_list:
        name, email = contact.split(",")[0], contact.split(",")[1]
        names.append(name)
        emails.append(email)
    return names, emails


def main():
    names, emails = get_contacts("./database/test_contact.txt")  # read contacts
    today = date.today().strftime("%b-%d-%Y")

    # set up the SMTP server
    s = smtplib.SMTP(host="smtp.gmail.com", port=587)
    s.starttls()
    s.login(MY_ADDRESS, PASSWORD)

    # For each contact, send the email:
    for name, email in zip(names, emails):
        msg = MIMEMultipart()  # create a message
        html_message = html_template()

        # setup the parameters of the message
        msg["From"] = "GunGoo's Daily Report"
        msg["To"] = email
        msg["Subject"] = today + ": Daily Stock News Report"

        msg.attach(MIMEText(html_message, "html"))
        # send the message via the server set up earlier.
        s.send_message(msg)
        del msg

    # Terminate the SMTP session and close the connection
    s.quit()


def html_template():
    first_part_html = open(
        "./database/content/first_part.txt",
        "r",
        encoding="utf-8",
    ).read()
    second_part_html = open(
        "./database/content/second_part.txt",
        "r",
        encoding="utf-8",
    ).read()
    happy = "\U0001f4c8"
    sad = "\U0001f4c9"
    middle_part = ""
    for news in news_entries:
        tk, news_title, neg_or_pos = news[0], news[1], news[2]
        up_or_down = happy if neg_or_pos == "Positive" else sad
        emoji = """<td id= "emoji_td">""" + up_or_down + "</td>"
        ticker = """<td id="ticker_id">""" + tk + "</td>"
        ns_content = """<td id="ellipsis"> <p>""" + news_title + "</p> </td>"
        new = "<tr>" + emoji + ticker + ns_content + "</tr>"
        middle_part += new

    html_message = first_part_html + middle_part + second_part_html

    return html_message


if __name__ == "__main__":
    main()
