from app import db

ROLE_USER = 0
ROLE_ADMIN = 1

class Product(db.Model):
    id = db.Column(db.String(64), index = True, primary_key = True)
    ndc = db.Column(db.String(12), index = True, unique = True)
    typename = db.Column(db.String(64))
    proprietary_name = db.Column(db.String(128))
    proprietary_name_suffix = db.Column(db.String(64))
    non_proprietary_name = db.Column(db.String(128))
    dos_age_for_name = db.Column(db.String(64))
    route_name = db.Column(db.String(64))
    start_marketing_date = db.Column(db.String(64))
    end_marketing_date = db.Column(db.String(64))
    marketing_category_name = db.Column(db.String(64))
    application_number = db.Column(db.String(64))
    label_name = db.Column(db.String(64))
    substance_name = db.Column(db.String(64))
    active_numerator_strength = db.Column(db.String(64))
    active_ingred_unit = db.Column(db.String(64))
    pharm_classes = db.Column(db.String(64))
    deaschedule = db.Column(db.String(64))
    
    #packages = db.relationship('Package', backref = 'author', lazy = 'dynamic')


class Package(db.Model):
    code = db.Column(db.String(12),  primary_key = True)
    description = db.Column(db.String(255))
    