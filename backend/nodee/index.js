const express = require("express");
const mongoose = require("mongoose");
const app = express();
const studentRouter = require("./routes/StudentRouter");
const teachersRouter = require("./routes/TeachersRouter");
const attendanceRouter = require("./routes/AttendanceRouter");
const port = 3000;

app.use(express.json());
app.use("/student", studentRouter);
app.use("/teacher", teachersRouter);
app.use("/attendance", attendanceRouter);

mongoose
  .connect("mongodb://127.0.0.1:27017/attend", {
    useUnifiedTopology: true,
    useNewUrlParser: true,
  })
  .then(() => {
    console.log("yoyoyo its connected to da db hawwwyeeeeeee");
    app.listen(port, () => {
      console.log(`app listening at http://localhost:${port}`);
    });
  })
  .catch(() => console.log("Nononono Couldnt connect to server gay"));
