from . import db


class PropertyInfo(db.Model):
    __tablename__ = "tproperties"

    id = db.Column(db.Integer, primary_key = True, unique = True)
    title = db.Column(db.String(225))
    number_of_bedrooms = db.Column(db.String(100))
    number_of_bathrooms = db.Column(db.String(100))
    location = db.Column(db.String(100))
    price = db.Column(db.String(100))
    typeHA = db.Column(db.String(100))
    description = db.Column(db.String(400))
    photo = db.Column(db.String(300))

    def __init__(self, title, nObedrooms, nObathrooms, location, price, typee, description, photo):
        self.title = title
        self.nObedrooms = number_of_bedrooms
        self.nobathrooms = number_of_bathrooms
        self.location = location
        self.price = price
        self.typee = typee
        self.description = description
        self.photo = photo
    
    def get_id(self):
        try:
            return unicode(self.id)
        except NameError:
            return str(self.id)