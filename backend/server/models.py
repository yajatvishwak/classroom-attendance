from server import db, ma

class Student(db.Model):
    sID = db.Column(db.Integer, primary_key = True)
    usn = db.Column(db.String(20), unique = True, nullable=False)
    name = db.Column(db.String(50), unique = True, nullable=False)
    # deviceID = db.Column(db.String(100), unique = True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    classCode = db.Column(db.String(60), nullable=False)
    subjectCodes = db.Column(db.String(60), nullable=False)
    #attendance = db.relationship("Attendance",backref="student")
class StudentSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Student

    sID = ma.auto_field()
    usn = ma.auto_field()
    name = ma.auto_field()
    password = ma.auto_field()
    classCode = ma.auto_field()
    subjectCodes = ma.auto_field()


class Teacher(db.Model):
    tID = db.Column(db.Integer, primary_key = True)
    usn = db.Column(db.String(20), unique = True, nullable=False)
    name = db.Column(db.String(50), unique = True, nullable=False)
    # deviceID = db.Column(db.String(100), unique = True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

class Attendance(db.Model):
    aID = db.Column(db.Integer, primary_key= True)
    sID = db.Column(db.String(10))
    sessionID = db.Column(db.String(20))
class AttendanceSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Attendance
    aID = ma.auto_field()
    sID =  ma.auto_field()
    sessionID = ma.auto_field()

class Session(db.Model):
    tid = db.Column(db.Integer )
    sessionID = db.Column(db.Integer, primary_key= True)
    classCode = db.Column(db.String(10))
    subjectCode = db.Column(db.String(20), nullable= False)
    timeInterval = db.Column(db.String(100))
    date = db.Column(db.String(100))

class SessionSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Session

    tid = ma.auto_field()
    sessionID = ma.auto_field()
    classCode = ma.auto_field()
    subjectCode = ma.auto_field()
    timeInterval = ma.auto_field()
    date = ma.auto_field()
