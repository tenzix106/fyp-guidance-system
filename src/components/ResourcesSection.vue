<script setup lang="ts">
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from './ui/index.vue';
import { Badge } from './ui/index.vue';
import { Button } from './ui/index.vue';
import { BookOpen, ExternalLink, Database, Wrench, FileText } from 'lucide-vue-next';
import { Resource } from '../../pages/Index.vue';

interface ResourcesSectionProps {
    resources: Resource[];
}

const props = defineProps<ResourcesSectionProps>();

const getResourceIcon = (type: string) => {
    switch (type) {
        case 'paper':
            return FileText;
        case 'tool':
            return Wrench;
        case 'dataset':
            return Database;
        case 'methodology':
            return BookOpen;
        default:
            return FileText;
    }
}

const getIconColor = (type: string): string => {
    switch (type) {
        case 'paper':
            return 'text-primary';
        case 'tool':
            return 'text-accent';
        case 'dataset':
            return 'text-secondary';
        case 'methodology':
            return 'text-muted-foreground';
        default:
            return 'text-muted-foreground';
    }
}

const getTypeColor = (type: string): string => {
    switch (type) {
    case 'paper':
      return 'bg-primary/10 text-primary border-primary/20';
    case 'tool':
      return 'bg-accent/10 text-accent border-accent/20';
    case 'dataset':
      return 'bg-secondary/10 text-secondary border-secondary/20';
    case 'methodology':
      return 'bg-muted text-muted-foreground border-muted';
    default:
      return 'bg-muted';
  }
}

const openResource = (url: string) => {
    window.open(url, '_blank');
}
</script>

<template>
    <section class="animate-fade-in">
      <div class="mb-8 text-center">
        <h2 class="mb-3 flex items-center justify-center gap-2 text-3xl font-bold">
          <BookOpen :size="32" class="text-primary" />
          Recommended Resources
        </h2>
        <p class="text-muted-foreground">
          Curated materials to help you succeed
        </p>
      </div>
  
      <div class="grid gap-4 md:grid-cols-2 lg:grid-cols-3">
        <Card
          v-for="(resource, index) in resources"
          :key="resource.id"
          class="group flex flex-col overflow-hidden transition-all hover:shadow-md animate-scale-in"
          :style="{ animationDelay: `${index * 75}ms` }"
        >
          <CardHeader class="pb-3">
            <div class="mb-2 flex items-center justify-between">
              <component :is="getResourceIcon(resource.type)" :size="20" :class="getIconColor(resource.type)" />
              <Badge :class="getTypeColor(resource.type)">
                {{ resource.type }}
              </Badge>
            </div>
            <CardTitle class="line-clamp-2 text-base">
              {{ resource.title }}
            </CardTitle>
          </CardHeader>
          
          <CardContent class="flex flex-1 flex-col">
            <CardDescription class="mb-4 flex-1 text-sm line-clamp-3">
              {{ resource.description }}
            </CardDescription>
  
            <div class="mt-auto flex items-center justify-between">
              <div class="flex items-center gap-1 text-xs text-muted-foreground">
                <span>Relevance:</span>
                <div class="flex gap-1">
                  <div
                    v-for="i in 5"
                    :key="i"
                    :class="[
                      'h-1.5 w-1.5 rounded-full',
                      i <= Math.round(resource.relevance * 5) ? 'bg-accent' : 'bg-muted'
                    ]"
                  />
                </div>
              </div>
  
              <Button
                variant="ghost"
                size="sm"
                class="h-8 gap-1 text-xs hover:text-primary"
                @click="openResource(resource.url)"
              >
                View
                <ExternalLink :size="12" />
              </Button>
            </div>
          </CardContent>
        </Card>
      </div>
    </section>
  </template>