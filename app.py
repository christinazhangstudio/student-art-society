from flask import Flask, render_template, url_for, request           # Library Imports
# Define application
app = Flask(__name__) 

# URL Routes
###################################
@app.route('/')
def homepage():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")    

@app.route('/events')
def events():
    return render_template("events.html")   

@app.route('/gallery')
def gallery():
    return render_template("gallery.html")

@app.route('/exhibitions')
def exhibitions():
    return render_template("exhibitions.html")    

@app.route('/member-spotlight')
def memberSpotlight():
    return render_template("member-spotlight.html") 

@app.route('/become-a-member')
def becomeMember():
    return render_template("become-a-member.html")                     

################################


if __name__ == "__main__":
    app.run(debug=True)