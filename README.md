#  Welcome To PyInsta
### A Python Library For Scraping InstaGram Data.

## Installation
### Installation With PyPi
```shell script
pip install PyInsta
        OR
pip3 install PyInsta
```
### Installation With Git
```shell script
git clone https://github.com/BLUE-DEVIL1134/PyInsta
cd PyInsta
python3 setup.py install
```

## Documentation
You People Must Have Used A Lot Of Python Libraries But Would Never
Have Seen A Proper Documentation In Maximum Of Them.

**That Is Not With Us (>oo>)**
### Regular Usage
Ok. Now Lets Start By Creating A File Named `main.py:`
The Content Of The File Would Be:
```python
# -*- coding: utf-8 -*-
import PyInsta

result = PyInsta.Insta('username')  # Any Username, You Can Also Use a Vriable
print(result)

```

Now Let's Run This File In The `Terminal:`
```commandline
python main.py
      OR
python3 main.py
```

The Result Will Be:
```shell script
We Have Set The Result Into A Python Dictionary,
So By Printing Just The Result We Get: 
{
    'Followers': number_of_followers,
    'Following': number_of_following,
    'Posts': number_of_posts,
    'Name': name
}
```

**Now We Can Access Each Data Seperately Like** `This:`

```python
# -*- coding: utf-8 -*-
import PyInsta

result = PyInsta.Insta('username')  # Any Username, You Can Also Use a Vriable

# This Is Case Sensitive
Followers = result["Followers"]
Following = result["Following"]
Posts = result["Posts"]
Name = result["Name"]

# Now You Can Print These Values Or Use To Make Bots
# Like Telegram Bots And Discord Bots
```

### Usage In Loops
As This Is Python, We Can Use This In Various Ways.
So Let's Create A File Named `loops.py:`
```python
import PyInsta

# Lets Define A List
usernames = ['username1','username2','username3','username4']
# Now We Use The All Known Best Loop:
for username in usernames:
    result = PyInsta.Insta(username)
    print(result)
```

### Mega Usage
Now Based On All The Avobe Information,
We Will Create A Script To Check Multiple 
Accounts.. (UserName Detector)...Create A File `detector.py:`
```python
import PyInsta
usernames = input('Enter Usernames Separated With Space : ').split(' ')

for username in usernames:
    result = PyInsta.Insta(username)
    if "No Such Username" in result:
        pass
    elif "No InterNet Connection" in result:
        print('No InterNet Connection')
        break
    else:
        print(f"""
**-------------------**
Found Live UserName : {username}
**-------------------**
""")
```

Run The File In The `Terminal:`
```commandline
python detector.py
```

The Result Will Be :
```commandline
Enter Usernames Separated With Space : carryminati binod bhubanbam username

**-------------------**
Found Live UserName : carryminati
**-------------------**


**-------------------**
Found Live UserName : binod
**-------------------**


**-------------------**
Found Live UserName : username
**-------------------**


Process finished with exit code 0

```

# License
**Like All Others We Also Have The MIT License**

```shell script
MIT License

Copyright (c) 2020 PyInsta

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```
# FAQ
Q. What Is PyInsta?

Ans.
```py
PyInsta Is A Python Library Made By Akash Pattnaik
Which Scrapes InstaGram Data With Just The UserName.
```
Q. Version?

Ans. 
```py
__version__ = 1.0.0
```

Q. What Data It Scrapes?

Ans.
```py
PyInsta For Now Scrapes Only The Name, Followers, Following,
Posts...

In The Future Versions PyInsta Will Scrape The Posts And The Status..
```

Q. What Are The Pre-Requests?

Ans.
```py
PyInsta Uses Nothing But requests And bs4
Which Will Be Installed Along With PyInsta !
```

Q. On Which OS Does This Works?

Ans.
```py
This Is OS-Independent
This Means That This Will Work On Any OS
```

Q. Is This Compatible With Pyinstaller or such Libraries?

Ans.
```py
In That Case
We Are Extermly To Say That
Yes! Reqests And bs4 Are Available In Cython
```
