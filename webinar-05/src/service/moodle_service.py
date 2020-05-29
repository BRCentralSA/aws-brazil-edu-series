import mysql.connector


def db_connector_factory():
    moodle_db = mysql.connector.connect(
        host="<DATABASE HOST ENDPOINT>",
        user="<DATABASE USER>",
        passwd="<DATABASE PASSWORD>",
        database="<DATABASE NAME>",
    )

    return moodle_db


def db_close_connector(connection):
    connection.close()


def get_students():
    moodle_db = db_connector_factory()
    cursor = moodle_db.cursor()
    cursor.execute("SELECT firstname, email FROM mdl_user;")
    students = cursor.fetchall()
    db_close_connector(moodle_db)

    return students
