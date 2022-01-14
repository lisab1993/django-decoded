<template>
  <div>
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
                  <div class="carousel-item active" data-bs-interval="10000">
                    Lorem ipsum dolor sit amet consectetur, adipisicing elit.
                    Esse, non eaque vitae quasi ratione ut id quo hic quod quia
                    magni! Dolore id sed dicta esse cupiditate natus provident
                    repellendus? Lorem ipsum dolor sit amet consectetur
                    adipisicing elit. Nihil fugiat, velit, hic a, minus quis
                    facere repellendus voluptates adipisci voluptatibus neque
                    minima! Impedit quidem commodi, eius quod dolore doloremque
                    harum!
                  </div>
                  <div class="carousel-item" data-bs-interval="2000">
                    Lorem ipsum dolor sit amet consectetur adipisicing elit.
                    Numquam iusto, autem quidem consequatur rem voluptate sequi
                    odit exercitationem omnis modi, voluptatibus cumque minima
                    temporibus itaque recusandae a laboriosam dolores totam?
                    Lorem ipsum dolor sit amet consectetur, adipisicing elit.
                    Neque, nulla. Ullam, sunt atque est tempore magni, qui
                    ratione asperiores aliquid maxime sint molestiae
                    voluptatibus. Minus repudiandae ea magnam fuga tempora.
                  </div>
                  <div class="carousel-item">
                    Lorem ipsum dolor sit, amet consectetur adipisicing elit.
                    Reiciendis nemo labore velit ducimus quod. Ipsum et,
                    repellendus debitis ducimus magni, sequi possimus aspernatur
                    voluptatum rerum excepturi neque voluptatem sunt rem. Lorem
                    ipsum dolor sit amet consectetur adipisicing elit. Porro
                    perspiciatis laborum cum fuga, quae hic veritatis officiis
                    nihil possimus, consequatur ex, dolor quis fugiat saepe?
                    Deleniti consequuntur unde mollitia non!
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
export default {
  name: "Tutorialstarts",
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