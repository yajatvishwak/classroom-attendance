<template>
  <div
    @click="navigateToSessionDetails"
    class="card bordered m-3 last-of-type:mb-20"
  >
    <div class="card-body">
      <div class="card-title flex items-center justify-between">
        <div>
          {{ this.classid }} - {{ this.sessionid }} - {{ this.date }} -
          {{ this.subjectCode }}
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: ["sessionid", "classid", "date", "subjectCode"],
  name: "SessionCard",
  methods: {
    navigateToSessionDetails() {
      this.$router.push("/sessiondetail/" + this.sessionid);
    },
  },
};
</script>
