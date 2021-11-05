const express = require("express");
const router = express.Router();
const teachersController = require("../controllers/TeachersController");

router.post("/add-teacher", teachersController.addTeachers);
module.exports = router;
