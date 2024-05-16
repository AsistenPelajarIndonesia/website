<script setup lang="ts">
useHead({
  title: `API | Login`,
  meta: [
    { name: 'Halaman daftar API', content: 'Halaman daftar asisten pelajar indonesia' }
  ],
})
const username: Ref<String> = ref("")
const password: Ref<String> = ref("")
const email: Ref<String> = ref("")
const isUserLoggedOut = useState("isSidebarOpened", () => true)
  const registerUser = () => {
    console.log(username.value)
    console.log(password)
    console.log(email)
    console.log(isUserLoggedOut)
    const isUserLoggedin = useState("isSidebarOpened", () => true)
    
}
</script>

<template>
    <main class="register-base">
        <article class="login">
    <h2>Daftar</h2>
    <div class="inputBx">
      <input v-model="username" type="text" placeholder="Username">
    </div>
    <div class="inputBx">
      <input v-model="password" type="password" placeholder="Password">
    </div>
    <div class="inputBx">
        <input v-model="email" type="text" placeholder="Email">
    </div>
    <button class="register-button" type="submit" v-on:click="registerUser">Register</button>
    <div class="links">
      <a href="masuk.html">{{  }}</a>
    </div>
</article>
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
.register-base {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  background: #111;
  width: 100%;
  max-height: 100vh;
  overflow: hidden;

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
}
.login h2 {
  font-size: 2em;
  color: #fff;
}
.login .inputBx {
  position: relative;
  width: 100%;
}
.login .inputBx input {
  position: relative;
  width: 100%;
  padding: 12px 20px;
  background: transparent;
  border: 2px solid #fff;
  font-size: 1.2em;
  color: #fff;
  box-shadow: none;
  outline: none;
  border-radius: 15px;

}
.register-button {
    border-radius: 15px;

  padding: 12px 20px;
  font-size: 1.2em;
  color: #fff;
  width: 100%;
  background: #0078ff;
  background: linear-gradient(45deg, #aa0022, #ff0033);
  border: none;
  cursor: pointer;
}
.login .inputBx input::placeholder {
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
</style>