from app import db
from datetime import datetime

class Agreement(db.model):
    id = db.Column(db.Integer, primary_key=True)
    parent_consent_id = db.Column(db.Integer)
    entity_key = db.Column(db.String(128))
    entity_key_type = db.Column(db.String(128))
    signed_date = db.Column(db.DateTime,default=datetime.utcnow)
