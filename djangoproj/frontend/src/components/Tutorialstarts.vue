<template>
  <div class="main">
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
              <h5 class="modal-title text-center" id="advancedModalLabel">
                Detailed Walkthrough
              </h5>
              <button
                type="button"
                class="btn-close"
                data-bs-dismiss="modal"
                aria-label="Close"
              ></button>
            </div>
            <div class="modal-body">
              <div
                class="form-check"
                v-for="(step, index) in advancedSteps"
                :key="step.name"
              >
                <input
                  class="form-check-input"
                  type="checkbox"
                  value=""
                  :id="'checkboxItem' + index"
                />
                <label
                  class="form-check-label"
                  :for="'checkboxItem' + index"
                  data-bs-toggle="collapse"
                  :href="'#collapseCommand' + index"
                  role="button"
                  aria-expanded="flase"
                  aria-controls="'collapseCommand'+index"
                >
                  {{ step.name }}
                </label>
                <div class="collapse" :id="'collapseCommand' + index">
                  <div class="card card-body">{{ step.command }}</div>
                  <img :src="step.picture" />
                </div>
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
      advancedSteps: [
        {
          name: "create project directory",
          command: "Enter in terminal:",
          picture: require("../assets/detailed-walkthrough/mkdir-kittensproj.jpg"),
        },
        {
          name: "create virtual environment",
          command: "Enter in terminal:",
          picture: require("../assets/detailed-walkthrough/create-ve.jpg"),
        },
        {
          name: "install django into virtual environment",
          command: "Enter in terminal: ",
          picture: require("../assets/detailed-walkthrough/install-django.jpg"),
        },
        {
          name: "create project in current directory, don't forget the dot",
          command: "Enter in terminal (don't forget the dot!):",
          picture: require("../assets/detailed-walkthrough/create-django-project.jpg"),
        },
        {
          name: "create app",
          command: "Enter in terminal:",
          picture: require("../assets/detailed-walkthrough/startapp.jpg"),
        },
        {
          name: "view tree at this point",
          command: "Here's how your project should look at this point. Our django project (kittens_proj) and django app(catapp) are both inside the main project directory (also called kittens_proj, shown at the top of the image).",
          picture: require("../assets/detailed-walkthrough/tree-after-createapp.jpg")
        },
        {
          name: "add app to INSTALLED_APPS in settings.py",
          command:
            "click on settings.py and type in the app name at the end of the list", picture: require("../assets/detailed-walkthrough/add-installed-apps.jpg")
        },
        {
          name: "set timezone",
          command:
            "while in settings.py, scroll down to the TIME_ZONE and change it to your timezone.\n   PST: 'America/Los_Angeles',\n   MST: 'America/Denver',\n   CST: 'America/Chicago',\n   EST: 'America/New_York',\n   Alaska: 'America/Anchorage',\n   Hawaii: 'Pacific/Honolulu'",
        },
        {
          name: "adding html templates",
          command: "In your teminal, move into the app folder; create a directory called 'templates'; inside templates, create another directory with the same name as your app; your html files go inside that.", picture: require("../assets/detailed-walkthrough/create-templates.jpg"),
        },
        {
          name: "view tree at this point",
          command:
            "After your templates are set up, the tree should look like this:", picture: require("../assets/detailed-walkthrough/tree-after-templates.jpg"),
        },
        {
          name: "create a view",
          command: "In views.py, pass a string into the context object so we can render it on the template. We'll come back and add more later.",
          picture: require("../assets/detailed-walkthrough/index-view-starting.jpg"),
        },
        {
          name: "create a urls.py file in the app folder",
          command:
            "Enter in terminal", picture: require("../assets/detailed-walkthrough/create-urls-file.jpg"),
        },
        {
          name: "create a path in urls.py",
          command:
            "Give templates a way to speak to views.py", picture: require("../assets/detailed-walkthrough/write-url-route.jpg"),
        },
        {
          name: "add app urls to project urls",
          command: "Allow kittens_proj/urls.py to speak to catapp/urls.py ", picture: require("../assets/detailed-walkthrough/include-urls.jpg"),
        },
        {
          name: "display data on the template",
          command: "will add pic for this",
        },
        {
          name: "create database",
          command: "py manage.py makemigrations and then py manage.py migrate",
        },
        { name: "create a superuser", command: "py manage.py createsuperuser" },
        {
          name: "run the server",
          command: "py manage.py runserver",
        },
      ],
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
.main {
   white-space:pre-wrap;
}

.modal-dialog {
  max-width: 80vw !important;
}
.modal-body {
  padding: 0;
}

.carousel {
  height: 75vh;
  width: 79.9vw;
}
.carousel-inner {
  height: 75vh;
  width: 100%;
  padding-left: 3rem !important;
  padding-right: 3rem !important;
}
.carousel-item {
  height: 75vh;
  background-color: lightpink;
  min-width: 75vw !important;
}

.carousel-control-prev {
  width: 3rem;
}

.carousel-control-next {
  width: 3rem;
}

.slide {
  background-color: lightpink;
}
</style>