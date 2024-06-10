<!-- components/ChatWindow.vue -->
<template>
  <div class="chat-window" ref="chatWindow">
    <div v-for="(msg, index) in messages" :key="index" :class="['message', msg.sender]">
      {{ msg.text }}
    </div>
    <div ref="chatEnd"></div>
  </div>
</template>

<script>
export default {
  props: {
    messages: {
      type: Array,
      required: true
    }
  },
  watch: {
    messages() {
      this.scrollToBottom();
    }
  },
  methods: {
    scrollToBottom() {
      this.$nextTick(() => {
        console.log("success")
        this.$refs.chatEnd.scrollIntoView();
      });
    }
  }
}
</script>

<style>
.chat-window {
  width: 80%;
  max-height: 400px;
  background-color: #888;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
  overflow-y: scroll;
  margin-bottom: 10px;
  -webkit-overflow-scrolling: auto;

}
.message {
  margin: 5px 0;
}
.message.user {
  text-align: right;
}
.message.bot {
  text-align: left;
}
</style>
