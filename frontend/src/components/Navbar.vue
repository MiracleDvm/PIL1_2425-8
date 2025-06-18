<template>
  <div class="nav">
    <div class="nav_div"> <div class="bar"></div> <div class="bar"></div> <div class="bar"></div> </div>
    <nav class="navbar">
      <router-link to="/home" class="nav-link">Accueil</router-link>
      <router-link to="/trips" class="nav-link">Trajets</router-link>
      <router-link to="/reservations" class="nav-link">Réservations</router-link>
      <router-link to="/chat" class="nav-link link">Messages</router-link>
      <router-link to="/notifications" class="nav-link">Notifications</router-link>
      <router-link to="/profile" class="nav-link">Profil</router-link>
    </nav>
  </div>
</template>

<style>
.navbar {
    display: flex;
    justify-content: space-around;
    background: var(--primary-color, #3498db);
    padding: 15px;
    border-radius: 8px;
}

.nav-link {
    color: white;
    text-decoration: none;
    font-weight: bold;
    transition: color 0.3s ease-in-out;

    margin: 7px;
    cursor: pointer;
}

.nav-link:hover {
    color: #ffd700;
}
  
/* */
.nav_div {
  top: 12px;
  left: 14px;
  min-width: 27px;
  border-radius: 4px;
  box-shadow: 0 0 4px 2px #68696b32;

  display: none;
  position: absolute;
  cursor: pointer;
}
.nav .bar {
  height: 5px;
  background-color: #3498db;
}

@media screen and (max-width: 476px) {
  .navbar {
    margin: 7px;
    padding: 10px;
    width: fit-content;
    background-color: #3498db70;
    /** */
    display: none;
    /** */
  }

  .nav_div {
    display: flex;
    flex-direction: column;
    gap: 2px;
  }

  .nav:hover {
    transition: all 1s ease-in-out;
  }
  .nav:hover .nav_div {
    display: none;
  }
  .nav:hover .navbar {
    display: flex;
    flex-direction: column;
    position: absolute;
  }
}
/** */

</style>
