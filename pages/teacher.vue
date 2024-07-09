<script setup lang="ts">
import AICard from '~/components/AICard.vue';
useHead({
  title: `API | Guru`,
  meta: [
    { name: 'Halaman guru API', content: 'Halaman guru asisten pelajar indonesia' }
  ],
})
const layout = "basic"
</script>

<template>
    <NuxtLayout :name="layout">
      <main class="cards"  style="background-color: #222;">
          <AICard
              title="Siasat Ngajar"
              heading="Siasat Ngajar"
              photo="/images/robot-8.jpg"
              subheading="Rancang strategi mengajar untuk guru" 
              description="Asisten yang akan membantu dalam kegiatan menstrategikan dan mendapatkan solusi untuk kegiatan mengajar" 
              link="/siasat-ngajar"
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