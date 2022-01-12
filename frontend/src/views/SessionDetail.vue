<template>
  <div class="p-5">
    <div class="text-2xl mb-10">Session Details</div>
    <div class="text-xl">Session id: {{ $route.params.id }}</div>
    <div class="text-xl">Date: {{ date }}</div>
    <div class="text-xl">Time: {{ timeInterval }}</div>
    <div class="text-xl" v-if="status == 1">Status: Disabled</div>
    <div class="text-xl" v-if="status != 1">Status: Enabled</div>
    <div class="text-xl mb-4">Class: {{ classCode }}</div>
    <div class="btn mb-4" @click="toggleStatus">Toggle Session Status</div>
    <div>Class Attended by:</div>
    <section class="">
      <div class="overflow-x-auto">
        <table class="table w-full">
          <thead>
            <tr>
              <th>Name</th>
              <th>USN</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="i in attended" :key="i.sID">
              <td>{{ i.name }}</td>
              <td>{{ i.usn }}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>
  </div>
</template>

<script>
import axios from "axios";
export default {
  methods: {
    toggleStatus: function () {
      axios
        .post("http://localhost:5000/disableAttendance", {
          sessionID: this.sessionID,
        })
        .then((res) => {
          if (res.data.message === "enabled") {
            alert("enabled");
          } else if (res.data.message === "disabled") {
            alert("disabled");
          } else {
            alert("something went wrong ");
          }
        });
    },
  },
  data() {
    return {
      sessionID: this.$route.params.id,
      date: "",
      classCode: "",
      subjectCode: "",
      status: "",
      timeInterval: "",
      attended: [],
    };
  },
  beforeMount() {
    axios
      .post("http://localhost:5000/getSessionDetails", {
        sessionID: this.sessionID,
      })
      .then((res) => {
        this.date = res.data.date;
        this.classCode = res.data.classCode;
        this.subjectCode = res.data.subjectCode;
        this.timeInterval = res.data.timeInterval;
        this.status = res.data.status;
        this.attended = res.data.attended.map((item) => item);
      });
  },
};
</script>
