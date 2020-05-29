from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    Response,
    redirect,
    url_for,
    session,
)

from src.controller.moodle_controller import moodle_controller

# Flask Configurations


class FlaskConfs(object):

    # Atributos
    app = Flask(__name__)
    app.secret_key = "eipohgoo4rai0uf5ie1oshahmaeF"

    def __init__(self):
        self.register_blue_prints()

    def register_blue_prints(self):
        self.app.register_blueprint(moodle_controller)

    def run_app(self):
        self.app.run(debug=True, host="0.0.0.0")
