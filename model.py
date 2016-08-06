"""Models and database functions for Safebot project"""

from flask_sqlalchemy import SQLAlchemy

# This is the connection to the PostgreSQL database through
# the Flask-SQLAlchemy helper library. On this, we can find the `session`
# object, where we do most of our interactions (like committing, etc.)

db = SQLAlchemy()

##############################################################################
# Model definitions

# class User(db.Model):
#     """Safebot User details"""

#     __tablename__ = "users"

#     user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
#     first_name = db.Column(db.String(20), nullable=True)
#     last_name = db.Column(db.String(30), nullable=True)
#     contact_num = db.Column(db.Integer, nullable=True)
#     nvmd_code = db.Column(db.String(3), nullable=True)

#     def __repr__(self):
#         """Provide helpful representation when printed."""

#         return "<User user_id=%s first_name=%s last_name=%s contact_num=%s>" % (self.user_id, self.first_name, self.last_name, self.contact_num)


class FoodPrices(db.Model):
    """Prices of Food"""

    __tablename__ = "foodprices"

    food_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    country = db.Column(db.String(60), nullable=True)
    city = db.Column(db.String(60), nullable=True)
    market = db.Column(db.String(60), nullable=True)
    commodity = db.Column(db.String(60), nullable=True)
    currency = db.Column(db.String(60), nullable=True)
    priceform = db.Column(db.String(60), nullable=True)
    quantityunit = db.Column(db.String(60), nullable=True)
    month = db.Column(db.Integer, nullable=True)
    year = db.Column(db.Integer, nullable=True)
    price = db.Column(db.Integer, nullable=True)
    commoditysource = db.Column(db.String(120), nullable=True)

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<FoodPrices food_id=%s country=%s city=%s market=%s commodity=%s>" % (
            self.food_id, self.country, self.city, self.market, self.commodity)

# class Unsafe(db.Model):
#     """Unsafe calls"""

#     __tablename__ = "unsafes"

#     unsafe_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
#     datetime = db.Column(db.DateTime)
#     geo_location = db.Column(db.Integer, autoincrement=True, primary_key=True)
#     sms_sent = db.Column(db.String(100))
#     user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))

#     user = db.relationship('User')

#     def __repr__(self):
#         """Provide helpful representation when printed."""

#         return "<Unsafe unsafe_id=%s datetime=%s geo_location=%s sms_sent=%s user_id=%s>" % (self.location_id, self.datetime, self.geo_location, self.sms_sent, self.user_id)



##############################################################################
# Helper functions

def connect_to_db(app):
    """Connect the database to the Flask app"""

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres:///proactivesupply'
    db.app = app
    db.init_app(app)


if __name__ == '__main__':

    from server import app
    connect_to_db(app)
    print "Connected to DB."

    db.configure_mappers()
    db.create_all()