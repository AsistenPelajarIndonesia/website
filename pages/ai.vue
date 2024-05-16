<script setup lang="ts">
import AITypeCard from '~/components/AITypeCard.vue';

useHead({
  title: `API | AI`,
  meta: [
    { name: 'Halaman Kumpulan AI', content: 'Halaman kumpulan AI asisten pelajar indonesia' }
  ],
})

</script>
<template>
    <main class="ai">
        <article  class="cards">
            <AITypeCard link="/" photo="/images/teacher-icon.png" role="Guru" message="Asisten Guru"/>
            <AITypeCard link="/" photo="/images/universal-icon.png" role="Sehari-Hari" message="Asisten Universal"/>
            <AITypeCard link="/" photo="/images/student-icon.png" role="Pelajar" message="Asisten Pelajar"/>
        </article> 
    </main>
</template>


<style scoped>
.ai {
    background-color: #222;
    min-height: 150vh;
}
.cards {
    padding: 100px;
    display: flex;
    align-items: center;
    justify-content: space-between;
}
@media only screen and (max-width: 600px) {
  .cards {
    flex-direction: column;
    height: 120vh;
  }
  .card {
    margin-bottom: 2rem;
  }
}
.links {
  text-decoration: none;
}
</style>