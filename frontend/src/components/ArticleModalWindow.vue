<template>
  <div v-if="show" class="modal-shadow" @click.self="closeModal">
      <div class="modal">
          <h3 class="title">
              Статья {{ article.pk }}. {{ article.title }}
          </h3>
          <div class="body">
              {{ article.body }}
          </div>
          <div class="footer">
            <button class="btn-close" @click="closeModal">
                Закрыть
            </button>
          </div>
      </div>
  </div>
</template>

<script>
export default {
    props: ['article'],
    data() {
        return {
            show: null,
        }
    },
    methods: {
        closeModal() {
            this.show = false;
        }
    },
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
    left: 30%;
    right: 30%;
}

.title {
    margin-bottom: 8%;
}

h3 {
    text-align:center;
}

button {
    margin-top: 8%;
    margin-left: 80%;
    padding: 10px;
    background-color: white;
    font-weight: bold;
    border: 3px solid black;
    cursor: pointer;
}
</style>