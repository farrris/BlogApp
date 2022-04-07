<template>
<div>
    <div v-for="article in articles" :key='article.pk'>
        <div @click="viewArticle(article)" class='article'>
            <div class='title'>Статья {{ article.pk }}.{{ article.title }}</div>
            <div class='date'>{{ article.date }}</div>
            <br>
            <div class='body'>{{ article.body.slice(0, 200) }}... 
                <a>Подробнее...</a>
            </div>
        </div>
            <button @click='updateArticleModalShow(article)' class='btn-edit'>Редактировать</button>
            <button @click='deleteArticleModalShow(article)' class='btn-delete'>Удалить</button>

        </div>
        <article-modal-window ref='modalViewArticle' :article='article' />
        <update-article-modal-window ref='modalUpdateArticle' :article='article' />
        <delete-article-modal-window ref='modalDeleteArticle' :article='article' />
</div>
</template>

<script>
import axios from "axios";
import UpdateNameModalWindow from './UpdateNameModalWindow.vue';
import ArticleModalWindow from './ArticleModalWindow.vue';
import UpdateArticleModalWindow from './UpdateArticleModalWindow.vue';
import DeleteArticleModalWindow from './DeleteArticleModalWindow.vue';
export default {
  components: { UpdateNameModalWindow, ArticleModalWindow, UpdateArticleModalWindow, DeleteArticleModalWindow },
    data() {
        return {
            articles: null,
            article: null,
        }
    },
    methods: {
        viewArticle(article) {
            this.$refs.modalViewArticle.show = true;
            this.article = article;
        },
        updateArticleModalShow(article) {
            this.$refs.modalUpdateArticle.show = true;
            this.article = article
        },
        deleteArticleModalShow(article) {
            this.$refs.modalDeleteArticle.show = true
            this.article = article
        }
    },
    mounted() {
        axios.get('http://127.0.0.1:8000/api/articles').then(response => (this.articles = response.data));
    },
}
</script>

<style scoped>
.article {
    border: 2px solid black;
    margin:5% 25% 0% 25%;
    padding:4% 4% 4% 4%;
    cursor: pointer;

}
.title {
    float:left;
}
.date {
    float:right;
    color: gray;
    margin-right:5%;
}

.body {
    margin: 4% 0% 0% 10%;
}
a {
    color:blue;
    font-size: 14px;
    margin-left:10px;
}

button {
    font-weight: bold;
    padding: 10px;
    background: none;
    border: 2px solid black;
    cursor: pointer;
}

button.btn-edit {
    margin: 2% 1% 0% 58.7%;
}



</style>