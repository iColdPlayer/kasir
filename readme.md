# Cashier System Management & Inventory Management Using Django.


| Build Status      |
| ----------- | 
[![CircleCI](https://circleci.com/gh/iColdPlayer/Cashier/tree/master.svg?style=svg&circle-token=4f154d06f362677227578c720f589ec04968e23b)](https://circleci.com/gh/iColdPlayer/Cashier/tree/master)




You can also see the live demo [here](https://kasir.herokuapp.com). with user: `admin` & password: `demoadmin` (**The demo can take a time to load**)


Read more the flowchart and the pattern models [here](/cashierModel.md)


### Installation:
```bash
# Clone it
git clone https://github.com/iColdPlayer/kasir.git

cd kasir

# create your own Virtual Environment on you local machine
python -m venv env

# then activate it
source env/bin/activate

# Install all the dependencies
pip install -r requirements.txt

# Migrate 
./manage.py migrate

# Run it
./manage.py runserver

```

If you're running in development mode `DEBUG=True`, Please do not forget to comment this line below:

```
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = True
SECURE_HSTS_PRELOAD = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'
CSRF_COOKIE_SECURE = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
CONN_MAX_AGE = 60
```

The languange currently support for Indonesian only, other language coming soon.

List To Do:

* [ ] Adding Test.
* [ ] Adding Language Support.
* [ ] Print Nota To PDF


---

#### [MIT License](https://github.com/iColdPlayer/Cashier/blob/master/LICENSE)

