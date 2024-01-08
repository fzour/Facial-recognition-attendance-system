from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

@app.route('/')
def student():
	return render_template("loginetudiant.html")

@app.route('/conn', methods=['POST', 'GET'])
def conn():
     mydb = mysql.connector.connect(
          host= "localhost", 
          username= "root", 
          password="", 
          database="utilisateurs"
          )
     mycursor= mydb.cursor()
     if request.method == 'POST':
     	signup= request.form
     	username=request.form
     	username=signup['user']
     	password=signup['pass']
     	mycursor.execute("select * from students where username='"+username+"' and password='"+password+"'")
     	r=mycursor.fetchall()
     	count=mycursor.rowcount
     	if count==1:
     		return render_template("etudiant.html")
     	else:
     		return render_template("loginetudiant.html")
     mydb.commit()
     mycursor.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5001', debug=True)