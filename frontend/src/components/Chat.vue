<template>
  <div class="chat-container">
    <div class="chat-messages" ref="messagesContainer">
      <div v-for="(msg, idx) in messages" :key="idx" :class="['chat-message', msg.isMine ? 'mine' : 'other']">
        <span class="chat-user" v-if="!msg.isMine">{{ msg.user }}:</span>
        <span class="chat-text">{{ msg.text }}</span>
        <span class="chat-time">{{ msg.time }}</span>
      </div>
    </div>
    <form class="chat-input" @submit.prevent="sendMessage">
      <input v-model="newMessage" type="text" placeholder="Écrivez un message..." autocomplete="off" />
      <button type="submit">Envoyer</button>
    </form>
  </div>
</template>

<script>
export default {
  name: 'Chat',
  data() {
    return {
      messages: [],
      newMessage: '',
      username: 'Moi', // À remplacer par l'utilisateur courant
    };
  },
  methods: {
    sendMessage() {
      if (!this.newMessage.trim()) return;
      const now = new Date();
      this.messages.push({
        user: this.username,
        text: this.newMessage,
        time: now.toLocaleTimeString(),
        isMine: true,
      });
      this.newMessage = '';
      this.$nextTick(() => {
        const el = this.$refs.messagesContainer;
        if (el) el.scrollTop = el.scrollHeight;
      });
      // TODO: Envoyer le message au serveur via WebSocket ou API
    },
    receiveMessage(msg) {
      this.messages.push({
        user: msg.user,
        text: msg.text,
        time: msg.time,
        isMine: false,
      });
      this.$nextTick(() => {
        const el = this.$refs.messagesContainer;
        if (el) el.scrollTop = el.scrollHeight;
      });
    },
  },
  mounted() {
    // TODO: Initialiser la connexion WebSocket ici
    // Exemple de réception simulée :
    // setTimeout(() => this.receiveMessage({user: 'Alice', text: 'Bonjour !', time: new Date().toLocaleTimeString()}), 2000);
  },
};
</script>

<style scoped>
.chat-container {
  display: flex;
  flex-direction: column;
  height: 100vh;
  max-width: 500px;
  margin: 0 auto;
  border: 1px solid #ddd;
  border-radius: 8px;
  background: #fff;
}
.chat-messages {
  flex: 1;
  overflow-y: auto;
  padding: 1rem;
  background: #f9f9f9;
}
.chat-message {
  margin-bottom: 0.5rem;
  display: flex;
  flex-direction: column;
}
.chat-message.mine {
  align-items: flex-end;
}
.chat-message.other {
  align-items: flex-start;
}
.chat-user {
  font-weight: bold;
  margin-right: 0.5rem;
}
.chat-text {
  background: #e6f7ff;
  padding: 0.5rem 1rem;
  border-radius: 16px;
  margin-bottom: 2px;
  max-width: 70%;
  word-break: break-word;
}
.chat-message.mine .chat-text {
  background: #d1ffd6;
}
.chat-time {
  font-size: 0.75rem;
  color: #888;
  margin-top: 2px;
}
.chat-input {
  display: flex;
  border-top: 1px solid #eee;
  padding: 0.5rem;
  background: #fafafa;
}
.chat-input input {
  flex: 1;
  padding: 0.5rem;
  border: 1px solid #ccc;
  border-radius: 16px;
  margin-right: 0.5rem;
}
.chat-input button {
  width: fit-content;
  padding: 0.5rem 1rem;
  border: none;
  background: #1890ff;
  color: #fff;
  border-radius: 16px;
  cursor: pointer;
  transition: background 0.2s;
}
.chat-input button:hover {
  background: #40a9ff;
}
</style>
