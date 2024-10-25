import flask

user_page = flask.Blueprint(
    name = "user_page",
    import_name ="user",
    template_folder = "templates"

)