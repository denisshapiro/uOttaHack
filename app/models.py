from app import db

class User(db.Model):
    id    = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), nullable=False)
    car = db.relationship("Car", uselist=False, back_populates="user")
    
    def jsonify(self):
        return {"username":self.username, "id": self.id, "car_id": self.car.id}

    def __repr__(self):
        return f"User('{self.id}, {self.car}')"

class Car(db.Model):
    id   = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(200), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    colour = db.Column(db.String(20), nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship("User", back_populates='car')

    def __repr__(self):
        return f"Car('{self.year} {self.colour} {self.model} | {self.user_id}')"