const Student = require("../models/Student");
const { nanoid } = require("nanoid");
let addStudent = async (req, res) => {
  const { usn, name, classID, password } = req.body;
  console.log("Incoming: ", { usn, name, classID });
  const newStud = new Student({
    studentID: nanoid(),
    name: name,
    classID: classID,
    usn: usn,
    password: password,
    lastLogin: {
      time: Date.now(),
      deviceID: "oneplus",
    },
  });
  try {
    await newStud.save();
    res.send({ message: "success", status: 200 });
  } catch (error) {
    console.log(error);
    res.send({ message: "failed", status: 500 });
  }
};

exports.addStudent = addStudent;
