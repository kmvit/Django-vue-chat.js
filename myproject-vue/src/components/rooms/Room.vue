<template>
  <mu-col span="4" sm="4">
      <div v-for="room in rooms" class="room-list">
        <h3 @click="openDialog(room.id)">{{room.creater.username}}</h3>
        <small>{{room.date}}</small>
      </div>
  </mu-col>
  </div>
</template>

<script>
  export default {
    name: "Room",

    data() {
      return{
        rooms:'',

    }
    },
    created() {
      $.ajaxSetup({
        headers: {'Authorization': 'Token ' + sessionStorage.getItem('auth_token')},
      }),
      this.loadRoom()

    },
    methods: {
      loadRoom() {
        $.ajax({
          url:'http://127.0.0.1:8000/api/v1/chat/room/',
          type:"GET",
          success:(response) =>{
            this.rooms = response.data.data
          }
        })
      },
      openDialog(id){
        this.$emit("openDialog", id)
      }
    }
  }
</script>

<style scoped>
  h3{
    cursor: pointer;
  }
  .room-list{
    background: #e0cd46;
    color:#fff;
    margin: 20px 10px 5px 0 ;
    padding: 1px 0px 10px 0px;
    line-height: 0.5;
  }
</style>
