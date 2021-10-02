# Student Art Society at UTSA Official Website
- - - -
## About
The Student Art Society is a COLFA student organization at the University of Texas at San Antonio. This git repository contains the source code for the website; this is a Python web app, using the Flask framework, deployed on Heroku (for free). The url 

- - - -
## Prerequisities
- Code IDE (e.g. Visual Studio Code)
- Python (Python 3.x recommended)
- A free Heroku account (currently, this app is deployed using Christina's account)
- Git
- Heroku CLI

- - - -
## Maintenance Notes

Everytime files are edited, do the following commands to update this git repo:
```
git add .
```
```
git commit -m "Add your custom commit message here"
```
```
git push
```

The heroku branch needs to be updated as well so that the heroku files are built:
```
git push heroku master
```
You can check the dyno hours/usage and make sure `web` is up with:
```
heroku ps
```

Lastly, open in browser!
```
heroku open
```

The Heroku account associated with the SAS website is Christina Zhang's (Founder/President 2020-2022). If future maintainers would like to shift ownership and create a new Heroku account (recommended), please download this source code or do a `git clone`, create a new Heroku account and login into it through `heroku login`, `cd` to the root directory for this app, create a heroku app through `heroku create`, and lastly do `git push heroku master` and `heroku open`.

Here are some helpful resources:
- https://devcenter.heroku.com/articles/getting-started-with-python?singlepage=true
- https://python-adv-web-apps.readthedocs.io/en/latest/flask_deploy.html

- - - -
## Contact
christinazhang2013@gmail.com
