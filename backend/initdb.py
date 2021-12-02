from server import db
db.create_all()


from server import User
user1 = User(username="admin", email="admin@gmail.com", password="password")

db.session.add(user1)
db.session.commit()
User.query.all()