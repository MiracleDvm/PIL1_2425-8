<template>
  <div id="app">
    <Navbar v-if="$store.state.user" />
    <Chat v-if="$store.state.user" />
    <router-view />
    <Settings v-if="$store.state.user" />
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
};
</script>
