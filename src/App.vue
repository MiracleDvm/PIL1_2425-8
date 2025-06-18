<template>
  <div id="app">
    <Navbar v-if="$store.state.user" />
    <Chat v-if="$store.state.user" />
    <router-view />
    <Settings v-if="$store.state.user" />
  </div>
  <div id="startin">
    <img src="logo.png" alt="" height="100" width="100">
    <h1> Bienvenue dans l'assistant qui vous guidera dans exploration de notre application </h1>
    <router-link to="/" class="start_link" @click="start"> Commencer </router-link>
  </div>
</template>

<script>
import Navbar from './components/Navbar.vue';
import Settings from './components/Settings.vue';
import Chat from './components/Chat.vue';

export default {
  components: {
    Navbar,
    Settings,
    Chat,
  },
  /**/
  methods: {
    start() {
      const start = document.getElementById('startin');
      start.remove();
    }
  },
  /** */
};
</script>

<!---->
<style scoped>
  #startin {
    height: 100vh;
    max-width: 936px;
    margin: auto;
    padding: 54px;
    text-align: center;

    display: flex;
    flex-direction: column;
    gap: 124px;

    color: rgb(62, 68, 83);
    background: #def6f881;
    border-radius: 21px;
    overflow-x: hidden;
  }
  #startin img {
    margin: 0 auto;
  }

  .start_link {
    position: absolute;
    right: 64px;
    bottom: 64px;
    padding: 4px;
    width: fit-content;
    color: rgb(44, 122, 211);
  }
  .start_link:hover {
    text-decoration: none;
    color: rgb(48, 230, 181);
  }
</style>
<!---->
