<script setup lang="ts">
import AICard from '~/components/AICard.vue';
useHead({
  title: `API | Siswa`,
  meta: [
    { name: 'Halaman siswa API', content: 'Halaman siswa asisten pelajar indonesia' }
  ],
})
</script>
<template>
    <main class="cards"  style="background-color: #222;">
        <AICard 
            title="Noah Neural" 
            photo="/images/robot-3.jpg"
            heading="Noah Neural" 
            subheading="Bimbingan Belajar dengan AI" 
            description="Untuk membantu murid, AI ini bisa digunakan untuk bertanya, selain bertanya AI ini bisa digunakan mengobrol sehingga murid merasa mengobrol dengan temannya, dapat membantu murid untuk tidak kesepian" 
            link="/"
        />
        <AICard
            title="InsightIQ"
            heading="InsightIQ"
            photo="/images/robot-1.jpg"
            subheading="Latihan Soal AI" 
            description="AI ini Untuk latihan soal para murid, sehingga murid dapat berlatih untuk bisa mendalami materi yang di pelajari dengan cara mengerjakan latihan soal, murid akan semakin mudah untuk berlatih kemampuannya" 
            link="/"
        />
        <AICard 
            title="EvolveAI"
            heading="EvolveAI"
            photo="/images/robot-2.jpg"
            subheading="Mencari materi disinilah tempatnya!"
            description="AI ini Bisa digunakan oleh para murid untuk bertanya tentang materi di sekolah, sehingga jika murid kurang paham dengan materi yang di pelajari sekolah, murid bertanya kepada AI ini sehingga murid akan lebih mengerti tentang materi nya" 
            link="/"
        />

    </main>
</template>



<style scoped>
.cards {
    padding: 50px;
    display: flex;
    align-items: center;
    justify-content: space-between;
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