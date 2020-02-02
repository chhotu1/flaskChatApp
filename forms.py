from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField,validators
from wtforms.validators import InputRequired, Required,ValidationError

class RegisterForm(FlaskForm):
    # image=FileField('image',validators=[FileRequired(), FileAllowed(images, 'Images only!')])
    username = StringField('Username',[validators.Length(min=4, max=10)])
    password = PasswordField('Password',[validators.Length(min=6,max=10)])
    email = StringField("Email",[validators.Required("Please enter your email address."),validators.Email("Please enter your email address.")])
class LoginForm(FlaskForm):
    username = StringField('Username',[validators.Length(min=4, max=10)])
    password = PasswordField('Password',[validators.Length(min=6)])
