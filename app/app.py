from flask import Flask, render_template, request, redirect
from flask_login import LoginManager,UserMixin
from flask_sqlalchemy import SQLAlchemy
import os
from werkzeug.security import generate_password_hash


app=Flask(__name__)

login_manager = LoginManager()
login_manager.init_app(app)#flaskとflask_loginを紐づけ

db = SQLAlchemy(app)
app.config['SECRET_KEY'] = os.urandom(24)#秘密鍵作成

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(25))


#必要な情報を送る
@app.route("/")
def upload():
    return render_template("excer_upload.html")


#excer_upload.htmlから来た情報をexcer_uoloaded_file.htmlへ送る
@app.route("/excer_upload",methods=["GET","POST"])
def excer_upload():
    if request.method=="POST":
        user_name = request.form.get("name")
        user_pass=request.form.get("password")
        image = request.files["image"]

        # 受け取った情報でUserのインスタンスを作成
        user = User(username=user_name, password=generate_password_hash(user_pass, method='sha256'))
        db.session.add(user)#$データベースにuserの情報を登録
        db.session.commit()#保存

        return redirect("/login")

        #image.save(os.path.join('../app/static/uploaded_images', image.filename))
        #return render_template("excer_uploaded_file.html", user_name, user_sex,image.filename)#引数が4つあるからだめらしい


"""
#excer_upload.htmlから来た情報をとりあえず表示する
@app.route('/excer_uploaded_file/<string:imagename>')
def excer_uploaded_file(imagename):
    return render_template('excer_uploaded_file.html', imagename=imagename)


"""


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')
        # Userテーブルからusernameに一致するユーザを取得
        user = User.query.filter_by(username=username).first()
        if check_password_hash(user.password, password):
            login_user(user)
            return redirect('/')

    else:
        return render_template('login.html')



if __name__=="main":
    app.run(debug=True)