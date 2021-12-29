<template>
  <div class="p-10 pb-0 text-2xl flex justify-between items-center">
    <div class="font-bold">Welcome, teacher</div>
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
    <SessionCard :sessionid="`sdf`" :classid="`broo`" :date="`today`" />
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
      />
      <input
        type="text"
        class="input w-full input-bordered m-2"
        placeholder="Class Code"
      />
      <input
        type="text"
        class="input w-full input-bordered m-2"
        placeholder="Time Interval"
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
import SessionCard from "../components/SessionCard.vue";

export default {
  components: { AttendanceCard, SessionCard },
};
</script>
