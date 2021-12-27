<template>
  <div class="card bordered m-3 last-of-type:mb-20">
    <div class="card-body">
      <div class="card-title flex items-center justify-between">
        <div>OS</div>
        <div class="badge badge-primary">low attendance</div>
      </div>

      <div>
        <div class="text-3xl font-bold text-center mt-3">30%</div>
      </div>
      <div class="my-5 text-center">
        100 Classes were conducted, 30 were attended by you
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "AttendanceCard",
};
</script>
