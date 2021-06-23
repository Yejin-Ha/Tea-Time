from flask import Flask, request, render_template, jsonify, redirect
from flask_jwt_extended import *
from selftest_dto import User
from dao import Camera
from signup_dto import USERDTO

app = Flask(__name__)

# app.config.update(
#     DEBUG=True,
#     JWT_SECRET_KEY="I'M IML"
# )

# jwt = JWTManager(app)

# 첫 화면은 카메라 추천 받는 화면으로 하자
@app.route('/', methods=['get'])
def index():
    print('login Page')
    return render_template('index.html')

# 자가진단 화면으로 이동
@app.route('/selftest', methods=['get'])
def linktoselftest():
    print('link to self test Page')
    return render_template('selftest.html')

# 유저인지 확인하는 역할
@app.route('/login', methods=['POST'])
def login_proc():
    user_info = User(request.form.get("id"), request.form.get("pw"), request.form.get("test_level"))
    camera = Camera()
    camera.update_level(user_info)
    return jsonify(result=200)

# 회원가입 화면으로 이동
@app.route('/signup', methods=['get'])
def linktosignup():
    print('sing up Page')
    return render_template('signup.html')

# 회원가입 기능
@app.route("/signup", methods=["POST"])
def insertuser():
    dao = Camera()
    dto = USERDTO(request.form.get("u_id"), request.form.get("u_pw"), request.form.get("nick"))
    dao.userinsert(dto)
    return jsonify(result=200)

# 아이디 중복 확인
@app.route('/checkid', methods = ["POST"])
def selectid():
    dao = Camera()
    check = dao.id_check(request.form.get("u_id"))
    if check is None:
        return jsonify(True)
    else:
        return jsonify(False)

# 닉네임 중복 확인
@app.route('/checknick', methods = ["POST"])
def selectnick():
    dao = Camera()
    check = dao.nick_check(request.form.get("nick"))
    if check is None:
        return jsonify(True)
    else:
        return jsonify(False)





@app.route('/user_login', methods=['get'])
def linktologin():
    print('login Page')
    return render_template('camera.html')


if __name__ == "__main__":
    app.run(debug=True, port="5000", host="127.0.0.1")
