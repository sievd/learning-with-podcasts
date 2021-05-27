<template>
  <div id="login-wrapper">
    <div id="login">
      <section class="logo">
        <img src="@/assets/logo-white.png" @click="onLogoClicked" />
      </section>
      <section>
        <ul class="auth-options">
          <li>Sing Up</li>
          <li class="active">Login</li>
        </ul>
        <div class="inputs-container">
          <p>Log in with your username</p>
          <div class="input-item">
            <input
              type="text"
              placeholder="Username"
              v-model="username"
              required
            />
          </div>
          <div class="input-item">
            <input
              type="password"
              placeholder="Password"
              v-model="password"
              required
            />
          </div>
        </div>
        <div class="button-wrapper">
          <div class="button" @click="onSubmitButtonClicked">Submit</div>
        </div>
        <div class="forgot-password">
          <span>Forgot Password?</span>
        </div>
      </section>
    </div>
  </div>
</template>

<script>
export default {
  name: "Login",
  data() {
    return {
      username: "",
      password: "",
    };
  },
  methods: {
    async onSubmitButtonClicked() {
      const loginData = { username: this.username, password: this.password };
      const ok = await this.$auth.login(loginData);
      if (!ok) {
        alert("invalid username or password");
      } else {
        this.$router.push("/");
      }
    },
    onLogoClicked() {
      this.$router.push("/");
    },
  },
};
</script>

<style scoped>
#login-wrapper {
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  color: #cccccc;
  /* background-color: #448ecf; */
  position: fixed;
  top: 0;
  left: 0;
}

#login {
  background-color: white;
  border-radius: 8px;
  padding-top: 1em;
  box-shadow: 0 30px 60px 0 rgba(0, 0, 0, 0.3);
}

.inputs-container {
  padding-right: 2em;
  padding-left: 2em;
  margin: 0;
}

ul {
  display: flex;
  justify-content: center;
  gap: 2em;
}

p {
  font-size: 0.8em;
  color: #343a3c;
}

.active {
  border-bottom: 3px solid #448ecf;
  color: #0d0d0d;
}

#login,
.logo,
.inputs-container,
.button-wrapper {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.logo,
.auth-options {
  margin-bottom: 0.25em;
  color: #cccccc;
}

.auth-options {
  margin-top: 0.75em;
}

.auth-options > *:hover {
  cursor: pointer;
  opacity: 0.8;
}

.logo:hover {
  cursor: pointer;
}

input {
  color: #0d0d0d;
  border: 2px solid #f6f6f6;
  background-color: #f6f6f6;
  padding: 1rem;
  font-size: 1rem;
  box-shadow: none;
}

input[type="text"]:focus,
input[type="password"]:focus {
  background-color: #fff;
  border-bottom: 2px solid #5fbae9;
}

.input-item:last-child {
  margin-top: 0.5rem;
}

.button {
  background-color: #448ecf;
  font-size: 0.8em;
  color: white;
  padding: 0.5rem;
  margin-top: 1rem;
  text-align: center;
}

input,
.button {
  box-sizing: border-box;
  border-radius: 5px;
}

input {
  width: 20rem;
}

.button {
  width: 10rem;
}

.button:hover {
  cursor: pointer;
  opacity: 0.8;
}

img {
  width: 30%;
}

.forgot-password {
  background-color: #f6f6f6;
  border-top: 1px solid #dce8f1;
  padding: 1em 0;
  margin-top: 1em;
  text-align: center;
  -webkit-border-radius: 0 0 10px 10px;
  border-radius: 0 0 10px 10px;
  width: 100%;
  font-size: 0.75em;
  color: #448ecf;
}

.forgot-password > span:hover {
  cursor: pointer;
  opacity: 0.8;
}
</style>
