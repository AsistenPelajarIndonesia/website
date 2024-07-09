<script setup lang="ts">
import AICard from '~/components/AICard.vue';
useHead({
  title: `API | Siswa`,
  meta: [
    { name: 'Halaman siswa API', content: 'Halaman siswa asisten pelajar indonesia' }
  ],
})
const layout = "basic"
</script>
<template>
  <NuxtLayout :name="layout">
    <main class="cards"  style="background-color: #222;">
        <AICard
            title="Milarian Jawaban"
            heading="Milarian Jawaban"
            photo="/Milarian Jawaban.png"
            subheading="Mencari Jawaban" 
            description="Kesulitan menemukan jawaban? Yuk kita temukan dengan kecerdasan buatan yang terkoneksi dengan Buku Paket!" 
            link="/"
        />

    </main>
  </NuxtLayout>
</template>



<style scoped>
.cards {
    padding: 50px;
    display: flex;
    align-items: center;
    justify-content: center;
}
@media only screen and (max-width: 600px) {
  .cards {
    flex-direction: column;
  }
}
.links {
  text-decoration: none;
}
</style>