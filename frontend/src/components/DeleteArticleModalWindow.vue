<template>
    <div v-if="show" class="modal-shadow" @click.self="closeModal">
        <div class="modal">
            <slot name="title">
                <h3 class="modal-title">Вы точно хотите удалить статью?</h3>
            </slot>
            <slot name="footer">
                <div class="modal-footer">
                    <button class="button-close" @click="closeModal">
                        Отмена
                    </button>
                    <button class='button-delete' @click="deleteArticle">
                        Подтвердить
                    </button>
                </div>
            </slot>
        </div>
    </div>
</template>
 
<script>
import axios from "axios"
export default {
    props: ['article'],
    data() {
        return {
            show: false,
        }
    },
    methods: {
        closeModal() {
            this.show = false
        },

        deleteArticle() {
            axios.delete('http://127.0.0.1:8000/api/articles/' + this.article.pk).then(response => (console.log(response))).catch(error => (console.log(error)));
            this.closeModal();
            location.reload();
            
        }
    }
}
</script>
 
<style scoped>
.modal-shadow {
    position: fixed;
    top: 0;
    left: 0;
    min-height: 100%;
    width: 100%;
    background: rgba(0, 0, 0, 0.39);
  }
.modal {
    background: #fff;
    border-radius: 8px;
    padding: 40px;
    position: absolute;
    top: 20%;
    left: 40%;
}

button {
    margin-top: 10%;
    padding: 10px;
    background-color: white;
    font-weight: bold;
    border: 3px solid black;
    cursor: pointer;
}

.button-delete {
    margin-left: 40%;
}
</style>
