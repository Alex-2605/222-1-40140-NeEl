<template>
  <body>
    <div>
      <router-link to="/"></router-link>
    </div>
    <router-view/>
  </body>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
body {
  background: #2c3e50;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
