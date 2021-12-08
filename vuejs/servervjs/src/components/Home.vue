<template lang="html">
  <body>
    <div class="topnav">
      <a class="active" @click="home">Home</a>
      <a @click="newGame">New Game</a>
      <a @click="updateGame">Update Game</a>
      <a @click="deleteGame">Delete Game</a>
      <a @click="showAllGames">Show All Games</a>
    </div>
    <img src="../images/super_mario_wallpaper.jpg" width="884" height="500">
  </body>
</template>

<script>
export default {
    name: 'Home',
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
</style>