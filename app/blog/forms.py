from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import InputRequired


class BlogForm(FlaskForm):
    body = TextAreaField("What's on your mind?", validators=[InputRequired()])
    submit = SubmitField('Submit')