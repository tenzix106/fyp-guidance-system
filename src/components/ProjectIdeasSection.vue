<script lang="ts">
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '../../src/components/ui/index.vue';
import { Badge } from '../../src/components/ui/index.vue';
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
    <section className="animate-fade-in">
      <div className="mb-8 text-center">
        <h2 className="mb-3 flex items-center justify-center gap-2 text-3xl font-bold">
          <Lightbulb className="h-8 w-8 text-accent" />
          Your Personalized Project Ideas
        </h2>
        <p className="text-muted-foreground">
          AI-generated suggestions tailored to your profile
        </p>
      </div>

      <div className="grid gap-6 md:grid-cols-2">
        {ideas.map((idea, index) => (
          <Card 
            key={idea.id} 
            className="group overflow-hidden border-2 transition-all hover:border-primary hover:shadow-lg animate-scale-in"
            style={{ animationDelay: `${index * 100}ms` }}
          >
            <CardHeader>
              <div className="mb-3 flex items-start justify-between">
                <Badge className={getDifficultyColor(idea.difficulty)}>
                  {idea.difficulty}
                </Badge>
                <Badge variant="outline" className="bg-gradient-accent text-accent-foreground">
                  {idea.category}
                </Badge>
              </div>
              <CardTitle className="text-xl group-hover:text-primary transition-colors">
                {idea.title}
              </CardTitle>
              <CardDescription className="text-base">
                {idea.description}
              </CardDescription>
            </CardHeader>
            <CardContent className="space-y-4">
              <div>
                <div className="mb-2 flex items-center gap-2 text-sm font-semibold">
                  <Code className="h-4 w-4 text-primary" />
                  Required Skills
                </div>
                <div className="flex flex-wrap gap-2">
                  {idea.requiredSkills.map((skill, idx) => (
                    <Badge key={idx} variant="secondary" className="text-xs">
                      {skill}
                    </Badge>
                  ))}
                </div>
              </div>
              
              <div>
                <div className="mb-2 flex items-center gap-2 text-sm font-semibold">
                  <TrendingUp className="h-4 w-4 text-accent" />
                  Potential Impact
                </div>
                <p className="text-sm text-muted-foreground">
                  {idea.potentialImpact}
                </p>
              </div>
            </CardContent>
          </Card>
        ))}
      </div>
    </section>
</template>