import Home from "./views/Home.vue";
import About from "./views/About.vue";
import NotFound from "./views/NotFound.vue";
import StudentLogin from "@/views/StudentLogin.vue";
import StudentSignup from "@/views/StudentSignup.vue";
import StudentDashboard from "@/views/StudentDashboard.vue";
export const routes = [
  { path: "/studentlogin", component: StudentLogin },
  { path: "/studentsignup", component: StudentSignup },
  { path: "/studentdashboard", component: StudentDashboard },
];
