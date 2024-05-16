<script setup>
const props = defineProps({
    link: String,
    photo: String,
    role: String,
    message: String
})
</script>

<template>
    <div class="card">
        <NuxtLink :to="`${link}`" style="text-decoration: none;">
            <img :src="`${photo}`" class="img" alt="icon">
            <h1 class="name">{{ role }}</h1>
            <button class="button">{{ message }}</button>
        </NuxtLink>
    </div>
</template>
<style scoped>

name:link { 
  text-decoration: none; 
} 
name:visited { 
  text-decoration: none; 
} 
name:hover { 
  text-decoration: none; 
} 
name:active { 
  text-decoration: none; 
}
.img {
  border-radius: 100%;
  width: 60%;
  margin-top: 30px;
  margin-left: 38px;
}

.name {
    text-align: center;
    color: white;
    text-decoration-line: none;
    margin-top: 10px;
    text-transform: capitalize;
    text-decoration: none !important;
}

.button {
    outline: none;
    background: crimson;
    margin-left: 20px;
    border-radius: 30px;
    width: 80%;
    height: 10%;
    font-size: 15px;
    color: white;
    border: none;
}

.card {
  width: 220px;
  height: 274px;
  text-decoration: none;
  border-radius: 30px;
  background: #1d2630;
  border: white 1px solid;
}
</style>