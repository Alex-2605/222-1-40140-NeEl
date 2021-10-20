<template>
  <img alt="Vue logo" src="./assets/logouniva.png">
  <h3>Prueba NE: {{ mensaje }}</h3>
</template>

<script>
import axios from 'axios'

export default {
   name: 'App',
  data () {
    return {
      mensaje: 'Mensaje por default'
    }
  },
  methods: {
    getMensaje () {
      const path = 'http://localhost:5000/api/v1.0/mensaje'
      axios.get(path).then((respuesta) => {
        this.mensaje = respuesta.data
      })
      .catch((error) =>{
        console.error(error);
      })
    }
  },
  created (){
    this.getMensaje()
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
