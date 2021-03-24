
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField
from wtforms.validators import DataRequired
from flask_wtf.file import FileAllowed, FileField, FileRequired

class PropertyForm(FlaskForm):
    Title = StringField("Title Property", validators = [DataRequired()])
    bedrooms = StringField("Number of Bedroom", validators = [DataRequired()])
    bathrooms = StringField("Number of Bathrooms", validators = [DataRequired()])
    Location = StringField("Location of Property", validators = [DataRequired()])
    Price = StringField("Price of Property", validators = [DataRequired()])
    Typee = SelectField("House or Apartment", choices = [("House", "House"), ("Apartment","Apartment")])
    Description = TextAreaField("Description of Property", validators = [DataRequired()])
    Photo = FileField("Photo of Property", validators = [FileRequired(), FileAllowed(["jpg","png","jpeg"], "Images Only!")])
                                                        