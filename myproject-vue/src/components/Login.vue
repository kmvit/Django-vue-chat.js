<template>
  <mu-container>
    <mu-form class="mu-demo-form">
      <mu-form-item  label="username" help-text="Введите имя пользователя" prop="Имя пользователя" :rules="usernameRules">
        <mu-text-field v-model="username" prop="username"></mu-text-field>
      </mu-form-item>
      <mu-form-item label="password" prop="password" :rules="passwordRules">
          <mu-text-field type="password" v-model="password" prop="Пароль"></mu-text-field>
      </mu-form-item>
      <mu-form-item>
        <mu-button color="primary" @click="setLogin">Войти</mu-button>
      </mu-form-item>
    </mu-form>
  </mu-container>
</template>

<style>
.mu-demo-form {
  width: 100%;
  max-width: 460px;
}
</style>

<script>
    export default {
        name: "Login",
        data() {
          return {
            username: '',
            password: '',
            usernameRules: [
              { validate: (val) => !!val, message: 'Username must be filled in'},
              { validate: (val) => val.length >= 3, message: 'Username length greater than 3'}
            ],
            passwordRules: [
              { validate: (val) => !!val, message: 'Password must be filled in'},
              { validate: (val) => val.length >= 3 && val.length <= 20, message: 'Password length must be greater than 3 and less than 10'}
            ],
          }
        },
        methods: {
            setLogin() {
                $.ajax({
                    url: "http://127.0.0.1:8000/auth/token/login/",
                    type: "POST",
                    data: {
                        username: this.username,
                        password: this.password,
                    },
                    success: (response) => {
                        alert("Спасибо что Вы с нами")
                        sessionStorage.setItem("auth_token", response.data.attributes.auth_token)
                        this.$router.push({name: "home"})
                    },
                    error: (response) => {
                        if (response.status === 400) {
                            alert("Логин или пароль не верен")
                        }
                    }
                })
            },
        }
    }
</script>
