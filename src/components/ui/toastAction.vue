<script setup lang="ts">
import { ToastAction as RadixToastAction} from 'radix-vue';
import { cn } from '../../../lib/utils';

interface ActionProps {
    class?: string;
    altText?: string;
}

const props = defineProps<ActionProps>();
</script>

<template>
    <RadixToastAction
        :alt-text="props.altText"
        :class="cn(
            'inline-flex h-8 shrink-0 items-center justify-center rounded-md border bg-transparent px-3 text-sm font-medium ring-offset-background transition-colors group-[.destructive]:border-muted/40 hover:bg-secondary group-[.destructive]:hover:border-destructive/30 group-[.destructive]:hover:bg-destructive group-[.destructive]:hover:text-destructive-foreground focus:outline-none focus:ring-2 focus:ring-ring focus:ring-offset-2 group-[.destructive]:focus:ring-destructive disabled:pointer-events-none disabled:opacity-50',
            props.class
        )"
    >
    <slot />
    </RadixToastAction>
</template>