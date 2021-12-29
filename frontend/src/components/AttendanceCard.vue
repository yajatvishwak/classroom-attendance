<template>
  <div class="card bordered m-3 last-of-type:mb-20">
    <div class="card-body">
      <div class="card-title flex items-center justify-between">
        <div>{{ subname }}</div>
      </div>

      <div>
        <div class="text-3xl font-bold text-center mt-3">
          {{ (parseInt(attended) / parseInt(conducted)) * 100 }}%
        </div>
      </div>
      <div class="my-5 text-center">
        {{ conducted }} Classes was/were conducted, {{ attended }} was/were
        attended by you
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "AttendanceCard",
  props: ["subname", "conducted", "attended"],
};
</script>
