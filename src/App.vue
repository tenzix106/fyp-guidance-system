<script setup lang="ts">
import { TooltipProvider } from './components/ui/index.vue';
import Toaster from './components/ui/toastViewport.vue';
import Sonner from './components/ui/sonner.vue';
</script>

<template>
  <TooltipProvider>
    <Toaster>
      <Sonner>
        <router-view />
      </Sonner>
    </Toaster>
  </TooltipProvider>
</template>

