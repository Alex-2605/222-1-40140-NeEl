<template lang="html">
  <div class="">
    <p> {{ mensaje }}  </p>
  </div>
</template>

<script>
export default {
    name: 'Main',
    data () {
        return{
            mensaje: 'Nuevo mensaje desde  Vue JS'
        }
    }
}
</script>

<style lang="css" scoped>
</style>