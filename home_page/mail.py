import flask_mail

from main.settings import project



project.config['MAIL_SERVER'] = 'smtp.gmail.com'
project.config['MAIL_PORT'] = 587
project.config['MAIL_USE_TLS'] = True
project.config['MAIL_USE_SSL'] = False
project.config['MAIL_USERNAME'] = "av3411261@gmail.com"
project.config['MAIL_PASSWORD'] = 'cexr vjan tuhd cjle'
project.config['MAIL_DEFAULT_SENDER'] = "av3411261@gmail.com"

mail = flask_mail.Mail(app = project)