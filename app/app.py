from flask import Flask,render_template,request


app=Flask(__name__)

#「/test」へのアクセス時"test.html"出す
@app.route("/test")
def hello():

    return render_template("test.html")

#「excer」へのアクセス時にexcer.html出す

@app.route("/excer")
def excer():
    return render_template("excer.html") 


if __name__=="main":
    app.run(debug=True)