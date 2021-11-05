let mongoose = require("mongoose");
let Schema = mongoose.Schema;
let TeachersSchema = new Schema({
  name: String,
  teacherID: String,
  classHandled: [String],
  password: String,
  teacherUSN: { type: String, required: true, unique: true },
});

module.exports = mongoose.model("Teachers", TeachersSchema);
