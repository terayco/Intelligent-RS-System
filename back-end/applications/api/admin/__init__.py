from flask import Flask

from applications.api.admin.analysis_api import analysis_api
from applications.api.admin.file import file_api
from applications.api.admin.history import history_api
from applications.api.admin.home import home_api
from applications.api.admin.report import report_api
from applications.api.admin.user import user_api


def admin_api(app: Flask):
    app.register_blueprint(user_api)
    app.register_blueprint(file_api)
    app.register_blueprint(history_api)
    app.register_blueprint(report_api)
    app.register_blueprint(analysis_api)
    app.register_blueprint(home_api)
    pass
