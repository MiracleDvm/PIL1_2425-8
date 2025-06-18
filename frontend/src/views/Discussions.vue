<template>
  <div class="chat-app">
    <!-- Barre latérale des conversations -->
    <div class="chat-sidebar">
      <h3> Conversations </h3>
      <ul class="conversation-list">
        <li 
        	v-for="conversation in conversations" 
        	:key="conversation.id" 
        	:class="{active: conversation.id === selectedConversation.id}" 
        	@click="selectConversation(conversation)">
          <span v-if="conversation.participants.length > 1"> {{ getConversationName(conversation) }} </span>
          <span v-else> Discussion avec soi-meme </span>
        </li>
      </ul>
    </div>

		<!-- Zone principale du chat -->
		<div class="chat-main">
			<div class="chat-header">
				<h3>
					<!-- Aficher le nom (ou les participants) de la coversation -->
					{{ selectedConversation ? getConversationName(selectedConversation) : 'Aucune conversation' }}
				</h3>
			</div>
			<div class="chat-messages" ref="chatMessages">
				<div 
					v-for="(message, index) in selectedConversation.messages" 
					:key="index" 
					:class=" ['chat-message', message].sender === currentUser ? 'sent' : 'received' ">
					<div class="message-content">{{ message.text }}</div>
					<div class="message-time">{{ formatTime(message.timestamp) }}</div>
				</div>
			</div>
			<form class="chat-input" @submit.prevent = "sendMessage">
				<input class="" type="text" v-model="newMessage" placeholder="Tapez votre message ..." required @keyup.enter="sendMessage">
				<button type="submit" class="send-button">
					<!-- Utilisation d'une icone (paper plane) pour envoyer -->
					<i class="bi bi-send-fill"></i>
				</button>
			</form>
		</div>
  </div>
</template>

<script>
export default {
	name: "Chat",
	data() {
		return {
			currentUser: "Moi",// Vous remplacerez cette valeur avec les infos de l'utilisateur connecté (par ex. via Vuexou props)
			newMessage: "",
			// Liste des conversations.
			conversations: [],
			selectedConversation: null,
		};
	},
	methods: {
		// Selectionne une conversation dans la barre latérale
		selectConversation(conversation) {
			this.selectedConversation = conversation;
			this.$nextTick(() => {
				this.scrollToBottom();
			});
		},
		// Envoie un message dans la conversation sélectionnée.
		sendMessage() {
			if (this.newMessage.trim() !== "") {
				const message = {
					text: this.newMessage,
					sender: this.currentUser,
					timestamp: new Date(),
				};
				if (!this.selectedConversation) return;
				this.selectedConversation.messages.push(message);
				this.newMessage = "",
				this.$nextTick(() => {
					this.scrollToBottom();
				});
			}
		},
		// Défilement automatique vers le bas de la zone des messages.
		scrollToBottom() {
			const container = this.$refs.chatMessages;
			if (container) {
				container.scrollTop = container.scrollHeight;
			}
		},
		// Formate l'heure du messa ge de manière lisible.
		formatTime(timestamp) {
			const date = new Date(timestamp);
			return date.toLocaleTimeString([], { hour: "2-digit", minute: "2-digit" });
		},
		// Retourne un libelllé pour la conversation en excluant l'utilisateur courant des participants.
		getConversationName(conversation) {
			const otherParticipants = conversation.participants.filter((participant) => participant !== this.currentUser);
			return otherParticipants.length === 0 ? "Discussion avec soi-meme" : otherParticipants.join(",");
		},
		// Récupère (ou simule) la liste des conversations.
		fetchConversations() {
			if (this.conversations.length === 0) {
				const selfConversation = {
					id: 1,
					participants: [this.currentUser],
					messages: [
						{
							text: "Bienvenue dans votre discussion personnelle !",
							sender: this.currentUser,
							timestamp: new Date(),
						},
					],
				};
				this.conversations.push(selfConversation);
			}
			// Sélectionne la première conversation par défaut.
			this.selectedConversation = this.conversations[0];
		},
	},
	mounted() {
		this.fetchConversations();
		this.$nextTick(() => {
			this.scrollToBottom();
		});
	},
};
</script>

<style scoped>
.chat-app {
	display: flex;
	height: 100vh;
}
/** Barre latérale des conversations */
.chat-sidebar {
	width: 250px;
	background-color: var(--secondary-color, #6c757d);
	padding: 20px;
	color: #fff;
	overflow-x: auto;
}

.chat-sidebar h3 {
	text-align: center;
}

.conversation-list {
	list-style: none;
	padding: 0;
	margin: 0;
}
.conversation-list li {
	padding: 10px;
	cursor: pointer;
	border-bottom: 1px solid rgba(--primary-color, #007bff);
}

/** Zone principale du chat */
.chat-main {
	flex: 1;
	display: flex;
	flex-direction: column;
	background-color: #f9f9f9;
}
.chat-header {
	background-color: var(--primary-color, #007bff);
	color: #fff;
	padding: 15px;
	text-align: center;
}

.chat-messages {
	flex: 1;
	padding: 15px;
	overflow-y: auto;
	background-color: linear-gradient(rgb(255, 255, 255), rgb(149, 240, 216));
}

.chat-message {
	margin-bottom: 10px;
	max-width: 70%;
	padding: 10px;
	border-radius: 8px;
	word-wrap: break-word;
}

.chat-message.sent {
	background-color: var(--primary-color, #007bff);
	color: #fff;
	align-self: flex-end;
}

.chat-message.received {
	background-color: #e9ecef;
	color: #333;
	align-self: flex-start;
}

.message-content {
	margin-bottom: 5px;
}

.message-time {
	font-size: 0.7rem;
	text-align: right;
	opacity: 0.7;
}

.chat-input {
	display: flex;
	padding: 10px;
	border-top: 1px solid #ddd;
	background-color: #fff;
}

.chat-input input {
	flex: 1;
	border: 1px solid #ddd;
	border-radius: 4px;
	padding: 10px;
	font-size: 1rem;
}
.send-button {
	background-color: var(--primary-color, #007bff);
	border: none;
	color: #fff;
	padding: 0 15px;
	margin-left: 10px;
	border-radius: 4px;
	display: flex;
	align-items: center;
	justify-content: center;
	cursor: pointer;
	transition: background-color 0.3s ease;
}

.send-button:hover {
	background-color: var(--secondary-color, #6c757d);
}

.send-button i {
	font-size: 1.2rem;
}
</style>
