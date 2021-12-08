<template lang="html">
  <body>
    <div class="topnav">
      <a class="active" @click="home">Home</a>
      <a @click="newGame">New Game</a>
      <a @click="updateGame">Update Game</a>
      <a @click="deleteGame">Delete Game</a>
      <a @click="showAllGames">Show All Games</a>
    </div>
    <table id="games" style="margin-top: 50px;">
        <thead>
            <tr>
                <th>Game ID</th>
                <th>Game Name</th>
                <th>Game Genre</th>
                <th>Game Classification</th>
                <th>Game Platform</th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="game in gamesInfo" :key="game.id">
                <td>{{ game.id }}</td>
                <td>{{ game.name }}</td>
                <td>{{ game.genre }}</td>
                <td>{{ game.classification }}</td>
                <td>{{ game.platform }}</td>
            </tr>
        </tbody>
    </table>
  </body>
</template>

<script>
import axios from 'axios'

export default {
    name: 'AllGames',
    data () {
        return {
            gamesInfo: []
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
          console.log("print games info");
          console.log(this.gamesInfo);
        this.$router.push('/');
      }
    },
    mounted () {
        axios({
            method: 'GET',
            url: 'http://localhost:5000/api/games/'
        }).then((success) => {
            this.gamesInfo = success.data;
        });
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

#games {
  font-family: Arial, Helvetica, sans-serif;
  border-collapse: collapse;
  width: 100%;
  background-color: #FFF;
}

#games td, #games th {
  border: 1px solid #ddd;
  padding: 8px;
}

#games tr:nth-child(even){background: #f2f2f2;}

#games tr:hover {background: #ddd;}

#games th {
  padding-top: 12px;
  padding-bottom: 12px;
  text-align: left;
  background: #04AA6D;
  color: white;
}
</style>