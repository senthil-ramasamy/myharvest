
from flask import Flask, redirect, url_for, request, render_template
from flask_mail import Mail, Message

app = Flask(__name__)
mail=Mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT']= 465
app.config['MAIL_USERNAME']='myharvestindia@gmail.com'
app.config['MAIL_PASSWORD']='myharvest'
app.config['MAIL_USE_TLS']=False
app.config['MAIL_USE_SSL']= True
mail=Mail(app)

@app.route("/mail/<name>/<phone>/<username>")
def success(name,phone,username):
	msg = Message('Hello', sender = 'myharvestindia@gmail.com', recipients = ['archustalin@gmail.com'])
	msg.body = "NAME:{},PHONE:{},EMAIL:{}".format(name,phone,username)
	mail.send(msg)
	return render_template("thank.html",name=name)

@app.route('/task1',methods=['POST'])
def login():
	if request.method =='POST':
		name,phone,username = request.form['name'],request.form['phone'],request.form['username']
		return redirect(url_for('success',name=name,phone=phone,username=username))


if __name__== '__main__':
	app.run(debug=True)
