from . import blog
from flask import render_template

@blog.app_errorhandler(401)
def four_ow_one(error):
    return render_template('401.html')