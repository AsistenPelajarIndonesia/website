<script setup>
const route = useRoute()
const aiName = useState("aiName", () => route.params.ai)
const userName = "John"

useHead({
  title: `API | ${aiName.value}`,
  meta: [
    { name: 'Chat Page', content: 'Go here to chat with an ai' }
  ],
})

const conversations = useState("conversations",() => ref([]))
const question = ref('')

async function getAnswer() {
    return await $fetch(`http://ext.lakm.us:8080/api/v2/${aiName.value}/${question.value}`)
}

async function displayAnswer() {
    const answer = await getAnswer()
    conversations.value.push(
        {
            question: question.value, 
            answer: answer.answer.content
        }
    )
}

</script>

<template>
    <Ucontainer class="container">
        <UContainer class="chat-box">
            <main v-for="conversation in conversations"  style="padding-top: 1.5rem;">
                <ChatQuestion name="Tamu" style="margin-bottom: 1rem;">{{ conversation.question }}</ChatQuestion>
                <ChatAnswer name="Asisten Pelajar Indonesia" style="margin-top: 1rem;">{{ conversation.answer }}</ChatAnswer>
            </main>
            <Placeholder class="h-32" />
        </UContainer>
        <section class="send">
            <UInput v-model="question" style="min-width: 80vw;" />
            <UButton color="primary" variant="solid" v-on:click="displayAnswer"><i class="ph ph-paper-plane-right"></i></UButton>
        </section>
        {{ result }}
    </Ucontainer>
</template>

<style>
.container {
    display: flex;
    min-width: 80vw;
    align-items: center;
    flex-direction: column; 
    justify-content: center;
}
.chat-box {
    min-width: 80vw;
    min-height: 80vh;
    overflow-y: scroll;
    overflow-x: inherit;
    word-wrap: break-word;
    max-width: 80vw;
    max-height: 80vh;
    padding-bottom: 2rem;
}
.send {
    display: flex;
    position: absolute;
    flex-direction: row;
    bottom: 0;
    margin-bottom: 2rem;
}
.question {
    min-width: 80vw;
    padding: 1rem;
    background: wheat;
}
.answer {
    min-width: 80vw;
    padding: 1rem;
    background: gray;
}
</style>