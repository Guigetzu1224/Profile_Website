from flask import Flask, escape, request, render_template, flash, url_for, redirect
from forms import RegistrationForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '9a047fca6ed2a0524aa92912ca476006'

@app.route('/')
@app.route('/home')
def home():
    return render_template('main.html')

@app.route('/aboutMe')
def aboutMe():
  return render_template('aboutMe.html')


@app.route('/contactMe', methods=['GET', 'POST'])
def contactMe():
	form = RegistrationForm()
	if form.validate_on_submit():
		flash(f"You're email was sent! I'll get back to you within 24 hours" ) #Success is the bootstrap class
		return redirect( url_for('home') )
	return render_template('contactMe.html', form=form)


@app.route("/register", methods=['GET', 'POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		flash(f'Account Created for {form.username.data}!', 'success' ) #Success is the bootstrap class
		return redirect( url_for('home') )
	''' 
		flash(f'Incorrect information! Try again!')
		return redirect (url_for('register'))
		'''
	return render_template('register.html',title='Register',form=form)


if __name__ == '__main__':
	app.run(debug=True)