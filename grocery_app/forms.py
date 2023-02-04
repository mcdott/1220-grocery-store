from flask_wtf import FlaskForm
from wtforms import StringField, DateField, FloatField, SelectField, SubmitField, PasswordField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Length, ValidationError
from grocery_app.models import ItemCategory, GroceryStore, User
from grocery_app.extensions import bcrypt

class GroceryStoreForm(FlaskForm):
    """Form for adding/updating a GroceryStore."""

    title = StringField('Store Name',
        validators=[DataRequired(), Length(max=80)])
    address = StringField('Address',
        validators=[DataRequired(), Length(min=5, max=200)])
    submit = SubmitField('Submit')

class GroceryItemForm(FlaskForm):
    """Form for adding/updating a GroceryItem."""

    name = StringField('Item',
        validators=[DataRequired(), Length(min=3, max=80)])
    price = FloatField('Price')
    category = SelectField('Category', choices=ItemCategory.choices())
    photo_url = StringField('Photo')
    store = QuerySelectField('Store', query_factory=lambda: GroceryStore.query.all(), get_label='title')

    submit = SubmitField('Submit')

    from flask_wtf import FlaskForm

class SignUpForm(FlaskForm):
    """Form for signing up a User."""
    username = StringField('User Name',
        validators=[DataRequired(), Length(min=3, max=50)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

class LoginForm(FlaskForm):
    """Form for logging in a User."""
    username = StringField('User Name',
        validators=[DataRequired(), Length(min=3, max=50)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if not user:
            raise ValidationError('No user with that username. Please try again.')

    def validate_password(self, password):
        user = User.query.filter_by(username=self.username.data).first()
        if user and not bcrypt.check_password_hash(
                user.password, password.data):
            raise ValidationError('Password doesn\'t match. Please try again.')

