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
        >app_name (dir)
      </a>

      <div class="collapse" id="appNameCollapse">
        <a
          data-bs-toggle="collapse"
          href="#migrationsCollapse"
          role="button"
          aria-expanded="false"
          aria-controls="migrationsCollapse"
        >
          >migrations (dir)
        </a>
        <div class="collapse" id="migrationsCollapse">migrations listed here</div>
        <div>
        <a
          data-bs-toggle="collapse"
          href="#templatesCollapse"
          role="button"
          aria-expanded="false"
          aria-controls="templatesCollapse"
        >
          >templates/appname (dir)
        </a>
        </div>
        <div class="collapse" id="templatesCollapse">index.html</div>
        <div>__init__.py</div>
        <div>admin.py</div>
        <div>apps.py</div>
        <div>models.py</div>
        <div>tests.py</div>
        <div>urls.py</div>
        <div>views.py</div>
      </div>
    </div>

    <a
      data-bs-toggle="collapse"
      href="#projectNameCollapse"
      role="button"
      aria-expanded="false"
      aria-controls="projectNameCollapse"
    >
      >project_name(dir)
    </a>
    <div class="collapse" id="projectNameCollapse">
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
    return {};
  },
};
</script>

<style scoped>
a {
  text-decoration: none;
  color: black;
}

/* .collapse {
  background-color: hotpink;
} */
</style>