<template>
  <div class="flex flex-col justify-center items-center h-screen">
    <div class="font-bold text-3xl mb-5">Attendify</div>
    <div class="p-10 card bg-base-200 w-full max-w-md">
      <div class="form-control">
        <label class="label">
          <span class="label-text">Username</span>
        </label>
        <input
          v-model="username"
          type="text"
          placeholder="username"
          class="input"
        />
        <label class="label">
          <span class="label-text mt-5">Password</span>
        </label>
        <input
          v-model="password"
          type="password"
          placeholder="password"
          class="input"
        />
        <div class="flex my-3 justify-between">
          <div
            @click="goToStudentSignup"
            class="cursor-pointer hover:text-primary transition-all"
          >
            sign up?
          </div>
          <div
            @click="goToTeacher"
            class="cursor-pointer hover:text-primary transition-all"
          >
            teacher? here
          </div>
        </div>

        <button @click="login" class="btn btn-primary mt-4">login</button>
      </div>
    </div>
  </div>
</template>
<script>
import axios from "axios";
export default {
  data() {
    return {
      username: "",
      password: "",
    };
  },
  methods: {
    goToStudentSignup: function () {
      this.$router.push("/studentsignup");
    },
    goToTeacher: function () {
      this.$router.push("/teacherlogin");
    },
    login: function (e) {
      e.preventDefault();
      console.log(this.username, this.password);
      //send to server
      axios
        .post("http://localhost:5000/loginstudent", {
          usn: this.username,
          password: this.password,
        })
        .then((res) => {
          if (res.data.message === "auth successful") {
            console.log(res.data.sid);
            //localStorage.setItem("sid", res.data.sid);
            this.$router.push("/studentdashboard");
          } else {
            alert("Something went wrong");
            this.username = "";
            this.password = "";
          }
        });
    },
  },
};
</script>
