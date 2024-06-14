<script setup lang="ts">
import AICard from '~/components/AICard.vue';
useHead({
  title: `API | Universal`,
  meta: [
    { name: 'Halaman universal API', content: 'Halaman universal asisten pelajar indonesia' }
  ],
})
</script>

<template>
    <main class="cards">
        <AICard 
            title="NeuralNex" 
            heading="NeuralNex" 
            photo="/images/robot-6.jpg"
            subheading="AI Sehari-hari" 
            description="AI ini bisa digunakan untuk sehari hari, yang dimana AI ini salah satu untuk bisa membawa dampak positif dan meningkatkan relevansi konten yang di sajikan dan menganalisis prefensi pengguna dan memberikan rekomendasi yang sesuai"
            link="/"
        />
        <AICard
            title="VirtuGen"
            heading="VirtuGen"
            photo="/images/robot-5.jpg"
            subheading="Pembuat presentasi secara otomatis" 
            description="AI ini bisa digunakan untuk membuat Power Point yang dimana bisa membuat Power Point otomatis jika sudah memberi materi kepada AI nya"
            link="/"
        />
        <AICard 
            title="OptiMind AI"
            heading="OptiMind AI"
            photo="/images/robot-4.jpg"
            subheading="AI Sehari-hari"
            description="AI ini bisa digunakan untuk sehari hari, yang dimana AI ini salah satu untuk bisa membawa dampak positif dan meningkatkan relevansi konten yang di sajikan dan menganalisis prefensi pengguna dan memberikan rekomendasi yang sesuai"
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