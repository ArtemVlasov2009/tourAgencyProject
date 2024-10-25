import flask, pandas, os
from .models import Tour
from main.settings import DATABASE
from datetime import datetime

def render_tour():
    path_xlsx = os.path.abspath(__file__ + "/../tours_table.xlsx")
    read_xlsx = pandas.read_excel(
        io=path_xlsx,
        header=None,
        names=["title", "date", "country", "price", "description"]
    )
    Tour.query.delete()
    print(read_xlsx)

    for _, row_data in read_xlsx.iterrows():
        try:
            tour_date = datetime.strptime(row_data['date'], "%Y-%m-%d").date()
        except (ValueError, TypeError):
            tour_date = datetime.today().date()

        tour = Tour(
            title=row_data['title'],
            date=tour_date,
            country=row_data['country'],
            price=row_data['price'],
            description=row_data['description']
        )
        DATABASE.session.add(tour)

    DATABASE.session.commit()
    return flask.render_template("tour.html", tours=Tour.query.all())

def render_tour_info(id):
    tour_id = Tour.query.get(id)
    return flask.render_template("tour_info.html", tour=tour_id)
