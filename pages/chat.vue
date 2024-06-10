<!-- pages/index.vue -->
<template>
    <div class="app">
      <UniversalChat :messages="messages" />
      <MessageInput @send="handleSend" />
    </div>
  </template>
  
  <script>
  import MessageInput from '~/components/MessageInput.vue';
  import UniversalChat from '~/components/UniversalChat.vue';
  //
  export default {
    components: {
      UniversalChat,
      MessageInput
    },
    data() {
      return {
        messages: []
      };
    },
    methods: {
      async handleSend(message) {
        const newMessage = { sender: 'user', text: message };
        this.messages.push(newMessage);
  
        // Simulate an API call
        const response = await $fetch(`https://ext.lakm.us:8080/api/v2/ai21/${message}`)
  
        const data = response;
        const botMessage = { sender: 'bot', text: data };
        this.messages.push(botMessage);
      }
    }
  }
  </script>
  
  <style>
  .app {
    display: flex;
    flex-direction: column;
    align-items: center;
    height: 100vh;
    justify-content: center;
    background-color: #f0f0f0;
  }
  </style>
  