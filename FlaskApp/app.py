from flask import Flask, render_template
app = Flask(__name__)
from game import test 
@app.route("/")
def main():
    return test(15)
    #return render_template("index.html")

if __name__ == "__main__":
    app.run
