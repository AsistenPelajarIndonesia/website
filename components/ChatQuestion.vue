<script setup lang="ts">
defineProps({
    name: String,
})
</script>

<template>
    <UCard>
        <template #header>
            <section class="card-header">
                <i class="ph ph-user ph-fill"></i>
                <h3 class="ai-user-name">{{ name }}</h3>
            </section>
        </template>

        <slot></slot>

    </UCard>
</template>

<style scoped>
.card-header {
    display: flex;
    align-items: center;
}
</style>