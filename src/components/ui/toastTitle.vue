<script setup lang="ts">

import { ToastTitle as RadixToastTitle} from 'radix-vue';
import { cn } from '../../../lib/utils';


interface TitleProps {
    class?: string;
}

const props = defineProps<TitleProps>();
</script>

<template>
    <RadixToastTitle
        :class="cn('text-sm font-semibold', props.class)">
        <slot />
    </RadixToastTitle>
</template>