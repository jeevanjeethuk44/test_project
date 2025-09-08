<template>
  <AuthLayout>
    <div class="form-content">
      <h1>Enter code</h1>
      <p class="subtitle">We sent a code to the console for {{ phoneNumber }}.</p>
      <form @submit.prevent="verifyOtp">
        <label for="otp">OTP Code</label>
        <input id="otp" type="text" v-model="otp" placeholder="Enter your 6-digit code" required>
        <button type="submit">Verify & Login</button>
      </form>
      <p v-if="error" class="error-message">{{ error }}</p>
    </div>
  </AuthLayout>
</template>

<script>
import axios from 'axios';
import AuthLayout from '@/components/AuthLayout.vue';

export default {
  name: 'VerifyOtpView',
  components: {
    AuthLayout
  },
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
.form-content {
  width: 100%;
  max-width: 360px;
  text-align: left;
}

h1 {
  font-size: 32px; /* Slightly larger */
  font-weight: 700; /* Bolder */
  margin-bottom: 12px;
}

.subtitle {
  color: #667085;
  margin-bottom: 32px;
  font-size: 16px;
}

label {
  display: block;
  font-weight: 600; /* Slightly bolder */
  margin-bottom: 8px;
}

input {
  width: 100%;
  padding: 12px 14px; /* More padding */
  border-radius: 8px;
  border: 1px solid #d0d5dd;
  margin-bottom: 24px;
  font-size: 16px;
  box-sizing: border-box;
}

button {
  width: 100%;
  padding: 12px; /* More padding */
  border-radius: 8px;
  border: none;
  background-color: #5B10FF; /* New vibrant purple */
  color: white;
  font-weight: 600;
  font-size: 16px;
  cursor: pointer;
}

.error-message {
  color: #d92d20; /* A less harsh red */
  margin-top: 16px;
  text-align: center;
}
</style>
