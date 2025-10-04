<script setup lang="ts">

import { ToastClose as RadixToastClose} from 'radix-vue';
import { X } from 'lucide-vue-next';
import { cn } from '../../../lib/utils';

interface CloseProps {
    class?: string;
}

const props = defineProps<CloseProps>();

</script>

<template>
    <RadixToastClose
        :class="cn(
            'absolute right-2 top-2 rounded-md p-1 text-foreground/50 opacity-0 transition-opacity group-hover:opacity-100 group-[.destructive]:text-red-300 hover:text-foreground group-[.destructive]:hover:text-red-50 focus:opacity-100 focus:outline-none focus:ring-2 group-[.destructive]:focus:ring-red-400 group-[.destructive]:focus:ring-offset-red-600',
            props.class
        )"
    >
        <X: size="16"/>
    </RadixToastClose>
</template>