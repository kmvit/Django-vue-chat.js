<template>
  <mu-col span="8">
    <mu-container class="dialog">
      <div v-for="dialog in dialogs"
              direction="column"
              justify-content="start"
              align-items="end">
      <p><strong>{{dialog.user.username}}</strong></p>
      <p>{{dialog.text}}</p>
      <span>{{dialog.date}}</span>
    </div>
    </mu-container>
    <mu-row>
      <mu-container>
        <mu-row>
          <mu-text-field
            v-model="form.textarea"
            placeholder="Введите текст"
            multi-line :rows="2"
            full-width></mu-text-field><br/>
          <mu-button round color="success">Добавить</mu-button>
          </mu-row>
      </mu-container>
    </mu-row>
  </mu-col>
</template>

<script>
  export default {
		name: "Dialog",
    props:{
		  id:'',
    },
    data(){
		  return{
		    dialogs:'',
        form:{
		      textarea:'',
        },
      }
    },
    created() {
      $.ajaxSetup({
        headers: {'Authorization': 'Token ' + sessionStorage.getItem('auth_token')},
      });
      this.loadDialog()

    },
    methods:{
		  loadDialog(){
		    $.ajax({
          url:'http://127.0.0.1:8000/api/v1/chat/dialog/',
          type:"GET",
          data:{
            room:this.id
          },
          success:(response) =>{
            this.dialogs = response.data.data
          }
        })
      }
    }
	}
</script>

<style scoped>
 .dialog{
   border:1px solid #ccc;
   margin-top: 20px;
 }
</style>
