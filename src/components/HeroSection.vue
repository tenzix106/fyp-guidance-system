<script setup lang="ts">
import { Sparkles, BookOpen, Lightbulb } from 'lucide-vue-next';
</script>

<template>
    <header class="relative overflow-hidden bg-gradient-hero text-primary-foreground">
    <div class="absolute inset-0 bg-[url('data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjAiIGhlaWdodD0iNjAiIHZpZXdCb3g9IjAgMCA2MCA2MCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48ZyBmaWxsPSJub25lIiBmaWxsLXJ1bGU9ImV2ZW5vZGQiPjxnIGZpbGw9IiNmZmYiIGZpbGwtb3BhY2l0eT0iMC4xIj48cGF0aCBkPSJNMzYgMzRjMC0yLjIxIDEuNzktNCAzLjk5OC00SDQ0Yy0yLjIxIDAtNC0xLjc5LTQtNHYtNGMwIDIuMjEtMS43OSA0LTQgNGgtNGMwLTIuMjEtMS43OS00LTQtNHYtNGMyLjIxIDAgNCAxLjc5IDQgNGg0YzIuMjEgMCA0IDEuNzkgNCA0djRjMi4yMSAwIDQgMS43OSA0IDR2NGgtNGMtMi4yMSAwLTQgMS43OS00IDR6Ii8+PC9nPjwvZz48L3N2Zz4=')] opacity-20"></div>
    
    <div class="container relative mx-auto px-4 py-20 md:py-28">
      <div class="mx-auto max-w-4xl text-center animate-fade-in">
        <div class="mb-6 inline-flex items-center gap-2 rounded-full bg-background/10 px-4 py-2 backdrop-blur-sm">
          <Sparkles :size="16" />
          <span class="text-sm font-medium">AI-Powered Research Assistant</span>
        </div>
        
        <h1 class="mb-6 text-4xl font-bold tracking-tight md:text-6xl lg:text-7xl">
          Your Final Year Project
          <span class="block bg-gradient-to-r from-secondary to-accent bg-clip-text text-transparent">
            Starts Here
          </span>
        </h1>
        
        <p class="mx-auto mb-8 max-w-2xl text-lg text-primary-foreground/90 md:text-xl">
          Get personalized project ideas and intelligent resource recommendations tailored to your interests, skills, and academic goals.
        </p>
        
        <div class="flex flex-wrap justify-center gap-8 text-sm">
          <div class="flex items-center gap-2">
            <div class="rounded-full bg-background/20 p-2 backdrop-blur-sm">
              <Lightbulb :size="16" />
            </div>
            <span>AI-Generated Ideas</span>
          </div>
          <div class="flex items-center gap-2">
            <div class="rounded-full bg-background/20 p-2 backdrop-blur-sm">
              <BookOpen :size="16" />
            </div>
            <span>Curated Resources</span>
          </div>
          <div class="flex items-center gap-2">
            <div class="rounded-full bg-background/20 p-2 backdrop-blur-sm">
              <Sparkles :size="16" />
            </div>
            <span>Personalized Recommendations</span>
          </div>
        </div>
      </div>
    </div>
    
    <div class="absolute bottom-0 left-0 right-0 h-16 bg-gradient-to-t from-background to-transparent"></div>
  </header>
</template>