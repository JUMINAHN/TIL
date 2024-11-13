<template>
  <div>
    <header>
      <nav>
        <RouterLink :to="{ name: 'ArticleView' }">Article</RouterLink>
        <!-- <RouterLink :to="{ name: 'DetailView' }">Detail</RouterLink> : 각각의 게시글 안에 -->
      </nav>
    </header>
    <RouterView />
  </div>
</template>

<script setup>
import { RouterView, RouterLink } from 'vue-router'
</script>

<style scoped>
</style>
