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
              <div class="buttons-wrap">
                  <NuxtLink to="/ai" class="button-wrap">
                    <button>
                      <span></span>
                      <div>Tanya AI</div>
                    </button>
                  </NuxtLink>
                  <NuxtLink to="/soal" class="button-wrap">
                    <button>
                      <span></span>
                      <div>Buat Soal</div>
                    </button>
                  </NuxtLink>
              </div>
          </div>
      </main>
    </NuxtLayout>
</template>

<style scoped>
* {margin: 0; padding: 0;}
main {
  background-image: url("/bg.jpeg");
      font-family: sans-serif;

  height: 100%;
    -webkit-background-size: cover;
    background-size: cover;
    background-position: center center;
    position: relative;
}
.button-wrap {
  display: flex;
  justify-content: center;
  align-items: center;
}
.buttons-wrap {
  display: flex;
  justify-content: center;
  align-items: center;
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
    font-weight:bold;

}

.content p {
    margin: 20px auto;
    font-weight: 100;
    line-height: 25px;
    
}

button {
    width: 11rem;
    padding: 15px 0;
    text-align:center;
    margin: 1rem 0.5rem;
    padding: 1.37rem;
    border-radius:25px;
    border: 2px solid crimson;
    background: rgb(154, 7, 37);
    cursor: pointer;
    position: relative;
    display: flex;
    justify-content: center;
    align-items: center;
}
button div {
  font-weight:bold;
  color:#fff;
  z-index: 4;
  position: absolute;

}
span {
    background: crimson;
    height: 100%;
    width: 0%;
    border-radius: 25px;
    position: absolute;
    left: 0;
    bottom: 0;
    z-index:2;
    transition: 0.5s;
}
button:hover span {
    width: 100%;
}
button:hover {
    border: none;
}
@media only screen and (max-width: 600px) {
    .buttons-wrap {
      flex-direction: column;
    }
    button {
      margin: 0.3rem 0.5rem;
    }
}
</style>