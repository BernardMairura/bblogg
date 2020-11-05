from flask import Blueprint

auth = Blueprint('blog',__name__)

from . import views,forms