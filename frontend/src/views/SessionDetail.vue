<template>
  <div class="p-5">
    <div class="text-2xl mb-10">Session Details</div>
    <div class="text-xl">{{ $route.params.id }}</div>
    <div class="text-xl">date</div>
    <div class="text-xl mb-4">class code</div>
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
            <tr>
              <td>Cy Ganderton</td>
              <td>1NH19CS200</td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>
  </div>
</template>
