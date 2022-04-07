<template>
<div>
  <h1 @click=showModalUpdateName>{{ name }}</h1>

  <button class='createArticle' @click="showModalCreateArticle">Добавить статью</button>

  <create-article-modal-window ref="modalCreateArticle"></create-article-modal-window>
  <update-name-modal-window ref='modalUpdateName' :name='name'></update-name-modal-window>
</div>
</template>

<script>
import axios from "axios";
import CreateArticleModalWindow from './CreateArticleModalWindow.vue';
import UpdateNameModalWindow from './UpdateNameModalWindow.vue';
export default {
  components: { 
    CreateArticleModalWindow,
    UpdateNameModalWindow 
  },
  methods: {
    showModalCreateArticle() {
      this.$refs.modalCreateArticle.show = true
    },
    showModalUpdateName() {
      this.$refs.modalUpdateName.show = true
    }
        },
  data() {
    return {
      name: null
    }
  },
  mounted() {
    axios.get('http://127.0.0.1:8000/api/name/1').then(response => (this.name = response.data.value));
  }

}
</script>

<style scoped>
  h1 {
    margin-left:22%;
    cursor: pointer;  
  }
  button.createArticle {
    position:absolute;
    left:70%;
    padding: 10px;
    background-color: white;
    font-weight: bold;
    border: 3px solid black;
    cursor: pointer;
  }
  button.name {
    margin-left:2%;
    padding: 3px;
    background-color: white;
    font-weight: bold;
    border: 2px solid black;
    cursor: pointer;
  }
  h1, button {
    display: inline-block;
    margin-top: 2%;
  }
</style>