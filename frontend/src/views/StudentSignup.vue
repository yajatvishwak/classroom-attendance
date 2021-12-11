<template>
    <div class=" flex flex-col justify-center items-center h-screen">
        <div class="font-bold text-3xl mb-5">Attendify</div>
        <div class="p-10 card bg-base-200 w-full max-w-md">
        <div class="form-control ">
            <label class="label">
            <span class="label-text">Name</span>
            </label> 
            <input type="text" placeholder="Name" class="input">
            <label class="label">
            <span class="label-text">USN</span>
            </label> 
            <input type="text" placeholder="USN" class="input">
            <label class="label">
            <span class="label-text">Password</span>
            </label> 
            <input type="password" placeholder="password" class="input">
             <div class="dropdown mt-3 -ml-1">
                <div tabindex="0" class="m-1 btn">Choose all attended subjects</div> 
                <ul tabindex="0" class="p-2 shadow menu dropdown-content bg-base-100 rounded-box w-52">
                    <li>
                        <div class="flex justify-between">
                            <label class="cursor-pointer label">
                                <span class="label-text">FACD</span>
                            </label>
                            <input type="checkbox" checked="checked" class="checkbox checkbox-primary">
                        </div> 
                    </li>
                     <li>
                        <div class="flex justify-between">
                            <label class="cursor-pointer label">
                                <span class="label-text">OS</span>
                            </label>
                            <input type="checkbox"  class="checkbox checkbox-primary">
                        </div> 
                    </li>
                     <li>
                        <div class="flex justify-between">
                            <label class="cursor-pointer label">
                                <span class="label-text">Python</span>
                            </label>
                            <input type="checkbox"  class="checkbox checkbox-primary">
                        </div> 
                    </li>
                </ul>
            </div>
            <div class="flex my-3 justify-between">
                <div @click="goToStudentLogin" class="cursor-pointer hover:text-primary transition-all">login?</div>
                <div class=" cursor-pointer  hover:text-primary transition-all">teacher? here</div>
            </div>
          
            <button class="btn btn-primary mt-4 ">signup</button> 
        </div>
        </div>
    </div>
</template>
<script>
export default {
     methods: {
        goToStudentLogin() {
            this.$router.push("/studentlogin")
        },
     }
}
</script>