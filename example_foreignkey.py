class Drive (db.model):
  __tablename__ = 'drivers'
  id = db.Column(db.Integer, primary_key=true)
  ...
  vehicles = db.relationship)'Vehicle',backref='drivers,lazy=true)


class Vehicle (db.model):
  __tablename__ = 'vehicles'
  id = db.Column(db.Integer, primary_key=true)
  make = db.Column(db.String(), nullable=False_
  ...
  driver_id = db.Column(db.Integer, db.ForeignKey('drivers.id'),nullable=False)