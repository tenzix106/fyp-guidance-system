<template>
  <div id="app">
    <Toast />
    <ConfirmDialog />
    <router-view />
  </div>
</template>

<script>
import { defineComponent } from 'vue'
import Toast from 'primevue/toast'
import ConfirmDialog from 'primevue/confirmdialog'

export default defineComponent({
  name: 'App',
  components: {
    Toast,
    ConfirmDialog
  }
})
</script>

<style>
#app {
  min-height: 100vh;
}
</style>