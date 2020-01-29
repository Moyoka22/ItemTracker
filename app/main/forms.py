from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DateField, SubmitField
from wtforms.validators import DataRequired, Length

minimum_description_length = 40

class AddItemForm(FlaskForm):
    item = StringField('name',validators=[DataRequired()])
    owner = StringField('owner',validators=[DataRequired()])
    description = TextAreaField('description',validators=[Length(min=minimum_description_length,message=f'Descriptions must be a minimum of {minimum_description_length} chars')])
    submit = SubmitField()