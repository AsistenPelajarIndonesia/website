<script setup lang="ts">
useHead({
  title: `API | Beranda`,
  meta: [
    { name: 'Halaman Utama', content: 'Halaman utama asisten pelajar indonesia' }
  ],
})
const onClick = async () => 
  await navigateTo('https://nuxt.com', {
  external: true
  })
const layout = "basic";

</script>
<template>
    <NuxtLayout :name="layout">
      <main>
        <div class="content">
              <h1>BELAJAR BERSAMA AI</h1>
              <p>
                Membawa Pelajar Ke Dunia Baru
                <br>
                Asisten Pelajar Indonesia
              </p>
              <div>
                  <NuxtLink to="/ai">
                    <button>
                      <span></span>
                      TANYA AI
                    </button>
                  </NuxtLink>
                  <NuxtLink to="/">
                    <button>
                      <span></span>
                      PERSONALITY TEST
                    </button>
                  </NuxtLink>
              </div>
          </div>
      </main>
    </NuxtLayout>
</template>

<style scoped>
main {
  background-image: url("/bg.jpeg");
      font-family: sans-serif;

  height: 100vh;
    -webkit-background-size: cover;
    background-size: cover;
    background-position: center center;
    position: relative;
}
.content {
    width: 100%;
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
    text-align: center;
    color: #fff;
}

.content h1 {
    font-size: 40px;
    margin-top: 80px;
}

.content p {
    margin: 20px auto;
    font-weight: 100;
    line-height: 25px;
}

button {
    width:200px;
    padding: 15px 0;
    text-align:center;
    margin:20 px 10 px;
    border-radius:25px;
    font-weight:bold;
    border: 2px solid crimson;
    background: transparent;
    color:#fff;
    cursor: pointer;
    position: relative;
    overflow: hidden;
}
span {
    background: crimson;
    height: 100%;
    width: 0%;
    border-radius: 25px;
    position: absolute;
    left: 0;
    bottom: 0;
    z-index: -1;
    transition: 0.5s;
}
button:hover span {
    width: 100%;
}
button:hover {
    border: none;
}
</style>