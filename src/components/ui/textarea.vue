<script setup lang="ts">
import { cn } from '../../../lib/utils';

interface TextareaProps {
    class?: string;
    modelValue?: string;
    placeholder?: string;
    disabled?: boolean;
    required?: boolean;
    readonly?: boolean;
    id?: string;
    name?: string;
    rows?: number;
    cols?: number;
}

const props = defineProps<TextareaProps>();

const emit = defineEmits<{
    'update:modelValue' : [value: string];
    blur: [event : FocusEvent];
    focus: [event: FocusEvent];
    input: [evemt: Event];
}>();

const handleInput = (event: Event) => {
    const target = event.target as HTMLTextAreaElement;
    emit('update:modelValue', target.value);
    emit('input', event);
}
const handleBlur = (event: FocusEvent) => {
    emit('blur', event);
};

const handleFocus = (event: FocusEvent) => {
    emit('focus', event);
}
</script>

<template>
    <textarea
        :class="cn(
           'flex min-h-[80px] w-full rounded-md border border-input bg-background px-3 py-2 text-sm ring-offset-background placeholder:text-muted-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50',
            props.class
        )"
        :value="modelValue"
        :placeholder="placeholder"
        :disabled="disabled"
        :required="required"
        :readonly="readonly"
        :id="id"
        :name="name"
        :rows="rows"
        :cols="cols"
        @input="handleInput"
        @blur="handleBlur"
        @focus="handleFocus"
    />
</template>