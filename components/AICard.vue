<script setup>
const props = defineProps({
    title: String,
    photo: String,
    heading: String,
    subheading: String,
    description: String,
    link: String
})
</script>

<template>
    <div class="card">
        <h2 class="card-title">{{ title }}</h2>
        <img :src="`${photo}`" class="card-img" alt="illustrations">
        <div class="card-body">
            <h1 class="card-heading">{{ heading }}</h1>
            <h2 class="card-subheading">{{ subheading }}</h2>
            <p class="card-description">{{ description }}</p>
            <NuxtLink :to="`${link}`">
                <button class="card-button">Gunakan</button>
            </NuxtLink>
        </div>
    </div>
</template>

<style scoped>
*  {
    box-sizing: border-box;
}

.card {
    width: 350px;
    height: 400px;
    border-radius: 20px;
    overflow: hidden;
    border: 4px solid #fff;
    position: relative;
    z-index:0;
}
.card-img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}

.card-title {
    display: block;
    text-align: center;
    color: #fff;
    background-color: crimson;
    padding: 2%;
    border-top-right-radius: 12px;
    border-top-left-radius: 12px;
}

.card-body {
    width: 100%;
    height: 100%;
    top: 0;
    right: -100%;
    position: absolute;
    background: #1f3d4738;
    backdrop-filter: blur(5px);
    border-radius: 15px;
    color: #fff;
    padding: 30px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    transition: 2s;
}

.card:hover .card-body {
    right: 0;
}

.card-heading {
    font-size: 50px;
    font-weight: 500;
}

.card-subheading {
    text-transform: capitalize;
    font-size: 14px;
    font-weight: 300;
}

.card-description {
    font-size: 16px;
    line-height: 25px;
    margin: 40px 0;
    font-weight: 400;
}

.card-button {
    color: #fff;
    background: crimson;
    width: 120px;
    padding: 10px 20px;
    border-radius: 5px;
    text-transform: capitalize;
    border: none;
    outline: none;
    font-weight: 500;
    cursor: pointer;
}
@media only screen and (max-width: 600px) {
    .card {
      margin-bottom: 2rem;
      width: 300px;
      height: 90vh;
    }
  }
  .links {
    text-decoration: none;
  }
</style>