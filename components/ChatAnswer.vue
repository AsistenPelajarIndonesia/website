<script setup lang="ts">
defineProps({
    name: String,
})
</script>

<template>
    <UCard>
        <template #header>
            <section class="card-header">
                <img src="/icon.svg" width="25" height="25" alt="">
                <h1 class="ai-user-name">{{ name }}</h1>
            </section>
        </template>

        <slot></slot>
        <template #footer>
            <i class="ph ph-thumbs-up"></i>
            <i class="ph ph-thumbs-down"></i>
            <i class="ph ph-copy"></i>
            <i class="ph ph-repeat"></i>

        </template>
    </UCard>
</template>
<style scoped>
.card-header {
    display: flex;
}
.ai-user-name {
    font-family: 'Times New Roman', Times, serif;
}
</style>