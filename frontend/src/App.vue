<template>
<div id='app'>
  <Header/>
  <ArticleList/>
</div>
</template>

<script>
import Header from '@/components/Header.vue'
import ArticleList from '@/components/ArticleList.vue'
export default {
  components: {
    Header,
    ArticleList
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}
</style>
