<script setup lang="ts">
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from './ui/index.vue';
import { Badge } from './ui/index.vue';
import { Lightbulb, TrendingUp, Code, Award  } from 'lucide-vue-next';
import { ProjectIdea } from '../../pages/Index.vue';

interface ProjectIdeasSectionProps {
    ideas: ProjectIdea[];
}

const props = defineProps<ProjectIdeasSectionProps>();

const getDifficultyColor = (difficulty: string) => {
    switch (difficulty) {
        case "beginner":
            return "bg-green-500/10 text-green-700 border-green-500/20";
        case "intermediate":
            return "bg-yellow-500/10 text-yellow-700 border-yellow-500/20";
        case "advanced":
            return "bg-red-500/10 text-red-700 border-red-500/20";
        default: 
            return "bg-muted";
    }
}
</script>

<template>
    <section class="animate-fade-in">
      <div class="mb-8 text-center">
        <h2 class="mb-3 flex items-center justify-center gap-2 text-3xl font-bold">
          <Lightbulb class="h-8 w-8 text-accent" />
          Your Personalized Project Ideas
        </h2>
        <p class="text-muted-foreground">
          AI-generated suggestions tailored to your profile
        </p>
      </div>

      <div class="grid gap-6 md:grid-cols-2">
        <Card 
          v-for="(idea, index) in ideas"
          :key="idea.id" 
          class="group overflow-hidden border-2 transition-all hover:border-primary hover:shadow-lg animate-scale-in"
          :style="{ animationDelay: `${index * 100}ms` }"
        >
          <CardHeader>
            <div class="mb-3 flex items-start justify-between">
              <Badge :class="getDifficultyColor(idea.difficulty)">
                {{ idea.difficulty }}
              </Badge>
              <Badge variant="outline" class="bg-gradient-accent text-accent-foreground">
                {{ idea.category }}
              </Badge>
            </div>
            <CardTitle class="text-xl group-hover:text-primary transition-colors">
              {{ idea.title }}
            </CardTitle>
            <CardDescription class="text-base">
              {{ idea.description }}
            </CardDescription>
          </CardHeader>
          <CardContent class="space-y-4">
            <div>
              <div class="mb-2 flex items-center gap-2 text-sm font-semibold">
                <Code class="h-4 w-4 text-primary" />
                Required Skills
              </div>
              <div class="flex flex-wrap gap-2">
                <Badge 
                  v-for="(skill, idx) in idea.requiredSkills"
                  :key="idx" 
                  variant="secondary" 
                  class="text-xs"
                >
                  {{ skill }}
                </Badge>
              </div>
            </div>
            
            <div>
              <div class="mb-2 flex items-center gap-2 text-sm font-semibold">
                <TrendingUp class="h-4 w-4 text-accent" />
                Potential Impact
              </div>
              <p class="text-sm text-muted-foreground">
                {{ idea.potentialImpact }}
              </p>
            </div>
          </CardContent>
        </Card>
      </div>
    </section>
</template>