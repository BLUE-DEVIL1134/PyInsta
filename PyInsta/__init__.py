"""
# -*- coding: utf-8 -*-

__author__ = "Akash"
__email__ = "akashjio6666@gmail.com"
__version__ = 1.0.0"
__copyright__ = "Copyright (c) 2004-2020 Leonard Richardson"
# Use of this source code is governed by the MIT license.
__license__ = "MIT"

Description:
            Py-Insta Is A Python Library
            Created By Akash Pattnaik From
            India..
            Py-Insta Helps Users To Easily
            Scrape Instagram Data
            And Print It Or You Can Define It Into A Variable...
            If You Find Bugs Then Please Report To
            @AKASH_AM1 On Telegram...

Pre-Requests:
            from bs4 import BeautifulSoup
            import requests

Documentation:
            Github: https://github.com/BLUE-DEVIL1134/Py-Insta
            PyPi: https://pypi.org/user/AkashPattnaik/
"""
__version__ = 1.0
import requests
from bs4 import BeautifulSoup

__url__ = "https://www.instagram.com/{}/"

def Insta(username):
    try:
        response = requests.get(__url__.format(username.replace('@','')),timeout=5)  # InCase Someone Types @UserName
        if '404' in str(response):  # If The Username Is Invalid
            data = 'No Such Username'
            return data
        else:
            soup = BeautifulSoup(response.text, "html.parser")
            meta = soup.find("meta", property="og:description")
            try:
                s = meta.attrs['content'].split(' ')
                data = {
                    'Followers': s[0],
                    'Following': s[2],
                    'Posts': s[4],
                    'Name': s[13]
                }
                return data
            except requests.exceptions.InvalidURL:
                return 'No Such Username'
    except (requests.ConnectionError, requests.Timeout):
        return 'No InterNet Connection'
