<template>
  <div class="auth-container">
    <div class="form-wrapper">
      <h1>Enter verification code</h1>
      <p class="subtitle">A 6-digit code was printed to the console for {{ phoneNumber }}.</p>
      <form @submit.prevent="verifyOtp">
        <input type="text" v-model="otp" placeholder="6-digit code" required>
        <button type="submit">Verify</button>
      </form>
      <p v-if="error" class="error-message">{{ error }}</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'VerifyOtpView',
  props: ['phoneNumber'],
  data() {
    return {
      otp: '',
      error: ''
    };
  },
  methods: {
    async verifyOtp() {
      this.error = '';
      try {
        const response = await axios.post('/api/verify-otp/', {
          phone_number: this.phoneNumber,
          otp: this.otp
        });
        localStorage.setItem('token', response.data.access);
        this.$router.push('/welcome');
      } catch (e) {
        this.error = 'Invalid OTP. Please try again.';
        console.error(e);
      }
    }
  }
};
</script>

<style scoped>
.auth-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  text-align: center;
}
.form-wrapper {
  width: 100%;
  max-width: 400px;
  padding: 20px;
}
h1 {
  font-size: 36px;
  font-weight: 700;
  margin-bottom: 16px;
}
.subtitle {
  color: #a0a0a0; /* Lighter grey for dark background */
  margin-bottom: 40px;
}
input {
  width: 100%;
  padding: 14px 20px;
  border-radius: 8px;
  border: 1px solid #444;
  background-color: #2a2a2a;
  color: white;
  font-size: 16px;
  box-sizing: border-box;
  margin-bottom: 24px;
}
button {
  width: 100%;
  padding: 14px;
  border-radius: 8px;
  border: none;
  background-color: #f0c419; /* Vibrant yellow/gold */
  color: #1a1a1a; /* Dark text on yellow button */
  font-weight: 700;
  font-size: 16px;
  cursor: pointer;
}
.error-message {
  color: #ff5c5c;
  margin-top: 16px;
}
</style>
