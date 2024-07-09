<template>
    <NuxtLayout :name="layout">
        <iframe src="https://chatsv2-production.up.railway.app/Milarian_Jawaban" frameborder="0"></iframe>
    </NuxtLayout>
</template>

<script setup>
const layout = "basic"
</script>

<style>
iframe {
    width:  100%;
    height: 100%;
}
</style>