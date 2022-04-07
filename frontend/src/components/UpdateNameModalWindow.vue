<template>
  <div v-if="show" class="modal-shadow" @click.self="closeModal">
        <div class="modal">
            <slot name="title">
                <h3 class="modal-title">Изменить название блога</h3>
            </slot>
            <slot name="body">
                <div class="modal-content">
                    <form>
                        <input v-model="name" type="text">
                    </form>
                </div>
            </slot>
            <slot name="footer">
                <div class="modal-footer">
                    <button class="button-close" @click="closeModal">
                        Отмена
                    </button>
                    <button class='button-update' @click="updateName">
                        Изменить
                    </button>
                </div>
            </slot>
        </div>
    </div>
</template>

<script>
import axios from "axios";
export default {
    props: ['name'],
    data() {
        return {
            show: false,
        }
    },
    methods: {
        closeModal() {
            this.show = false
        },
        updateName() {
            let name = {
                value: this.name
            }
            axios.put('http://127.0.0.1:8000/api/name/1', name).then(response => (console.log(response))).catch(error => (console.log(error)));
            this.closeModal();
            location.reload();
        }
    }
}
</script>

<style scoped>
.modal-shadow {
    position: absolute;
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

.modal-title {
    margin-bottom: 15%;
}


.modal-footer {
    margin-top: 10%;
}

button {
    font-weight: bold;
    padding: 10px;
    background: none;
    border: 3px solid black;
    cursor: pointer;
}

.button-update {
    margin-left:29.8%;
}

input {
    width: 95%;
    padding: 2%;
    margin-bottom: 10%;
}
</style>