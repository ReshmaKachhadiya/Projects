from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/aboutus.html")
def aboutus():
    return render_template('aboutus.html')


# @app.route("/menu.html")
# def aboutus():
#     return render_template('menu.html')
if __name__=="__main__":
    app.run(debug=True)    