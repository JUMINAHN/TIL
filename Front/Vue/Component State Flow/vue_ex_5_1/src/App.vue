<template>
  <div>
    <h1>쇼핑 애플리케이션</h1>
    <ul>
      <!--근데 자식에게 전달해줄 것-->
      <!--product를 줄것임 어떻게? :my-prop에 담아서 -->
      <ProductList 
        v-for="product in products"
        :key="product.id" 
        :my-prop="product"
        /> <!--리스트로 만들 것 : proudct 자체가 만듬 -->
    </ul>
  </div>
</template>

<script setup>
import ProductList from '@/components/ProductList.vue';
import { ref } from 'vue'


let id = 0 //products를
const products = ref([ //이걸 ProudctList에서 전달받는다 
  { id: id++, name: '사과', price: 1000 },
  { id: id++, name: '바나나', price: 1500 },
  { id: id++, name: '딸기', price: 2000 },
  { id: id++, name: '포도', price: 3000 },
  { id: id++, name: '복숭아', price: 2000 },
  { id: id++, name: '수박', price: 5000 }
])
</script>

<!-- 
<style>

</style> -->