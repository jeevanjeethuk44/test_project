<template>
  <div class="login">
    <h2>Login</h2>
    <form @submit.prevent="login">
      <input type="text" v-model="username" placeholder="Username" required>
      <input type="password" v-model="password" placeholder="Password" required>
      <button type="submit">Login</button>
    </form>
    <p v-if="error" style="color: red;">{{ error }}</p>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      username: '',
      password: '',
      error: ''
    };
  },
  methods: {
    async login() {
      this.error = '';
      try {
        const response = await axios.post('/api/token/', {
          username: this.username,
          password: this.password
        });
        localStorage.setItem('token', response.data.access);
        this.$router.push('/welcome');
      } catch (e) {
        this.error = 'Invalid credentials. Please try again.';
        console.error(e);
      }
    }
  }
};
</script>
