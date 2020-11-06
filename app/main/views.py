
from . import main
from flask import render_template
from .forms import ContactForm
from .. import db
from ..models import Post

@main.route('/')
def index():
    posts = Post.query.order_by(Post.timestamp.desc()).all()
    return render_template('index.html', active = 'home', posts=posts)

@main.route('/contact')
def contact():
    form = ContactForm()
    return render_template('contact.html', form=form, active =  'contact')

@main.route('/about')
def about():
    return render_template('about.html', active = 'about')