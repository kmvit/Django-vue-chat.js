<template>
  <mu-container>
    <mu-appbar style="width: 100%;" color="primary">
      <mu-button icon slot="left">
        <mu-icon value="menu"></mu-icon>
      </mu-button>
      Чат на vue.js
      <mu-button flat slot="right" @click="gologin" v-if="!auth">LOGIN</mu-button>
      <mu-button flat slot="right" v-else="auth" @click="logout">LOGOUT</mu-button>
    </mu-appbar>
    <mu-row>
    </mu-row>
    <mu-row>
      <Room v-if="auth" @openDialog="openDialog"></Room>
      <Dialog v-if="dialog.show" :id="dialog.id"></Dialog>
    </mu-row>
  </mu-container>
</template>

<script>
  import Room from "./rooms/Room";
  import Dialog from "./rooms/Dialog";

  export default{
    name: "Home",
    components:{
      Room,
      Dialog,
    },
    data(){
      return{
        dialog:{
          'id':'',
          'show':false,

        }
      }
    },
    computed:{
      auth(){
        if (sessionStorage.getItem('auth_token')){
          return true
        }
      }
    },
    methods:{
      gologin(){
        this.$router.push({name:'login'})
      },
      logout(){
        sessionStorage.removeItem('auth_token')
        window.location = '/'
      },
      openDialog(id){
        this.dialog.id = id,
        this.dialog.show = true
      },
    },
  }
</script>

<style scoped>

</style>

