const express = require("express");
const router = express.Router();
const studentController = require("../controllers/StudentController");

router.post("/add-student", studentController.addStudent);
module.exports = router;
