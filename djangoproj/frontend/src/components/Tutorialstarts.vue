<template>
  <div>
    <!-- {{steps}} -->
    <div>
      <!-- Button trigger modal -->
      <button
        type="button"
        class="btn btn-primary"
        data-bs-toggle="modal"
        data-bs-target="#exampleModal"
      >
        Start Beginner Walkthrough
      </button>

      <!-- Modal -->
      <div
        class="modal fade"
        id="exampleModal"
        tabindex="-1"
        aria-labelledby="exampleModalLabel"
        aria-hidden="true"
      >
        <div class="modal-dialog">
          <div class="modal-content">
            <div class="modal-header">
              <h5 class="modal-title" id="exampleModalLabel">Modal title</h5>
            </div>
            <div class="modal-body text-center">
              <!--                  Modal body starts above                -->
              <div
                id="carouselExampleDark"
                class="carousel carousel-dark slide"
                data-bs-ride="carousel"
              >
                <div class="carousel-inner">
                  <div
                    class="carousel-item"
                    v-for="(step, idx) in steps"
                    :key="step.id"
                    :class="{ active: idx == 0 }"
                    data-bs-interval="2000"
                  >
                    <div>{{ step.name }}</div>
                    <div>{{ step.text }}</div>
                  </div>
                </div>
                <button
                  class="carousel-control-prev"
                  type="button"
                  data-bs-target="#carouselExampleDark"
                  data-bs-slide="prev"
                >
                  <span
                    class="carousel-control-prev-icon"
                    aria-hidden="true"
                  ></span>
                  <span class="visually-hidden">Previous</span>
                </button>
                <button
                  class="carousel-control-next"
                  type="button"
                  data-bs-target="#carouselExampleDark"
                  data-bs-slide="next"
                >
                  <span
                    class="carousel-control-next-icon"
                    aria-hidden="true"
                  ></span>
                  <span class="visually-hidden">Next</span>
                </button>
              </div>
              <!--          End of modal body below                -->
            </div>

            <div class="modal-footer">
              <button
                type="button"
                class="btn btn-secondary"
                data-bs-dismiss="modal"
              >
                Close
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { getAPI } from "../axios-api";

export default {
  name: "Tutorialstarts",
  data() {
    return {
      steps: [],
    };
  },
  created() {
    getAPI
      .get("/step/")
      .then((response) => {
        console.log(response, "got the steps in tutorialstarts");
        this.steps = response.data;
      })
      .catch((err) => {
        console.log(err);
      });
  },
};
</script>

<style scoped>
.modal {
  padding-right: 53vw;
}
.modal-body {
  padding: 0;
}
.modal-header {
  width: 80vw;
  justify-content: center;
}
.modal-title {
  margin: 0;
}

.modal-content {
  width: 80vw;
}
.modal-footer {
  width: 80vw;
}

.carousel {
  height: 75vh;
  width: 80vw;
}
.carousel-inner {
  height: 75vh;
}
.carousel-item {
  height: 75vh;
  width: 80vw;
  background-color: lightpink;
  padding-left: 3rem;
  padding-right: 3rem;
}

.carousel-control-prev {
  width: 3rem;
}

.carousel-control-next {
  width: 3rem;
}
</style>