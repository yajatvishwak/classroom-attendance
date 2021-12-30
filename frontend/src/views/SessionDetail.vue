<template>
  <div class="p-5">
    <div class="text-2xl mb-10">Session Details</div>
    <div class="text-xl">Session id: {{ $route.params.id }}</div>
    <div class="text-xl">Date: {{ date }}</div>
    <div class="text-xl">Time: {{ timeInterval }}</div>
    <div class="text-xl mb-4">Class: {{ classCode }}</div>
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
  data() {
    return {
      sessionID: this.$route.params.id,
      date: "",
      classCode: "",
      subjectCode: "",
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
        this.attended = res.data.attended.map((item) => item);
      });
  },
};
</script>
