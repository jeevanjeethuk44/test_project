<template>
  <div class="sidebar">
    <div class="profile">
      <div class="profile-icon">
        <img src="https://via.placeholder.com/50" alt="Profile Icon">
      </div>
      <div class="profile-info">
        <h3>{{ user.fullName }}</h3>
        <p>{{ user.phoneNumber }}</p>
      </div>
    </div>
    <nav>
      <ul>
        <li><a href="#">Home</a></li>
        <li><a href="#">About</a></li>
        <li><a href="#">Contact</a></li>
      </ul>
    </nav>
    <button @click="logout">Logout</button>
  </div>
</template>

<script>
export default {
  name: 'SideBar',
  props: {
    user: {
      type: Object,
      required: true,
      default: () => ({ fullName: '', phoneNumber: '' })
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
.sidebar {
  width: 250px;
  background-color: #1a1a1a;
  color: #f0c419;
  display: flex;
  flex-direction: column;
  padding: 20px;
}
.profile {
  display: flex;
  align-items: center;
  margin-bottom: 30px;
}
.profile-icon img {
  width: 50px;
  height: 50px;
  border-radius: 50%;
  margin-right: 15px;
}
.profile-info h3 {
  margin: 0;
  font-size: 18px;
}
.profile-info p {
  margin: 0;
  font-size: 14px;
  color: #a0a0a0;
}
nav ul {
  list-style: none;
  padding: 0;
  margin: 0;
}
nav li {
  margin-bottom: 10px;
}
nav a {
  color: #f0c419;
  text-decoration: none;
  font-size: 16px;
}
button {
  margin-top: auto;
  padding: 12px;
  border-radius: 8px;
  border: none;
  background-color: #f0c419; /* Vibrant yellow/gold */
  color: #1a1a1a; /* Dark text on yellow button */
  font-weight: 700;
  font-size: 16px;
  cursor: pointer;
}
</style>
