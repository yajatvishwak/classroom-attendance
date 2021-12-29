import Home from "./views/Home.vue";
import About from "./views/About.vue";
import NotFound from "./views/NotFound.vue";
import StudentLogin from "@/views/StudentLogin.vue";
import StudentSignup from "@/views/StudentSignup.vue";
import StudentDashboard from "@/views/StudentDashboard.vue";
import TeacherDashboard from "@/views/TeacherDashboard.vue";
import TeacherLogin from "@/views/TeacherLogin.vue";
import SessionDetail from "@/views/SessionDetail.vue";
export const routes = [
  { path: "/studentlogin", component: StudentLogin },
  { path: "/studentsignup", component: StudentSignup },
  { path: "/studentdashboard", component: StudentDashboard },
  { path: "/teacherdashboard", component: TeacherDashboard },
  { path: "/teacherlogin", component: TeacherLogin },
  { path: "/sessiondetail/:id", component: SessionDetail },
];
