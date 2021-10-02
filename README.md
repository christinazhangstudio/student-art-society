Everytime files are edited, do the following commands to update this git repo:
```
git add.
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
