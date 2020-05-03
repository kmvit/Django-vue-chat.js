<template>
    <HomeSlot>
        <mu-row>
            <mu-col span="4" xl="2">
                <mu-button @click="addRoom">Создать комнату</mu-button>
                <div v-for="room in rooms" class="room-button">
                    <h3 @click="openDialog(room.id)">{{room.creater.username}}</h3>
                    <small>{{room.date}}</small>
                </div>
            </mu-col>
            <slot></slot>
        </mu-row>
    </HomeSlot>
</template>

<script>
    import HomeSlot from '../Home'
    export default {
        name: "Room",
        components: {
            HomeSlot,
        },
        data() {
            return {
                rooms: '',
            }
        },
        created() {
            $.ajaxSetup({
                headers: {'Authorization': "Token " + sessionStorage.getItem('auth_token')},
            });
            this.loadRoom()
        },
        methods: {
            // Загружаю список комнат
            loadRoom() {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/chat/room/",
                    type: "GET",
                    success: (response) => {
                        this.rooms = response.data.data
                    }
                })
            },
            openDialog(id) {
                // this.$emit("openDialog", id)
                this.$router.push({name: 'dialog', params: {id: id}})
            },
            // Создание комнаты
            addRoom() {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/chat/room/",
                    type: "POST",
                    success: (response) => {
                        this.loadRoom()
                    },
                    error: (response) => {
                        alert(response.statusText)
                    }
                })
            }
        }
    }
</script>

<style scoped>
    h3 {
        cursor: pointer;
    }
    .rooms-list {
        margin: 0 10px 0 0;
        box-shadow: 1px 4px 5px #848181;
    }
  .room-button {
        padding: 5px;
        /* color: #fff; */
        margin: 5px;
        background: #fdd835;
    }
</style>
