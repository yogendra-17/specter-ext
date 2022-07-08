

from flask import render_template
from ..service import WardenService




login_endpoint = WardenService.blueprints["login"]


# its full path will be: http://127.0.0.1:25441/svc/warden/login/
# the '/login' comes from the key
@login_endpoint.route("/", methods=["GET", "POST"])
def login():
    return "loginpage"
