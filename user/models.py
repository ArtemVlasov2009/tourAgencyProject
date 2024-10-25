from main.settings import DATABASE
from flask_login import UserMixin

class Users(DATABASE.Model, UserMixin):
  id = DATABASE.Column(DATABASE.Integer, primary_key = True)
  username = DATABASE.Column(DATABASE.String(30), nullable = False)
  password = DATABASE.Column(DATABASE.String(20), nullable = False)

  def __repr__(self) :
    return f"User id - {self.id}; Username - {self.username}"

