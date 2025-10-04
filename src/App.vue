<script setup lang="ts">

import { VueQueryPlugin, QueryClient } from '@tanstack/vue-query';
import { TooltipProvider } from '../src/components/ui/index.vue';
import Toaster from '../src/components/ui/toastViewport.vue';
import Sonner from '../src/components/ui/sonner.vue';

const queryClient = new QueryClient();
</script>

<template>
  <VueQueryPlugin :query-client="queryClient">
    <TooltipProvider>
      <Toaster>
      <Sonner>

        <router-view />
      </Sonner>
      </Toaster>
    </TooltipProvider>
  </VueQueryPlugin>
</template>

