from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, ValidationError,EqualTo
from app.models import Agreement

class AgreementForm(FlaskForm):
    entity_key = StringField('Entity Key',validators=[DataRequired()])
    entity_key_type = StringField('Entity Key Type',validators=[DataRequired()])
    submit = SubmitField('Create Agreement')

