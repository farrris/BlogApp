<template>
    <div v-if="show" class="modal-shadow" @click.self="closeModal">
        <div class="modal">
            <slot name="title">
                <h3 class="modal-title">Изменить статью</h3>
            </slot>
            <slot name="body">
                <div class="modal-content">
                    <form>
                        <div class='field-one'>Заголовок:</div>
                        <textarea v-model='article.title' cols="60" rows="1"></textarea>
                        <div class='field-two'>Текст:</div>
                        <textarea v-model='article.body' cols="60" rows="10"></textarea>
                    </form>
                </div>
            </slot>
            <slot name="footer">
                <div class="modal-footer">
                    <button class="button-close" @click="closeModal">
                        Отмена
                    </button>
                    <button class='button-update' @click="updateArticle">
                        Сохранить
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

        getDate() {
            let date = new Date();

            let dd = date.getDate();
            if (dd < 10) dd = '0' + dd;

            let mm = date.getMonth() + 1;
            if (mm < 10) mm = '0' + mm;

            let yy = date.getFullYear() % 100;
            if (yy < 10) yy = '0' + yy;

            let hours = date.getHours();
            if (hours < 10) hours = '0' + hours;

            let min = date.getMinutes();
            if (min < 10) min = '0' + min;

            let result = `${dd}.${mm}.${yy} ${hours}:${min}`;

            return result;
        },

        updateArticle() {
            let articleUpdate = {
                title: this.article.title,
                body: this.article.body,
                date: this.getDate()
            };
            axios.put('http://127.0.0.1:8000/api/articles/' + this.article.pk, articleUpdate).then(response => (console.log(response))).catch(error => (console.log(error)));
            this.closeModal();
            
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
    padding: 35px;
    position: absolute;
    top: 10%;
    left: 30%;
}

.modal-content {
    margin-right: 20%;
}

.modal-title {
    margin-bottom: 15%;
    text-align:center;
}

.field-two {
    margin-top:10%;
}

.field-one, .field-two {
    margin-bottom:3%;
}

.modal-footer {
    margin-top: 10%;
}

button {
    padding: 10px;
    background-color: white;
    font-weight: bold;
    border: 3px solid black;
    cursor: pointer;
}

.button-update {
    margin-left: 56%;
}
</style>
