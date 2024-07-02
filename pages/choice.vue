<template>
    <main class="choices">
        <UCard class="choice">
            <template #header>
                <img src="https://upload.wikimedia.org/wikipedia/commons/9/9c/TOEFL_Logo.svg" alt="">
            </template>

            <Placeholder class="h-32" />
            <UButton color="red" variant="solid">Kerjakan Latihan</UButton>
            <UButton color="blue" variant="solid">Pelajari Materi</UButton>
            <UButton color="white" variant="solid">Ambil Simulasi</UButton>
        </UCard>
    </main>
</template>

<style>
.choices {
    padding: 1rem;
}
.choice {
    background-color: white !important;
}
</style>