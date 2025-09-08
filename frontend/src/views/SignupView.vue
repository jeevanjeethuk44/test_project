<template>
  <div class="signup">
    <h2>Signup</h2>
    <form @submit.prevent="signup">
      <input type="text" v-model="username" placeholder="Username" required>
      <input type="password" v-model="password" placeholder="Password" required>
      <input type="password" v-model="passwordConfirm" placeholder="Confirm Password" required>
      <button type="submit">Signup</button>
    </form>
    <p v-if="error" style="color: red;">{{ error }}</p>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'SignupView',
  data() {
    return {
      username: '',
      password: '',
      passwordConfirm: '',
      error: ''
    };
  },
  methods: {
    async signup() {
      this.error = '';
      if (this.password !== this.passwordConfirm) {
        this.error = "Passwords do not match.";
        return;
      }
      try {
        await axios.post('/api/register/', {
          username: this.username,
          password: this.password
        });
        this.$router.push('/login');
      } catch (e) {
        this.error = 'An error occurred during signup.';
        console.error(e);
      }
    }
  }
};
</script>
