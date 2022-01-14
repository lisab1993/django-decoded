<template>
  <div>
    <div>
      <button class="hidden-button" @click="updateSelected('app_name')">
        <a
          data-bs-toggle="collapse"
          href="#appNameCollapse"
          role="button"
          aria-expanded="false"
          aria-controls="appNameCollapse"
        >
          >app_name
        </a>
      </button>

      <div class="collapse nested-one" id="appNameCollapse">
        <button class="hidden-button" @click="updateSelected('migrations')">
          <a
            data-bs-toggle="collapse"
            href="#migrationsCollapse"
            role="button"
            aria-expanded="false"
            aria-controls="migrationsCollapse"
          >
            >migrations
          </a>
        </button>

        <div class="collapse nested-two" id="migrationsCollapse">
          <div>
            <button
              class="hidden-button"
              @click="updateSelected('__pycache__ (migrations)')"
            >
              __pycache__
            </button>
          </div>
          <div>
            <button
              class="hidden-button"
              @click="updateSelected('__init__.py (migrations)')"
            >
              __init__.py
            </button>
          </div>
          <div>
            <button
              class="hidden-button"
              @click="updateSelected('00001_initial.py')"
            >
              00001_initial.py
            </button>
          </div>
          <div>
            <button
              class="hidden-button"
              @click="updateSelected('00002_some_update.py')"
            >
              00002_some_update.py
            </button>
          </div>
        </div>
        <div>
          <button class="hidden-button" @click="updateSelected('templates')">
            <a
              data-bs-toggle="collapse"
              href="#templatesCollapse"
              role="button"
              aria-expanded="false"
              aria-controls="templatesCollapse"
            >
              >templates
            </a>
          </button>
        </div>
        <!-- <div class="collapse" id="templatesCollapse">index.html</div> -->
        <div class="collapse" id="templatesCollapse">
          <button class="hidden-button" @click="updateSelected('appname')">
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
          </button>
        </div>

        <div class="collapse nested-three" id="templatesAppCollapse">
          <button class="hidden-button" @click="updateSelected('index.html')">
            index.html
          </button>
        </div>
        <div>
          <button class="hidden-button" @click="updateSelected('__init__.py (app)')">
            __init__.py
          </button>
        </div>
        <div>
          <button class="hidden-button" @click="updateSelected('admin.py')">
            admin.py
          </button>
        </div>
        <div>
          <button class="hidden-button" @click="updateSelected('apps.py')">
            apps.py
          </button>
        </div>
        <div>
          <button class="hidden-button" @click="updateSelected('models.py')">
            models.py
          </button>
        </div>
        <div>
          <button class="hidden-button" @click="updateSelected('tests.py')">
            tests.py
          </button>
        </div>
        <div>
          <button class="hidden-button" @click="updateSelected('urls.py (app)')">
            urls.py
          </button>
        </div>
        <div>
          <button class="hidden-button" @click="updateSelected('views.py')">
            views.py
          </button>
        </div>
      </div>
    </div>

    <button class="hidden-button" @click="updateSelected('proj_name')">
      <a
        data-bs-toggle="collapse"
        href="#projectNameCollapse"
        role="button"
        aria-expanded="false"
        aria-controls="projectNameCollapse"
      >
        >proj_name
      </a>
    </button>

    <div class="collapse nested-one" id="projectNameCollapse">
      <div><button class="hidden-button" @click="updateSelected('__init__.py (proj)')">__init__.py</button></div>
      <div><button class="hidden-button" @click="updateSelected('asgi.py')">asgi.py</button></div>
      <div><button class="hidden-button" @click="updateSelected('settings.py')">settings.py</button></div>
      <div><button class="hidden-button" @click="updateSelected('urls.py (proj)')">urls.py</button></div>
      <div><button class="hidden-button" @click="updateSelected('wsgi.py')">wsgi.py</button></div>
    </div>

    <div><button class="hidden-button" @click="updateSelected('Pipfile')">Pipfile</button></div>
    <div><button class="hidden-button" @click="updateSelected('Pipfile.lock')">Pipfile.lock</button></div>
    <div><button class="hidden-button" @click="updateSelected('manage.py')">manage.py</button></div>
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
      this.selectedFile = event;
      this.$emit("clicked", event);
    },
  },
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