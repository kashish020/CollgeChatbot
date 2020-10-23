from chatbot import chatbot
from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)
app.static_folder = 'static'

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(chatbot.get_response(userText))

@app.route("/login")
def login():
    return render_template("login.html")

@app.route('/result',methods=['POST','GET'])
def result():
    mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="chatbot"
    )
    mycursor=mydb.cursor()
    if request.method=='POST':
        signup=request.form
        username = signup['username']
        password = signup['password']
        mycursor.excute("select * from reg where Username='"+username+"' and Password='"+password+"'")
        r=mycursor.fetchall()
        count=mycursor.rowcount
        if count==1:
            return render_template("index.html")
        else:
            return render_template("login.html")
        
    mydb.commit()
    mycursor.close()

if __name__ == "__main__":
    app.run() 