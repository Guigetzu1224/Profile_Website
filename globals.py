def initialize(app):
	app.config["MAIL_SERVER"] = "smtp.gmail.com"
	app.config["MAIL_PORT"] = 465
	app.config["MAIL_USE_SSL"] = True
	app.config["MAIL_USERNAME"] = 'samuelstein1224.webapp@gmail.com'
	app.config["MAIL_PASSWORD"] = 'webapp_password'
	app.config['MAIL_DEFAULT_SENDER'] = 'samuelstein1224.webapp@gmail.com'
	app.secret_key = 'DEVELOPMENT_KEY_11'