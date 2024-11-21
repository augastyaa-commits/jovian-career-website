from flask import Flask

# Creating an app( An app is an object of the class, Flask)
app= Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, Kiranc</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)