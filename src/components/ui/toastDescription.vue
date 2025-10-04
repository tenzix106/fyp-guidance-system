<script setup lang="ts">

import { ToastDescription as RadixToastDescription } from 'radix-vue';
import { cn } from '../../../lib/utils';

interface DescriptionProps {
    class?: string;
}

const props = defineProps<DescriptionProps>();
</script>

<template>
    <RadixToastDescription :class="cn('text-sm opacity-90', props.class)">
        <slot />
    </RadixToastDescription>
</template>