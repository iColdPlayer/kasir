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

# export your SECRET_KEY
export SECRET_KEY='your_secret_key'

# Migrate 
./manage.py migrate

# you can also create an admin for yourself (default username is admin, pass: admin)
./manage.py createsuperuser

# Run it
./manage.py runserver
```
And go to your `localhost:8000`, you should see the login page there. <br>
You can also register as user at `localhost:8000/register`.

### Import & Export Data From Admin Page
You can also export and import your stock from the admin page itself.
Go to `/admin/data/stock`, you should be able to see the example data over there.

### Production
Please do not forget to `collectstatic` before you plan to use on production by running: <br>
`./manage.py collectstatic` or your site won't be able to load the staticfiles.

To make sure your staticfiles works correctly, you can running locally on your local machine with debug set to `False`
by typing this: <br>
`./manage.py runserver --insecure`


If you plan to use on production, please do not forget to uncomment this line below in your `settings` 
when `DEBUG = 0`.

Check this option by running: <br>
`./manage.py check --deploy`


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


Thank's for visiting and don't forget to give a star, create an issue or pull request.

---

#### [MIT License](https://github.com/iColdPlayer/Cashier/blob/master/LICENSE)

