<template>
  <AuthLayout>
    <div class="form-content">
      <h1>Welcome back</h1>
      <p class="subtitle">Enter your phone number to receive a one-time passcode.</p>
      <form @submit.prevent="generateOtp">
        <label for="phone">Phone Number</label>
        <input id="phone" type="text" v-model="phoneNumber" placeholder="e.g., +14155552671" required>
        <button type="submit">Get OTP</button>
      </form>
      <p v-if="error" class="error-message">{{ error }}</p>
    </div>
  </AuthLayout>
</template>

<script>
import axios from 'axios';
import AuthLayout from '@/components/AuthLayout.vue';

export default {
  name: 'PhoneLoginView',
  components: {
    AuthLayout
  },
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
