<script setup lang="ts">
import { cn } from '../../../lib/utils';

interface InputProps {
    class?: string;
    type?: string;
    modelValue?: string | number;
    placeholder?: string;
    disabled?: boolean;
    required?: boolean;
    readonly?: boolean;
    id?: string;
    name?: string;
}

const props = withDefaults(defineProps<InputProps>(), {
    type: ' text',
})

const emit = defineEmits<{
    'update:modelValue': [value: string];
    blur: [event: FocusEvent];
    focus: [event: FocusEvent];
    input: [event: Event];
}>();

const handleInput = (event: Event) => {
    const target = event.target as HTMLInputElement;
    emit('update:modelValue', target.value);
    emit('input', event);
}

const handleBlur = (event: FocusEvent) => {
    emit('blur', event);
}

const handleFocus = (event: FocusEvent) => {
    emit('focus', event);
}
</script>

<template>
    <input
        :type="type"
        :class="cn(
            'flex h-10 w-full rounded-md border border-input bg-background px-3 py-2 text-base ring-offset-background file:border-0 file:bg-transparent file:text-sm file:font-medium file:text-foreground placeholder:text-muted-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50 md:text-sm',
            props.class
        )"
        :value="modelValue"
        :placeholder="placeholder"
        :disabled="disabled"
        :required="required"
        :readonly="readonly"
        :id="id"
        :name="name"
        @input="handleInput"
        @blur="handleBlur"
        @focus="handleFocus"
    />
</template>