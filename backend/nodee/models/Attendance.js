let mongoose = require("mongoose");
let Schema = mongoose.Schema;
let AttendanceSchema = new Schema({
  classID: String,
  teacherID: String,
  dateandtime: Date,
  sessionName: String,
  sessionID: String,
  attendance: [{ studentID: String, deviceID: String }],
});

module.exports = mongoose.model("Attendance", AttendanceSchema);
