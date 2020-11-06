from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, PasswordField
from wtforms.validators import InputRequired, Length, Email, EqualTo


class BlogForm(FlaskForm):
	title = StringField('Title', validators=[InputRequired()])
	body = TextAreaField("Type your desired quote?",validators=[InputRequired()])
	submit = SubmitField('Submit')

class ContactForm(FlaskForm):
	name = StringField("Name",  [InputRequired("Please enter your name.")])
	email = StringField("Email",  [InputRequired("Please enter your email address."), Email("This field requires a valid email address")])
	subject = StringField("Subject",  [InputRequired("Please enter a subject.")])
	message = TextAreaField("Message",  [InputRequired("Not including a message would be stupid")])
	submit = SubmitField("Send")