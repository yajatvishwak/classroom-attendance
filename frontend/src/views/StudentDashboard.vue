<template>
  <div class="p-10 pb-0 text-2xl flex justify-between items-center">
    <div class="font-bold">Welcome, username</div>
    <div class="m-3">
      <img
        src="https://via.placeholder.com/50"
        class="rounded-2xl"
        alt=""
        srcset=""
      />
    </div>
  </div>
  <div class="px-10 pb-0">teri attendance ki maa chudi padi hai hehe</div>

  <div class="grid lg:grid-cols-3 lg:p-36 p-10 grid-cols-1">
    <AttendanceCard />
    <AttendanceCard />
    <AttendanceCard />
  </div>
  <!-- <div class="fixed bottom-0 w-full p-10 text-center bg-black text-white">
    Punch Attendance
  </div> -->
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
        class="input w-full input-bordered"
        placeholder="Session Code"
      />

      <div class="modal-action">
        <label for="my-modal-2" class="btn btn-primary">Submit</label>
        <label for="my-modal-2" class="btn">Cancel</label>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import AttendanceCard from "../components/AttendanceCard.vue";

export default {
  components: { AttendanceCard },
};
</script>
