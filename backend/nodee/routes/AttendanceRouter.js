const express = require("express");
const router = express.Router();
const attendanceController = require("../controllers/AttendanceController");

router.post("/make-session", attendanceController.makeSession);
router.post("/punch-attendance", attendanceController.punchAttendance);
module.exports = router;
