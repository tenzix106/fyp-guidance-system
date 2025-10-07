<script setup lang="ts">
import { Toaster } from 'vue-sonner';

interface ToasterProps {
    [key: string]: any;
}
const props = defineProps<ToasterProps>();
</script>

<template>
  <Toaster v-bind="props" />
</template>