from main.settings import DATABASE

class Data(DATABASE.Model):
    id = DATABASE.Column(DATABASE.Integer, primary_key = True)
    name = DATABASE.Column(DATABASE.String(30), nullable = False)
    email = DATABASE.Column(DATABASE.String(40), nullable = False)
    review = DATABASE.Column(DATABASE.String, nullable = False)

    def __repr__(self):
      return f"id користувача - {self.id}; Email користувача {self.email}; Review користувача {self.review};"