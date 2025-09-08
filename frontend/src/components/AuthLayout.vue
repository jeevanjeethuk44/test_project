<template>
  <div class="auth-layout">
    <div class="form-column">
      <div class="logo">Untitled UI</div>
      <div class="form-container">
        <slot></slot>
      </div>
    </div>
    <div class="graphic-column">
      <!-- For simplicity, we use a solid color background instead of the 3D graphic -->
    </div>
  </div>
</template>

<script>
export default {
  name: 'AuthLayout'
};
</script>

<style scoped>
.auth-layout {
  display: flex;
  height: 100vh;
  width: 100vw;
  background-color: #f9fafb;
}

.form-column {
  flex: 0 0 520px; /* Fixed width for the form column */
  display: flex;
  flex-direction: column;
  padding: 40px;
  box-sizing: border-box;
}

.logo {
  font-weight: bold;
  font-size: 20px;
  margin-bottom: 80px;
}

.form-container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  flex-grow: 1;
  padding: 20px;
}

.graphic-column {
  flex-grow: 1;
  background-color: #5B10FF; /* Vibrant purple */
  border-top-left-radius: 30px;
  border-bottom-left-radius: 30px;
  margin: 16px 16px 16px 0;
}
</style>
