<template>
  <div id="app-container">
    <SideBar v-if="loggedIn" :user="user" @logout="logout" />
    <router-view @login-success="handleLogin" @logout="logout"/>
  </div>
</template>

<script>
import axios from 'axios';
import SideBar from './components/SideBar.vue';

export default {
  name: 'App',
  components: {
    SideBar
  },
  data() {
    return {
      loggedIn: false,
      user: {}
    };
  },
  created() {
    this.checkLoginStatus();
  },
  methods: {
    checkLoginStatus() {
      const token = localStorage.getItem('token');
      if (token) {
        this.loggedIn = true;
        this.fetchUserDetails();
      }
    },
    async fetchUserDetails() {
      try {
        const token = localStorage.getItem('token');
        const response = await axios.get('/api/user/', {
          headers: {
            'Authorization': `Bearer ${token}`
          }
        });
        this.user = {
          fullName: response.data.full_name,
          phoneNumber: response.data.phone_number
        };
      } catch (error) {
        console.error('Failed to fetch user details', error);
        this.logout();
      }
    },
    handleLogin() {
      this.loggedIn = true;
      this.fetchUserDetails();
    },
    logout() {
      localStorage.removeItem('token');
      this.loggedIn = false;
      this.user = {};
      this.$router.push('/login');
    }
  }
};
</script>

<style>
#app-container {
  display: flex;
}
/* Global styles */
body {
  margin: 0;
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  background-color: #1a1a1a; /* Dark charcoal background */
  color: #ffffff; /* White text */
}
</style>
