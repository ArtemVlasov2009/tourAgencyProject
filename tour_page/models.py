from main.settings import DATABASE


class Tour(DATABASE.Model):
  id = DATABASE.Column(DATABASE.Integer, primary_key = True)
  title = DATABASE.Column(DATABASE.String(40), nullable = False)
  date = DATABASE.Column(DATABASE.String(20), nullable = False)
  country = DATABASE.Column(DATABASE.String(30), nullable = False)
  price = DATABASE.Column(DATABASE.Integer, nullable = False)
  description = DATABASE.Column(DATABASE.Text, nullable = False)

  def __repr__(self):
    return f"Tour id - {self.id}; Tour title - {self.title}; Tour country - {self.country}"
  
