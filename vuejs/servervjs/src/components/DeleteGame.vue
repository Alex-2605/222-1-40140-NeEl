<template lang="html">
  <body>
    <div class="topnav">
      <a class="active" @click="home">Home</a>
      <a @click="newGame">New Game</a>
      <a @click="updateGame">Update Game</a>
      <a @click="deleteGame">Delete Game</a>
      <a @click="showAllGames">Show All Games</a>
    </div>
    <p class="databaseMessage">{{ databaseMessage }}</p>
    <input type="text" v-model="gameId" placeholder="Game ID" style="margin-bottom: 30px; margin-top: 60px;" class="inputField"><br>
    <button class="deleteButton" @click="deleteGameDatabase">Delete</button>  
  </body>
</template>

<script>
import axios from 'axios'

export default {
    name: 'DeleteGame',
    data () {
        return {
            gameId: '',
            databaseMessage: ''
        }
    },
    methods: {
      newGame () {
        this.$router.push('/new_game');
      },
      deleteGame () {
        this.$router.push('/delete_game');
      },
      showAllGames () {
        this.$router.push('/all_games');
      },
      updateGame () {
        this.$router.push('/update_game');
      },
      home () {
        this.$router.push('/');
      },
      deleteGameDatabase () {
        axios({
            method: 'DELETE',
            url: 'http://localhost:5000/api/delete_game/' + this.gameId
        }).then((success) => {
            if (success.data == 0) {
                this.databaseMessage = "An error ocurred and game could not be deleted";
            } else {
                this.databaseMessage = "The game was deleted from the database";
            }
        });
      }
    }
}
</script>

<style lang="css" scoped>
.topnav {
  overflow: hidden;
  background-color: #333;
}

.topnav a {
  float: left;
  color: #f2f2f2;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
  font-size: 17px;
  cursor: pointer;
}

.topnav area:hover {
  background-color: #ddd;
  color: black;
}

.topnav a.active {
  background-color: #04AA6D;
  color: white;
}

.deleteButton {
  background-color: #4CAF50;
  border: none;
  color: white;
  padding: 15px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  cursor: pointer;
}

.inputField {
  width: 260px;
  height: 40px;
  font-size: 20px;
}

.databaseMessage {
  font-weight: bold;
  font-size: 18px;
  color: yellow;
  text-align: center;
}
</style>