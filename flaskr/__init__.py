import os

from flask import Flask
from . import config


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_object(config.DevelopmentConfig)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    # directions endpoint
    import googlemaps
    from datetime import datetime
    gmaps = googlemaps.Client(key=app.config['GOOGLE_API_KEY'])

    from . import directions
    app.register_blueprint(directions.bp)
    app.add_url_rule('/', endpoint='index')

    from flask import render_template

    @app.route('/directions')
    def directions():
        now = datetime.now()
        res = gmaps.directions("Gdynia",
                         "Gdansk",
                         mode="transit",
                         departure_time=now)
        startingPoint=res[0]['legs'][0]['start_location']
        endPoint=res[0]['legs'][0]['end_location']
        totalDist=res[0]['legs'][0]['distance']['text']
        totalTime=res[0]['legs'][0]['duration']['text']
        return render_template('directions/directions.html', startingPoint=startingPoint, endPoint=endPoint, totalDist=totalDist, totalTime=totalTime)

    return app
