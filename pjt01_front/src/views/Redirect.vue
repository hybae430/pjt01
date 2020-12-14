<template>
  <div>
      페이지 연결중 ...
  </div>
</template>

<script>
import axios from 'axios'
export default {
    created() {
        var encode = this.$route.params.redirect;
        axios ({
        method: 'GET',
        url: 'http://127.0.0.1:8000/'+ encode,
        data: {
          url: encode,
        }
      }).then((res)=>{
        console.log(res.data)
        window.location.href="http://"+res.data
      })
    }
}
</script>

<style>

</style>