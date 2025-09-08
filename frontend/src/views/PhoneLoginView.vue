<template>
  <div class="phone-login">
    <h2>Enter Phone Number</h2>
    <form @submit.prevent="generateOtp">
      <input type="text" v-model="phoneNumber" placeholder="Phone Number" required>
      <button type="submit">Get OTP</button>
    </form>
    <p v-if="error" style="color: red;">{{ error }}</p>
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
