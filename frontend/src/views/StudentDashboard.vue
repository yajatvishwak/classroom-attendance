<template>
  <div class="p-10 pb-0 text-2xl flex justify-between items-center">
    <div class="font-bold">Welcome, {{ sname }}</div>
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
  <div class="px-10 pb-0">teri attendance ki maa chudi padi hai hehe</div>

  <div class="grid lg:grid-cols-3 lg:p-36 p-10 grid-cols-1">
    <AttendanceCard
      v-for="a in attendance"
      :conducted="a.conducted"
      :subname="a.subname"
      :attended="a.attended"
      :key="a.message"
    />
  </div>

  <label
    for="my-modal-2"
    class="btn modal-button outline-none border-0 fixed bottom-0 w-full p-10 text-center bg-black text-white"
    >Punch Attendance</label
  >
  <input type="checkbox" id="my-modal-2" class="modal-toggle" />

  <div class="modal">
    <div class="modal-box">
      <div class="text-2xl mb-5">Mark Attendance for Session</div>
      <input
        type="text"
        v-model="sessionID"
        class="input w-full input-bordered"
        placeholder="Session Code"
      />

      <div class="modal-action">
        <label for="my-modal-2" @click="punchAttendance" class="btn btn-primary"
          >Submit</label
        >
        <label for="my-modal-2" class="btn">Cancel</label>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import axios from "axios";
import AttendanceCard from "../components/AttendanceCard.vue";

export default {
  beforeMount() {
    axios
      .post("http://localhost:5000/getAttendance", { sID: this.sid })
      .then((res) => {
        console.log(res.data.data);
        this.attendance2 = res.data.data;
        let subjects = Object.keys(this.attendance2);

        this.attendance = subjects.map((item) => {
          return {
            subname: item,
            conducted: this.attendance2[item].conducted,
            attended: this.attendance2[item].attended,
          };
        });
        console.log(this.attendance);
      });
  },
  data() {
    return {
      sid: localStorage.getItem("sid"),
      sname: localStorage.getItem("sname"),
      sessionID: "",
      attendance2: {},
      attendance: [],
    };
  },
  methods: {
    punchAttendance: function () {
      axios
        .post("http://localhost:5000/punchAttendance", {
          sID: this.sid,
          sessionID: this.sessionID,
        })
        .then((res) => {
          if (res.data.message === "added attendance") {
            alert("added");
          } else {
            alert("something went wrong");
          }
        });
    },
  },
  components: { AttendanceCard },
};
</script>
