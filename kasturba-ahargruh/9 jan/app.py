from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/about.html")
def aboutus():
    return render_template('about.html')

@app.route("/contact.html")
def contactus():
    return render_template('contact.html')
@app.route("/menu.html")
def menu():
    return render_template('menu.html')
if __name__=="__main__":
    app.run(debug=True,port=5000)    