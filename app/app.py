from webbrowser import get
from flask import Flask, render_template, request, url_for, redirect
import os


app=Flask(__name__)

#必要な情報を送る
@app.route("/upload")
def upload():
    return render_template("excer_upload.html")


#excer_upload.htmlから来た情報をexcer_uoloaded_file.htmlへ送る
@app.route("/excer_upload",methods=["GET","POST"])
def excer_upload():
    if request.method=="POST":
        user_name = request.form.get("name")
        file = request.files["image"]
        file.save(os.path.join('../app/static/uploaded_images', file.filename))
        return redirect(url_for('excer_uploaded_file', filename=file.filename))

#excer_upload.htmlから来た情報をとりあえず表示する
@app.route('/excer_uploaded_file/<string:filename>')
def excer_uploaded_file(filename):
    return render_template('excer_uploaded_file.html', filename=filename)



if __name__=="main":
    app.run(debug=True)