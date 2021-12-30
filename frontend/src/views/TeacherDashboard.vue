<template>
  <div>
    <div class="p-10 pb-0 text-2xl flex justify-between items-center">
      <div class="font-bold">Welcome, {{ teachername }}</div>
      <label for="my-modal-1" class="modal-button"
        ><div class="m-3">
          <img
            src="https://via.placeholder.com/50"
            class="rounded-2xl"
            alt=""
            srcset=""
          /></div
      ></label>
      <input type="checkbox" id="my-modal-1" class="modal-toggle" />
      <div class="modal">
        <div class="modal-box">
          <div class="text-2xl mb-5">Change Password</div>
          <input
            type="text"
            class="input w-full input-bordered my-3"
            placeholder="Current Password"
          />
          <input
            type="text"
            class="input w-full input-bordered my-3"
            placeholder="New Password"
          />
          <div class="modal-action">
            <label for="my-modal-1" class="btn btn-primary">Submit</label>
            <label for="my-modal-1" class="btn">Cancel</label>
          </div>
        </div>
      </div>
    </div>
    <div class="grid lg:grid-cols-3 lg:p-36 p-10 grid-cols-1">
      <SessionCard
        v-for="s in submissions"
        :key="s.sessionID"
        :sessionid="s.sessionID"
        :classid="s.classCode"
        :date="s.timeInterval"
        :subjectCode="s.subjectCode"
      />
    </div>
    <label
      for="my-modal-2"
      class="btn modal-button outline-none border-0 fixed bottom-0 w-full p-10 text-center bg-black text-white"
      >Create Session
    </label>
    <input type="checkbox" id="my-modal-2" class="modal-toggle" />
    <div class="modal">
      <div class="modal-box">
        <div class="text-2xl mb-5">Session Creation</div>
        <input
          type="text"
          class="input w-full input-bordered m-2"
          placeholder="Subject Code"
          v-model="subjectCode"
        />
        <input
          type="text"
          class="input w-full input-bordered m-2"
          placeholder="Class Code"
          v-model="classCode"
        />
        <input
          type="text"
          class="input w-full input-bordered m-2"
          placeholder="Time Interval"
          v-model="timeInterval"
        />
        <div class="modal-action">
          <div @click="createSession" class="btn btn-primary">Submit</div>
          <label for="my-modal-2" class="btn">Cancel</label>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import axios from "axios";
import AttendanceCard from "../components/AttendanceCard.vue";
import SessionCard from "../components/SessionCard.vue";

export default {
  data() {
    return {
      teachername: localStorage.getItem("tname"),
      submissions: [],
      subjectCode: "",
      classCode: "",
      timeInterval: "",
    };
  },
  methods: {
    createSession: function () {
      console.log("broooo");
      axios
        .post("http://localhost:5000/createSession", {
          subjectCode: this.subjectCode,
          classCode: this.classCode,
          timeInterval: this.timeInterval,
          tid: localStorage.getItem("tid"),
          date: "now",
        })
        .then((res) => {
          if (res.data.message === "created session") {
            alert("Session created. Session id: " + res.data.sessionID);
          }
        });
    },
  },
  beforeMount() {
    axios
      .post("http://localhost:5000/getAllSessionTeacher", {
        tid: localStorage.getItem("tid"),
      })
      .then((res) => {
        this.submissions = res.data.sessions.map((item) => item);
      });
  },
  components: { AttendanceCard, SessionCard },
};
</script>
