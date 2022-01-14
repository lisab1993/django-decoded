<template>
  <div>
    <div>
      <a
        data-bs-toggle="collapse"
        href="#appNameCollapse"
        role="button"
        aria-expanded="false"
        aria-controls="appNameCollapse"
      >
        >app_name
      </a>

      <div class="collapse nested-one" id="appNameCollapse">
        <a
          data-bs-toggle="collapse"
          href="#migrationsCollapse"
          role="button"
          aria-expanded="false"
          aria-controls="migrationsCollapse"
        >
          >migrations
        </a>
        <div class="collapse nested-two" id="migrationsCollapse">
          <div>__pycache__</div>
          <div>__init__.py</div>
          <div>00001_initial.py</div>
          <div>00002_some_update.py</div>
        </div>
        <div>
          <a
            data-bs-toggle="collapse"
            href="#templatesCollapse"
            role="button"
            aria-expanded="false"
            aria-controls="templatesCollapse"
          >
            >templates
          </a>
        </div>
        <!-- <div class="collapse" id="templatesCollapse">index.html</div> -->
        <div class="collapse" id="templatesCollapse">
          <a
            class="nested-two"
            data-bs-toggle="collapse"
            href="#templatesAppCollapse"
            role="button"
            aria-expanded="false"
            aria-controls="templatesAppCollapse"
          >
            >appname
          </a>
        </div>
        
        <div class="collapse nested-three" id="templatesAppCollapse">
          <button class="hidden-button" @click="updateSelected('index.html')">index.html</button>
        </div>
        <div><button class="hidden-button" @click="updateSelected('__init__.py')">__init__.py</button></div>
        <div><button class="hidden-button" @click="updateSelected('admin.py')">admin.py</button></div>
        <div><button class="hidden-button" @click="updateSelected('apps.py')">apps.py</button></div>
        <div><button class="hidden-button" @click="updateSelected('models.py')">models.py</button></div>
        <div><button class="hidden-button" @click="updateSelected('tests.py')">tests.py</button></div>
        <div><button class="hidden-button" @click="updateSelected('urls.py')">urls.py</button></div>
        <div><button class="hidden-button" @click="updateSelected('views.py')">views.py</button></div>
      </div>
    </div>

    <a
      data-bs-toggle="collapse"
      href="#projectNameCollapse"
      role="button"
      aria-expanded="false"
      aria-controls="projectNameCollapse"
    >
      >proj_name
    </a>
    <div class="collapse nested-one" id="projectNameCollapse">
      <div>__init__.py</div>
      <div>asgi.py</div>
      <div>settings.py</div>
      <div>urls.py</div>
      <div>wsgi.py</div>
    </div>

    <div>Pipfile</div>
    <div>Pipfile.lock</div>
    <div>manage.py</div>
  </div>
</template>

<script>
export default {
  name: "Navbar",
  data() {
    return {
      selectedFile: "",
    };
  },
  methods: {
    updateSelected(event) {
      this.selectedFile = event
      this.$emit('clicked', event)
    }
  }
};
</script>

<style scoped>
a {
  text-decoration: none;
  color: black;
}

.nested-one {
  padding-left: 0.5rem;
}
.nested-two {
  padding-left: 1rem;
}
.nested-three {
  padding-left: 1.5rem;
}
.hidden-button {
  background-color: rgba(128, 128, 128, 0);
  border: none;
}
</style>