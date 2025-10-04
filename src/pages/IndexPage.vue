<template>
  <div class="min-h-screen flex items-center justify-center">
    <div class="text-center px-6">
      <i class="pi pi-graduation-cap text-6xl text-primary mb-4"></i>
      <h1 class="text-4xl font-bold mb-3">Welcome to FYP Guidance System</h1>
      <p class="text-xl text-gray-600 mb-6">
        A comprehensive platform for managing your Final Year Project
      </p>
      <Button
        label="Get Started"
        icon="pi pi-arrow-right"
        @click="navigateToDashboard"
        class="p-button-lg"
      />
    </div>
  </div>
</template>

<script>
import { defineComponent } from 'vue'
import { useRouter } from 'vue-router'
import Button from 'primevue/button'

export default defineComponent({
  name: 'IndexPage',
  components: {
    Button
  },
  setup() {
    const router = useRouter()
    
    const navigateToDashboard = () => {
      router.push('/dashboard')
    }
    
    return {
      navigateToDashboard
    }
  }
})
</script>
