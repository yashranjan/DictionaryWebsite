<h1 align="center">Dictionary Website</h1>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

---

<p align="center"> A simple dictionary website to fetch the various context, meanings, synonyms and antonyms of any entered word.
    <br> 
</p>

## 📝 Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Built Using](#built_using)

## 🧐 About <a name = "about"></a>

A simple dictionary website to fetch a lot of information of any entered word built using Django and uses SQLite3 as the database. The user is provided the option to search the word of one's choice, after which the various context of the word, along with the synonyms and antonyms are displayed.

## 🏁 Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Make sure that you've python version >=3.6, virtualenv and pip3 installed. If not, then follow the instructions from the official documentation for your OS.


### Installing

To get the setup up and running, follow the below steps

1 Clone the repo

```
 git clone https://github.com/yashranjan/DictionaryWebsite.git && cd DictionaryWebsite
```

2  Create a virtual env for running the website that'll be local to this project only

```
virtualenv venv -p python3.x
source venv/bin/activate
```

3 Install the requirements mentioned in the requirements.txt
```
pip -r requirements.txt
```
4 Start the server which and then open localhost:8000 in the browser
```
python manage.py runserver
```

## ⛏️ Built Using <a name = "built_using"></a>

- [Django](https://www.djangoproject.com/) - Server Framework
- [SQLite3](https://www.sqlite.org/index.html/) - Database

