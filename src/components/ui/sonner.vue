<script setup lang="ts">

import { computed } from 'vue';
import { useColorMode } from '@vueuse/core';
import { Toaster } from 'vue-sonner';

interface ToasterProps {
    [key: string]: any;
}
const props = defineProps<ToasterProps>();
</script>