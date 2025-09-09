<template>
  <div class="auth-container">
    <div class="form-container">
      <div class="form-wrapper">
        <div class="logo">VOYAGE</div>
        <h1>Log in or sign up</h1>
        <p class="subtitle">Enter your full name and phone number to receive a one-time passcode.</p>
        <form @submit.prevent="generateOtp">
          <div class="input-wrapper">
            <input type="text" v-model="fullName" placeholder="Your full name" required>
          </div>
          <div class="phone-input-wrapper">
            <span class="country-code">+91</span>
            <input type="text" v-model="phoneNumber" placeholder="Your 10-digit number" required>
          </div>
          <button type="submit">Continue</button>
        </form>
        <p v-if="error" class="error-message">{{ error }}</p>
      </div>
    </div>
    <div class="image-container">
      <!-- The background image is set in the CSS -->
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
      fullName: '',
      error: ''
    };
  },
  methods: {
    async generateOtp() {
      this.error = '';
      const fullPhoneNumber = `+91${this.phoneNumber}`;
      try {
        await axios.post('/api/generate-otp/', {
          phone_number: fullPhoneNumber,
          full_name: this.fullName
        });
        this.$router.push({ name: 'VerifyOtpView', params: { phoneNumber: fullPhoneNumber } });
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
  height: 100vh;
  width: 100%;
}
.form-container {
  flex: 1;
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
  padding: 40px;
}
.image-container {
  flex: 1;
  background-image: url('https://picsum.photos/seed/voyage/1200/900');
  background-size: cover;
  background-position: center;
}
.logo {
  font-size: 24px;
  font-weight: 800;
  letter-spacing: 4px;
  color: #f0c419; /* Vibrant yellow/gold */
  margin-bottom: 40px;
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
.input-wrapper, .phone-input-wrapper {
  border: 1px solid #444;
  border-radius: 8px;
  background-color: #2a2a2a;
  margin-bottom: 16px;
}
.phone-input-wrapper {
  display: flex;
  align-items: center;
}
.country-code {
  padding: 14px 0 14px 20px;
  color: #a0a0a0;
  font-size: 16px;
}
input {
  border: none;
  background: none;
  width: 100%;
  padding: 14px 20px 14px 10px;
  color: white;
  font-size: 16px;
  box-sizing: border-box;
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
