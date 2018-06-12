from app import db


class Stuff(db.Model):
    __tablename__ = "stuff_seva"  # зміни на назву своєї таблиці
    stuff_id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.String(20))
    price = db.Column('name', db.Integer)
    producer = db.Column('price', db.String(20))
    material = db.Column('material', db.String(20))
    weight = db.Column('weight', db.Integer)
    stuff_type = db.Column('stuff_type', db.String(20))

    def __str__(self):
        return str("stuff id: " + str(self.stuff_id) + "\nname: " + str(
            self.name) + "\nname: " + str(self.price) + "\nprice: " + str(
            self.producer) + "\nmaterial" + str(self.material) + "\nweight: " + str(
            self.weight) + "\nstuff type: " + str(self.stuff_type))
