from flask import Blueprint, flash, g, redirect, render_template, request, url_for
from werkzeug.exceptions import abort
from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint("blog", __name__)


@bp.route("/")
def index():
    db = get_db()
    posts = db.execute(
        "select post.id, title, body, created, author_id, username"
        " from post join user on post.author_id = user.id"
        " order by created desc"
    ).fetchall()
    return render_template("blog/index.html", posts=posts)

