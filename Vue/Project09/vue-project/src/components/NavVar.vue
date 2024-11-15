<template>
  <nav class="navbar navbar-expand-lg bg-dark-subtle">
    <div class="container-fluid">
      <a class="navbar-brand" href="#">MyTube</a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav">
          <li class="nav-item">
            <!--routerlink로 변경 예정-->
            <RouterLink :to="{name : 'home'}" class="nav-link active" aria-current="page">HOME</RouterLink> 
            <!-- <a class="nav-link active" aria-current="page" href="#">Home</a> -->
          </li>
          <li class="nav-item">
            <!--routerlink로 변경 예정-->
            <RouterLink :to="{name : 'search'}" class="nav-link active" aria-current="page">SEARCH</RouterLink>
            <!-- <a class="nav-link" href="#">Search</a> -->
          </li>
          <li class="nav-item">
            <RouterLink :to="{name : 'later'}" class="nav-link active" aria-current="page">LATER</RouterLink>
            <!--routerlink로 변경 예정-->
            <!-- <a class="nav-link" href="#">Later</a>/ -->
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script setup>
  import { RouterLink } from 'vue-router';
</script>

<style scoped>

</style>