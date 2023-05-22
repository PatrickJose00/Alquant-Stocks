<template>
  <div>
    <slot :data="data" :loading="loading" />
  </div>
</template>

<script setup>
import { ref, watch } from "vue";
import { defineProps } from "vue";

const props = defineProps({
  symbol: {
    type: String,
    required: true,
  },
});

const data = ref(null);
const loading = ref(false);

const fetchData = async () => {
  loading.value = true;
  const result = await fetch(
    `https://stock-server-3-stocks.herokuapp.com/stocks/${props.symbol}/statistics`
  );
  const response = await result.json();
  data.value = response.statistics;
  loading.value = false;
};

watch(
  () => props.symbol,
  () => {
    fetchData();
  }
);

fetchData();
</script>
