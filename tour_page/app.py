import flask

tour = flask.Blueprint(
  name = "tour",
  import_name ="tour_page",
  template_folder = "templates",
  static_folder = "static"

)