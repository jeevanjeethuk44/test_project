<template>
  <div class="auth-container">
    <div class="form-wrapper">
      <h1>Log in or sign up</h1>
      <p class="subtitle">Enter your phone number to receive a one-time passcode.</p>
      <form @submit.prevent="generateOtp">
        <input type="text" v-model="phoneNumber" placeholder="Phone Number" required>
        <button type="submit">Continue</button>
      </form>
      <p v-if="error" class="error-message">{{ error }}</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'PhoneLoginView',
  data() {
    return {
      phoneNumber: '',
      error: ''
    };
  },
  methods: {
    async generateOtp() {
      this.error = '';
      try {
        await axios.post('/api/generate-otp/', {
          phone_number: this.phoneNumber
        });
        this.$router.push({ name: 'VerifyOtpView', params: { phoneNumber: this.phoneNumber } });
      } catch (e) {
        this.error = 'Failed to send OTP. Please try again.';
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
