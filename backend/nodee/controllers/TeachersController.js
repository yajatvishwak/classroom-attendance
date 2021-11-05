const Teachers = require("../models/Teachers");
const { nanoid } = require("nanoid");
let addTeachers = async (req, res) => {
  const { teacherusn, name, password, classHandled } = req.body;
  console.log("Incoming: ", { teacherusn, name, classHandled });
  const newTeach = new Teachers({
    teacherID: nanoid(),
    name: name,
    classHandled: classHandled,
    teacherUSN: teacherusn,
    password: password,
  });
  try {
    await newTeach.save();
    res.send({ message: "success", status: 200 });
  } catch (error) {
    console.log(error);
    res.send({ message: "failed", status: 500 });
  }
};

exports.addTeachers = addTeachers;
