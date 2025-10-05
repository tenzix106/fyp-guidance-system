<script setup lang="ts">
import { Label as RadixLabel } from 'radix-vue';
import { cva,  type VariantProps } from 'class-variance-authority';
import { cn } from '../../../lib/utils';

const labelVariants = cva(
    'text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70'
)

type LabelVariants = VariantProps<typeof labelVariants>;

interface LabelProps {
    class?: string;
    for?: string;
}

const props = defineProps<LabelProps>();
</script>

<template>
    <RadixLabel
        :for="props.for"
        :class="cn(labelVariants(), props.class)"
    >
        <slot/>
    </RadixLabel>
</template>