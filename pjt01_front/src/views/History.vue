<template>
  <div>
    <h2 class="text-left">
      Others Found ...
    </h2>
    <br>
    <p class="text-left" v-for="result in results" :key="result.id">
      <a style="color: #007bff;" class="trigger" @click="redirect(result.content)">{{ result.content }}</a>
      <pre>{{ result.created_at | moment("from", "now") }}</pre>
    </p>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  data() {
    return {
      results: [],
    }
  },
  methods: {
    redirect(res) {
      window.location.href="http://"+ res
    },
  },
  created() {
    axios ({
        method: 'GET',
        url: 'http://127.0.0.1:8000/shorten/history/show/',
      }).then((res)=>{
        console.log(res.data)
        this.results = res.data
      })
  }
}
</script>

<style>
  .trigger:hover {
    text-decoration: underline;
    cursor: pointer;
  }
</style>