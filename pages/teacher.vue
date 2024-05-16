<script setup lang="ts">
import AICard from '~/components/AICard.vue';
useHead({
  title: `API | Guru`,
  meta: [
    { name: 'Halaman guru API', content: 'Halaman guru asisten pelajar indonesia' }
  ],
})
</script>

<template>
    <main class="cards"  style="background-color: #222;">
        <AICard 
            title="Solution AI" 
            heading="Solution AI" 
            photo="/images/robot-7.jpg"
            subheading="Chat Untuk Mendapatkan Solusi!" 
            description="" 
            link="/"
        />
        <AICard
            title="Quantum IQ"
            heading="Quantum IQ"
            photo="/images/robot-8.jpg"
            subheading="Membantu pembuatan strategi mengajar!s" 
            description="AI ini dapat digunakan oleh guru untuk membuat strategi mengajar dan dapat memilih materi yang akan dibahas kepada murid untuk kedepannya, jadi AI ini bisa menjadi solusi untuk guru terutama dalam mengajar" 
            link="/"
        />

    </main>
</template>



<style scoped>
.cards {
    padding: 50px;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 10vw;
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