<script>
import axios from 'axios'
const URL = 'http://localhost:8000'
export default {
  methods: {
    getArticleList() {
      return axios.get(`${URL}/articles`).then(response => response.data);
    },
    createArticle(article) {
      return axios.post(`${URL}/articles`, article);
    },
    updateArticle(article, pk) {
      return axios.put(`${URL}/articles/${pk}`, article);
    },
    deleteArticle(pk) {
      return axios.delete(`${URL}/articles/${pk}`);
    }
  }
}
</script>