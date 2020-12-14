<template>
  <div class="container">
    <h1 class="text-left">Shorten Your URL!</h1>
    <div class="row">
      <div class="col-md-7">
        <form @submit="sendurl" class="d-flex">
          <input class="form-control" type="text" placeholder="Type url that you want to shorten!" aria-label="Search" v-model="original">
          <button class="btn btn-outline-success" type="submit"><i class="fas fa-exchange-alt"></i></button>
        </form>
        <br v-show="result">
        <p v-show="result" class="text-left">Shortened URL: <router-link :to="{ name: 'Redirect', params: { redirect: result } }" >http://localhost:8080/{{ result }}</router-link></p>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  data() {
    return {
      original: '',
      edit: '',
      result: '',
    }
  },
  methods: {
    sendurl(event) {
      event.preventDefault()
      this.edit = this.original
      if (this.edit.indexOf("https://") !== -1) {
        this.original = this.original.replace('https://', 'dbslh')
        this.edit = this.edit.replace('https://', '')
      } else if (this.edit.indexOf("http://") !== -1) {
        this.original = this.original.replace('http://', 'dbslh')
        this.edit = this.edit.replace('http://', '')
      }
      if (this.edit.indexOf("www.") !== -1) {
        this.edit = this.edit.replace('www.', '')
      }
      while (this.original.indexOf('?') !== -1) {
        this.original = this.original.replace('?', 'quesm')
        this.edit = this.edit.replace('?', 'quesm')
      }
      while (this.original.indexOf('%') !== -1) {
        this.original = this.original.replace('%', 'pcent')
        this.edit = this.edit.replace('%', 'pcent')
      }
      while (this.edit.indexOf('/') !== -1) {
        this.original = this.original.replace('/', 'slh')
        this.edit = this.edit.replace('/', '')
      }
      axios ({
        method: 'GET',
        url: 'http://127.0.0.1:8000/'+ this.edit +'/' + this.original,
        data: {
          url: this.edit,
          
        }
      }).then((res)=>{
        console.log(res.data)
        this.result = res.data
        this.original = ''
      })
    }
  }
};
</script>

<style scoped>
  .no-padding {
    padding: 0;
    margin: 0;
  }
</style>