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
            @click="goToStudent"
            class="cursor-pointer hover:text-primary transition-all"
          >
            student? here
          </div>
        </div>

        <button @click="onClickLogin" class="btn btn-primary mt-4">
          login
        </button>
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
    // goToStudentSignup: function () {
    //   this.$router.push("/teacherlo");
    // },
    onClickLogin: function (e) {
      e.preventDefault();
      axios
        .post("http://localhost:5000/loginteacher", {
          usn: this.username,
          password: this.password,
        })
        .then((res) => {
          if (res.data.message === "auth successful") {
            localStorage.setItem("tid", res.data.tid);
            localStorage.setItem("tname", res.data.name);
            this.$router.push("/teacherdashboard");
          } else {
            alert("something went wrong");
          }
        });
    },
    goToStudent: function () {
      this.$router.push("/studentlogin");
    },
  },
};
</script>
