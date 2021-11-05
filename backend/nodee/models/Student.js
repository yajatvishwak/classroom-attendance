let mongoose = require("mongoose");
let Schema = mongoose.Schema;
let StudentSchema = new Schema({
  studentID: String,
  usn: { type: String, unique: true, required: true },
  password: String,
  classID: String,
  lastLogin: { time: Date, deviceID: String },
});

module.exports = mongoose.model("Student", StudentSchema);
