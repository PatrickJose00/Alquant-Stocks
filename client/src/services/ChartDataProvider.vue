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
  const result = await fetch(`http://localhost:8000/stocks/${props.symbol}`);
  const response = await result.json();
  data.value = response.data.map((item) => ({
    timestamp: item.timestamp,
    value: item.value,
  }));
  loading.value = false;
};

watch(
  () => props.symbol,
  () => {
    fetchData();
  }
);

fetchData();

setInterval(fetchData, 60000);
</script>
