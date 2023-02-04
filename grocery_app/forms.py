from flask_wtf import FlaskForm
from wtforms import StringField, DateField, FloatField, SelectField, SubmitField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Length, URL
from grocery_app.models import ItemCategory, GroceryStore

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
