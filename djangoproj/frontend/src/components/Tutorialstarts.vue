<template>
  <div>
    <!-- {{steps}} -->
    <div>
      <!-- Button trigger modal -->
      <button
        type="button"
        class="btn btn-primary"
        data-bs-toggle="modal"
        data-bs-target="#beginnerModal"
      >
        Start Beginner Walkthrough
      </button>

      <!-- Modal -->
      <div
        class="modal fade"
        id="beginnerModal"
        tabindex="-1"
        aria-labelledby="beginnerModalLabel"
        aria-hidden="true"
      >
        <div class="modal-dialog">
          <div class="modal-content">
            <div class="modal-header">
              <h5 class="modal-title" id="beginnerModalLabel">Modal title</h5>
            </div>
            <div class="modal-body text-center">
              <!--                  Modal body starts above                -->
              <div
                id="carouselExampleDark"
                class="carousel carousel-dark slide"
                data-ride="carousel"
                data-interval="false"
              >
                <div class="carousel-inner">
                  <div
                    class="carousel-item"
                    v-for="(step, idx) in steps"
                    :key="step.id"
                    :class="{ active: idx == 0 }"
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
    <div>
      <!-- Button trigger modal -->
      <button
        type="button"
        class="btn btn-primary"
        data-bs-toggle="modal"
        data-bs-target="#advancedModal"
      >
        Start Advanced Walkthrough
      </button>

      <!-- Modal -->
      <div
        class="modal fade"
        id="advancedModal"
        tabindex="-1"
        aria-labelledby="advancedModalLabel"
        aria-hidden="true"
      >
        <div class="modal-dialog">
          <div class="modal-content">
            <div class="modal-header">
              <h5 class="modal-title" id="advancedModalLabel">Modal title</h5>
              <button
                type="button"
                class="btn-close"
                data-bs-dismiss="modal"
                aria-label="Close"
              ></button>
            </div>
            <div class="modal-body">


              <div class="form-check">
                <input
                  class="form-check-input"
                  type="checkbox"
                  value=""
                  id="checkboxItem"
                />
                <label class="form-check-label" for="checkboxItem">
                  Start Project
                </label>
              </div>


            </div>
            <div class="modal-footer">
              <button
                type="button"
                class="btn btn-secondary"
                data-bs-dismiss="modal"
              >
                Close
              </button>
              <button type="button" class="btn btn-primary">
                Save changes
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
.modal-dialog {
  max-width: 80vw !important;
}
.modal-body {
  padding: 0;
}

.carousel {
  height: 75vh;
  width: 80vw;
}
.carousel-inner {
  height: 75vh;
  width: 100%;
  padding-left: 3rem;
  padding-right: 3rem;
}
.carousel-item {
  height: 75vh;
  background-color: lightpink;
  border-left: 0.08rem solid black;
  border-right: 0.08rem solid black;
}

.carousel-control-prev {
  width: 3rem;
}

.carousel-control-next {
  width: 3rem;
}
</style>