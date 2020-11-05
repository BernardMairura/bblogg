
from . import main
from flask import render_template
from .forms import ContactForm
from .. import db
from ..models import Blog

@main.route('/')
def index():
    blogs = Blog.query.order_by(Blog.timestamp.desc()).all()
    return render_template('index.html', active = 'home', blogs=blogs)

@main.route('/contact')
def contact():
    form = ContactForm()
    return render_template('contact.html', form=form, active =  'contact')

@main.route('/about')
def about():
    return render_template('about.html', active = 'about')