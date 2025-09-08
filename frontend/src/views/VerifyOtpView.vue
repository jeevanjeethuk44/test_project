<template>
  <div class="verify-otp">
    <h2>Enter OTP</h2>
    <p>An OTP should have been printed to the Django console for {{ phoneNumber }}</p>
    <form @submit.prevent="verifyOtp">
      <input type="text" v-model="otp" placeholder="OTP" required>
      <button type="submit">Verify & Login</button>
    </form>
    <p v-if="error" style="color: red;">{{ error }}</p>
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
