from . import blog
from flask import render_template, url_for, redirect
from .. import db
from ..models import Post
from .forms import PostForm
import markdown2
from flask_login import current_user, login_user, logout_user, login_required



@blog.route('/blog', methods = ['GET', 'POST'])
@login_required
def index():
    post = PostForm()
    if current_user is not None:
        if post.validate_on_submit():
            post =  Post(body=post.body.data, author = current_user._get_current_object())
            db.session.add(post)
            db.session.commit()
            return redirect(url_for('main.index')) 
    return render_template('blog/blog.html', active = 'blog', post=post)