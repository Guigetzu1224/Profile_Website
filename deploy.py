from flask import Flask, escape, request, render_template, flash, url_for, redirect
from forms import ContactForm
from flask_mail import Message, Mail
from globals import initialize # Private variables
app = Flask(__name__)
mail = Mail(app)
initialize(app)
mail = Mail(app)
# Irrelevant, this key is public on github


@app.route('/')
@app.route('/home')
def home():
    return render_template('main.html')

@app.route('/aboutMe')
def aboutMe():
  return render_template('aboutMe.html')

@app.route('/contactMe', methods=['GET', 'POST'])
def contactMe():  

  form = ContactForm(request.form)
  if request.method == 'POST':
    if form.validate() == False:
      print(form.validate())
      return render_template('contactMe.html', form=form)
    else:
      msg = Message(form.subject.data,recipients=['sstein17@fordham.edu'])
      msg.body = ("""
      From: {}; Name {};
      {}
      """.format(str(form.name.data), str(form.email.data), str(form.message.data)))
      mail.send(msg)
      return render_template('contactMe.html', success=True)
 
  elif request.method == 'GET':
    return render_template('contactMe.html', form=form)



if __name__ == '__main__':
	app.run(debug=True)

