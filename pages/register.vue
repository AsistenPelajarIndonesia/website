<script setup lang="ts">
useHead({
  title: `API | Register`,
  meta: [
    { name: 'Halaman daftar API', content: 'Halaman daftar asisten pelajar indonesia' }
  ],
})
const username: Ref<String> = ref("")
const password: Ref<String> = ref("")
const email: Ref<String> = ref("")
const inputType: Ref<string> = ref("password")
const inputImageFileName: Ref<string> = ref("/eye.png")

const eyeOnClick: VoidFunction = () => {
  if (inputImageFileName.value == "/eye.png") {
    inputImageFileName.value = "/eye-slash.png"
    inputType.value = "text"
  }
  else {
    inputImageFileName.value = "/eye.png"
    inputType.value = "password"
  }
}
</script>

<template>
  <main>
    <div class="login-box">
      <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/3.3.7/css/bootstrap.min.css">
      <div class="login">
        <h2>Daftar</h2>
        <section class="input-box">
          <input type="email" required placeholder="Email" v-model="email">
        </section>
        <section class="input-box">
          <input type="text" placeholder="Username" v-model="username">
        </section>
        <section class="input-box">
          <input :type="inputType" placeholder="Password" id="password" v-model="password">
          <img v-on:click="eyeOnClick" :src="inputImageFileName" alt="" id="toggle">
        </section>
        <footer class="input-box">
          <NuxtLink to="AI_Pelajar.html">
              <input type="submit" value="Daftar">
          </NuxtLink>   
        </footer>
        <article class="links">
          <NuxtLink to="/login">Masuk</NuxtLink>
        </article>
      </div>
    </div>
  </main>
</template>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Quicksand:wght@300&display=swap");
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: "Quicksand", sans-serif;
}
main {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  background: linear-gradient(crimson, #212122);
  width: 100%;
  overflow: hidden;
}

.login-box{
  position: absolute;
  top: 50%;
  left: 50%;
  width: 400px;
  height: 450px;
  padding: 40px;
  transform: translate(-50%, -50%);
  background: rgba(0, 0, 0, 0.5);
  box-sizing: border-box;
  box-shadow: 0 15px 25px rgba(0, 0, 0, 0.6);
  border-radius: 10px;
}

.login {
  position: absolute;
  width: 300px;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  gap: 20px;
  padding-left: 22px;
  padding-bottom: 100px;
}
.login h2 {
  font-size: 2em;
  color: #fff;
}
.login .input-box {
  position: relative;
  width: 100%;
}
.login .input-box input {
  position: relative;
  width: 100%;
  padding: 12px 20px;
  background: transparent;
  border: 2px solid #fff;
  border-radius: 15px;
  font-size: 1.2em;
  color: #fff;
  box-shadow: none;
  outline: none;
}
.login .input-box input[type="submit"] {
  width: 100%;
  background: #0078ff;
  background: linear-gradient(45deg, #aa0022, #ff0033);
  border: none;
  cursor: pointer;
}
.login .input-box input::placeholder {
  color: rgba(255, 255, 255, 0.75);
}
.login .links {
  position: relative;
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 0 20px;
}
.login .links a {
  color: #fff;
  text-decoration: none;
}
.login .links a:hover{
  color: #ff577f;
  transition: all .3s ease-in-out
}

#toggle{
  position: absolute;
  top: 43%;
  padding-top: 7px;
  transform: translateY(-50%);
  right: 12px;
  width: 27px;
  color: crimson;
  background-size: cover;
  cursor: pointer;
}
</style>