<script setup lang="ts">
useHead({
  title: `API | Login`,
  meta: [
    { name: 'Halaman Login API', content: 'Halaman login asisten pelajar indonesia' }
  ],
})
const username: Ref<String> = ref("")
const password: Ref<String> = ref("")
</script>

<template>
    <main class="container">
      <article class="login">
        <h1 class="login-title">Login</h1>
        <section class="input-box">
          <input v-model="username" type="text" placeholder="Username">
        </section>
        <section class="input-box">
          <input v-model="password" type="password" placeholder="Password">
        </section>
        <section class="input-box input-box-submit">
            <input type="submit" value="Sign in" v-on:click="">
        </section>
        <section class="register-link">
          <NuxtLink class="link" to="/register">Sign Up</NuxtLink>
        </section>
      </article>
    </main>
</template>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Quicksand:wght@300&display=swap");
* {
  font-family: "Quicksand", sans-serif;
}
.container {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  background: #111;
  width: 100%;
  overflow: hidden;
}

.login {
  width: 300px;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  gap: 20px;
}
.login-title {
  font-size: 2em;
  color: #fff;
}
.input-box {
  position: relative;
  width: 100%;
}
.input-box {
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
.input-box-submit {
  width: 100%;
  background: #0078ff;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  background: linear-gradient(45deg, #aa0022, #ff0033);
  border: none;
  cursor: pointer;
}
.input-box input::placeholder {
  color: rgba(255, 255, 255, 0.75);
}
.register-link {
  position: relative;
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 0 20px;
}
.register-link .link {
  color: #fff;
  text-decoration: none;
}
.register-link .link:hover{
  color: #ff577f;
  transition: all .3s ease-in-out
}
</style>