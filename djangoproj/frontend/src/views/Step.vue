<template>
  <div>
    <div class="container-fluid">
      <div class="row full-height">
        <div class="col-3 navigation-station"><Navbar></Navbar></div>
        <div class="col-9">
          <div class="row infopanel">
            <div class="col"><Infopanel></Infopanel></div>
          </div>
          <div class="row tutorialstarts"><div class="col"><Tutorialstarts></Tutorialstarts></div></div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { getAPI } from "../axios-api";
import Navbar from "../components/Navbar";
import Infopanel from "../components/Infopanel.vue";
import Tutorialstarts from "../components/Tutorialstarts.vue";



export default {
  name: "Step",
  data() {
    return {
      output: [],
    };
  },
  components: {
    Navbar,
    Infopanel,
    Tutorialstarts,
  },
  created() {
    getAPI
      .get("/step/")
      .then((response) => {
        console.log(response, 'data received');
        this.output = response.data;
      })
      .catch((err) => {
        console.log(err);
      });
  },
};
</script>

<style scoped>
.container-fluid {
  height: 100vh;
}

.full-height {
  height: 100vh;
}

.infopanel {
  height: 80vh;
}

.tutorialstarts {
    border-top: 1px solid black;
    height: 20vh;
}

.navigation-station {
    border-right: 1px solid black;
}
</style>