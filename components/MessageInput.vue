<!-- components/MessageInput.vue -->
<template>
    <div class="message-input">
      <input
        type="text"
        v-model="message"
        @keypress.enter="sendMessage"
        placeholder="Type a message..."
      />
      <button @click="sendMessage">Send</button>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        message: ''
      };
    },
    methods: {
      sendMessage() {
        if (this.message.trim() !== '') {
          this.$emit('send', this.message);
          this.message = '';
        }
      }
    }
  }
  </script>
  
  <style>
  .message-input {
    display: flex;
    width: 80%;
  }
  .message-input input {
    flex: 1;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 5px 0 0 5px;
  }
  .message-input button {
    padding: 10px;
    border: none;
    background-color: #007bff;
    color: #fff;
    border-radius: 0 5px 5px 0;
    cursor: pointer;

  }
  .message-input button:hover {
    background-color: #0056b3;
  }
  </style>
  