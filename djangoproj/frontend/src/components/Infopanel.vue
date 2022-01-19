<template>
  <div>
     {{ navbarSelected }} 

    <div v-for="page in filterPage" :key="page.id">
      {{page.content}}
      <br><br>
    </div>
  </div>
</template>

<script>
import { getAPI } from "../axios-api";

export default {
  name: "Infopanel",
  props: ["navbarSelected"],
  data() {
    return {
      pageData: "",
    };
  },
  created() {
    getAPI
      .get("/page/")
      .then((response) => {
        // console.log(response, 'data received');
        this.pageData = response.data;
      })
      .catch((err) => {
        console.log(err);
      });
  },
  computed: {
    filterPage() {
      let output = this.pageData.filter(obj => obj.title === this.navbarSelected)
      return output
    },
  },
};
</script>

<style scoped>
</style>