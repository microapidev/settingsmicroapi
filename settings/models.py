from datetime import datetime
from settings.config import db, ma


class Config(db.Model):
    __tablename__ = 'configurations'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    api_name = db.Column(db.String(), nullable=False)
    current_config = db.Column(db.String(), nullable=False)
    previous_config = db.Column(db.String(), nullable=True)
    default_config = db.Column(db.String(), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __str__(self):
        return "Config <{id}: {api_name}>".format(id=self.id, api_name=self.api_name)

    __repr__ = __str__


class ConfigSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Config
