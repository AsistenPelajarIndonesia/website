<script setup lang="ts">
import AICard from '~/components/AICard.vue';
useHead({
  title: `API | Universal`,
  meta: [
    { name: 'Halaman universal API', content: 'Halaman universal asisten pelajar indonesia' }
  ],
})
const layout = "basic"
</script>

<template>
    <NuxtLayout :name="layout">
    <main class="cards">
        <AICard 
            title="Hiji Ka Hiji" 
            heading="Hiji Ka Hiji" 
            photo="/Hiji Ka Hiji.png"
            subheading="Teman mengobrol" 
            description="Butuh teman untuk berbicara dan berbagi isi pikiran? Kecerdasan Buatan ini akan berusaha untuk membantumu untuk hal tersebut!"
            link="/"
        />
        <AICard
            title="PPT Gen"
            heading="PPT Gen"
            photo="/Coming Soon.png"
            subheading="Bikin PPT Dipermudah" 
            description="Kecerdasan buatan digunakan untuk membuat Power Point yang secara otomatis hanya dengan memberikan materi kepadanya"
            link="/"
        />
        <AICard 
            title="Warta Palsu?"
            heading="Warta Palsu?"
            photo="/Warta Palsu.png"
            subheading="Pendeteksi Hoax"
            description="Apakah ini berita palsu atau bukan? Dengan adanya 'Warta Palsu?' anda dapat mengecek kebeneran berita dengan kecerdasan buatan!"
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
    justify-content: space-between;
    background-color: #222;
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