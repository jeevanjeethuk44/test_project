<template>
  <div class="welcome-container">
    <div class="welcome-box">
      <h1>Welcome!</h1>
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
  background-color: #f9fafb;
}
.welcome-box {
  text-align: center;
  padding: 40px;
  border-radius: 8px;
  background-color: white;
  box-shadow: 0 4px 6px rgba(0,0,0,0.1);
}
button {
  margin-top: 20px;
  padding: 10px 20px;
  border-radius: 8px;
  border: none;
  background-color: #4a00e0;
  color: white;
  font-weight: 500;
  cursor: pointer;
}
</style>
