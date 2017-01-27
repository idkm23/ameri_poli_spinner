#!/usr/bin/python
# Import requests (to download the page)
import binascii
import requests
import smtplib
import time

last_checksum = None
first_time = True
while True:
    url = "https://american-politics-gp.wiki.uml.edu/9AM-Camelot+Roles"
    # set the headers like we are a browser,
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    response = requests.get(url, headers=headers).text
    if "Karame" in response:
        print "unedited."
    else:
        if first_time:
            first_time = False
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login("throway19xiii04jSa0f@gmail.com", "f0aSj40iiix91yaworht")
            msg = "The site has been updated you fuck."
            server.sendmail("throway19xiii04jSa0f@gmail.com", "idkm23@gmail.com", msg)
            server.quit()
        print "AHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH"
    time.sleep(6)
