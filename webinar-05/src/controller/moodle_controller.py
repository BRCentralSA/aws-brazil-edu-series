from flask import jsonify, Blueprint
import src.service.moodle_service as moodle_service
import src.service.notify_service as notify_service

moodle_controller = Blueprint("moodle_controller", __name__)


@moodle_controller.route("/health/", methods=["GET"])
def health():
    return jsonify({"Health": "Ok"})


@moodle_controller.route("/get_students/", methods=["GET"])
def get_students():
    os_info = moodle_service.get_students()

    return jsonify(os_info)


@moodle_controller.route("/notify_students/", methods=["POST"])
def notify_students():
    notifications = notify_service.send_email()

    return jsonify(notifications)
