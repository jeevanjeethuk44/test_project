<template>
  <div class="welcome-container">
    <div class="welcome-box">
      <h1>Welcome to the Club!</h1>
      <p>You have successfully logged in.</p>
      <button @click="logout">Logout</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'WelcomeView',
  methods: {
    logout() {
      localStorage.removeItem('token');
      this.$router.push('/login');
    }
  }
};
</script>

<style scoped>
.welcome-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  text-align: center;
}
.welcome-box {
  padding: 40px;
}
h1 {
  font-size: 48px;
  font-weight: 700;
  margin-bottom: 16px;
}
p {
  color: #a0a0a0;
  font-size: 18px;
}
button {
  margin-top: 32px;
  padding: 14px 28px;
  border-radius: 8px;
  border: none;
  background-color: #f0c419; /* Vibrant yellow/gold */
  color: #1a1a1a; /* Dark text on yellow button */
  font-weight: 700;
  font-size: 16px;
  cursor: pointer;
}
</style>
