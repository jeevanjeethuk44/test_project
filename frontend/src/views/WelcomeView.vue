<template>
  <div class="page-container">
    <header>
      <h1>Explore Your Next Adventure</h1>
      <p>{{ welcomeMessage }}</p>
      <button @click="logout">Logout</button>
    </header>
    <main class="image-gallery">
      <div v-for="n in 6" :key="n" class="gallery-item">
        <img :src="`https://picsum.photos/seed/travel${n}/600/400`" alt="Random travel image">
      </div>
    </main>
  </div>
</template>

<script>
export default {
  name: 'WelcomeView',
  mounted() {
    this.$emit('login-success');
  },
  computed: {
    welcomeMessage() {
      const user = this.$root.user;
      if (user && user.fullName) {
        return `Welcome back, ${user.fullName}! Discover amazing destinations.`;
      }
      return 'Welcome back! Discover amazing destinations.';
    }
  },
  methods: {
    logout() {
      this.$emit('logout');
    }
  }
};
</script>

<style scoped>
.page-container {
  flex: 1;
  padding: 40px;
  text-align: center;
  overflow-y: auto;
}
header {
  margin-bottom: 60px;
}
h1 {
  font-size: 48px;
  font-weight: 700;
  margin-bottom: 16px;
}
p {
  color: #a0a0a0;
  font-size: 18px;
  max-width: 600px;
  margin: 0 auto 32px auto;
}
button {
  padding: 12px 24px;
  border-radius: 8px;
  border: none;
  background-color: #f0c419; /* Vibrant yellow/gold */
  color: #1a1a1a; /* Dark text on yellow button */
  font-weight: 700;
  font-size: 16px;
  cursor: pointer;
}
.image-gallery {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 20px;
  max-width: 1200px;
  margin: 0 auto;
}
.gallery-item img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  border-radius: 8px;
}
</style>
