from flask import Flask, render_template, request
from icecream import ic
import json

app = Flask(__name__)
file_path = 'data.json'
users=[]

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/test")
def test():
    return render_template("test.html")

@app.route("/login",methods=["GET","POST"])
def login():
    if request.method == "POST":
        req_user_name=request.form["user"]
        req_pwd= request.form["pwd"]
        
        if len(users) == 0:
            with open(file_path, 'r') as json_file:
                users = json.load(json_file)

        for user in users:
            if user["userName"] == req_user_name and user["pwd"] == req_pwd:
                ic("yesssssssssssssssssssssssssssssssssssssssssssssssss")
                ic(user["userName"])
                return render_template("about.html")
            
    return render_template("login.html")


@app.route("/signup",methods=["GET","POST"])
def signup():
    if request.method == "POST":
        req_user_name=request.form["user"]
        req_pwd= request.form["pwd"]
        ic(req_user_name)
        # read old users
        if len(users) == 0:
            with open(file_path, 'r') as json_file:
                users = json.load(json_file)

        # add new users
        users.append({"userName":req_user_name,"pwd":req_pwd})
        with open(file_path, 'w') as json_file:
            json.dump(users, json_file)
        ic(users)
        return render_template("home.html") 
    return render_template("signup.html")