<template>
  <q-page class="flex flex-center">
    <div class="text-center">
      <q-icon name="error" size="4rem" color="negative" class="q-mb-md" />
      <div class="text-h4 q-mb-md">Oops! Nothing here...</div>
      <div class="text-subtitle1 q-mb-lg">404 - Page Not Found</div>
      <q-btn
        color="primary"
        label="Go Home"
        to="/"
        icon="home"
      />
    </div>
  </q-page>
</template>

<script>
import { defineComponent } from 'vue'

export default defineComponent({
  name: 'ErrorNotFound'
})
</script>
