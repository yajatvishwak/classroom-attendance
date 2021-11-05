const { nanoid } = require("nanoid");
const Attendance = require("../models/Attendance");
const Student = require("../models/Student");
let report = [];

let makeSession = async (req, res) => {
  const { teacherID, sessionName, classID } = req.body;
  const id = nanoid();
  const session = new Attendance({
    teacherID: teacherID,
    classID: classID,
    on: Date.now(),
    sessionID: id,
    sessionName: sessionName,
    attendance: [],
  });
  try {
    await session.save();
    res.send({ message: "success", status: 200, sessionID: id });
  } catch (error) {
    console.log(error);
    res.send({ message: "failed", status: 500 });
  }
};

let punchAttendance = async (req, res) => {
  const { studentID, deviceID, sessionID } = req.body;
  console.log({ studentID, deviceID, sessionID });
  try {
    const student = await Student.findOne({ studentID: studentID });
    const session = await Attendance.findOne({
      sessionID: sessionID,
    });
    console.log(session);
    console.log(student);
    const lastdeviceID = student.lastLogin.deviceID;

    //TODO : check if already punched
    //TODO : check if 2 students have the same device id

    //check if someone else used the same device id
    let cheat = false;
    //check if same person is giving attendance again
    let dup = false;
    session.attendance.map((item) => {
      if (item.deviceID === deviceID && item.studentID !== studentID)
        cheat = true;
      if (item.deviceID === deviceID && item.studentID === studentID)
        dup = true;
    });
    if (cheat) {
      report.push({
        studentID: studentID,
        deviceID: deviceID,
        sessionID: sessionID,
        reason: "Device already used to punch attendance",
      });
      return res.send({ message: "2 Accounts, on device", status: 400 });
    }
    if (dup) {
      return res.send({ message: "duplicate", status: 400 });
    }

    if (lastdeviceID !== deviceID) {
      // student tried to alter the app
      report.push({
        studentID: studentID,
        deviceID: deviceID,
        sessionID: sessionID,
        reason: "Change of device/ Tried to uninstall/ Random Check",
      });
      return res.send({ message: "suspect", status: 400 });
    }
    // last device id and this one is same
    // logging in from same device, punch attendance
    await Attendance.updateOne(
      { sessionID },
      { $push: { attendance: { studentID: studentID, deviceID: deviceID } } }
    );
    return res.send({ message: "success", status: 200 });
  } catch (error) {
    console.log(error);
    res.send({ message: "failed", status: 500 });
  }
};

let getReported = async (req, res) => {
  const { sessionID } = req.body;
  const payload = report.filter((item) => {
    if (item.sessionID === sessionID) return item;
  });
  res.send(payload);
};

exports.makeSession = makeSession;
exports.punchAttendance = punchAttendance;
exports.getReported = getReported;
