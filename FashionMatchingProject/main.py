import data

from flask import Flask,redirect, url_for, render_template,request
import code


app = Flask(__name__)

@app.route("/",methods=["POST","GET"])
def master():
    if request.method == "POST":

        starty = request.form["clothing"]
        clothy = request.form["color"]
        wow = code.clothes(clothy,int(starty))

        return render_template("results.html",s=starty,s2=clothy,s3 = wow )
    else:
        return render_template("index.html")



@app.route("/results")
def results():
    return "<h1> this is were you will eventually see the razzle dazzle</h1>"

@app.route("/redirect1")
def redirect1():
    return redirect(url_for("master"))


if __name__ == "__main__":
    app.run()

