<script setup lang="ts">
import { ref } from 'vue';
import { Button } from '../components/ui/index.vue';
import { Input } from '../components/ui/index.vue';
import { Label } from '../components/ui/index.vue';
import { Textarea } from '../components/ui/index.vue';

import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '../components/ui/index.vue';
import { Loader2, Sparkles } from 'lucide-vue-next';
import { useToast } from '../../hooks/useToast';
import { StudentProfile, ProjectIdea, Resource } from '../../pages/Index.vue';

// Removed Supabase; using Flask backend via Vite proxy

// Props are received via v-model-like emits in parent; only isGenerating is needed as prop
const props = defineProps<{ isGenerating: boolean }>();

const emit = defineEmits<{
    submit: [profile: StudentProfile];
    'update:project-ideas': [ideas: ProjectIdea[]];
    'update:resources': [resources: Resource[]];
    'update:is-generating': [generating: boolean];
}>();

const { toast } = useToast();

const formData = ref<StudentProfile>({
    interest: '',
    coursework: '',
    fieldOfStudy: '',
    skills: '',
});


const handleSubmit = async (e: Event) => {
  e.preventDefault();

  if (!formData.value.interest.trim() || !formData.value.fieldOfStudy.trim()) {
    toast({
      title: 'Missing Information',
      description: 'Please fill in at least your interests and field of study.',
      variant: 'destructive',
    });
    return;
  }

  emit('update:is-generating', true);
  emit('submit', formData.value);

  try {
    const resp = await fetch('/api/generate-fyp-ideas', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ profile: formData.value }),
    });
    if (!resp.ok) {
      throw new Error(`HTTP ${resp.status}`);
    }
    const data = await resp.json();

    if (data?.ideas) emit('update:project-ideas', data.ideas);
    if (data?.resources) emit('update:resources', data.resources);

    toast({
      title: 'Success!',
      description: 'AI has generated personalized project ideas and resources for you.',
    });
  } catch (error) {
    console.error('Error generating ideas:', error);
    toast({
      title: 'Error',
      description: 'Failed to generate project ideas. Please try again.',
      variant: 'destructive',
    });
  } finally {
    emit('update:is-generating', false);
  }
};
</script>

<template>
    <Card class="mx-auto max-w-3xl animate-slide-up shadow-lg">
      <CardHeader>
        <CardTitle class="flex items-center gap-2 text-2xl">
          <Sparkles :size="24" class="text-accent" />
          Tell Us About Yourself
        </CardTitle>
        <CardDescription>
          Share your interests and background to get personalized project recommendations
        </CardDescription>
      </CardHeader>
      <CardContent>
        <form @submit="handleSubmit" class="space-y-6">
          <div class="space-y-2">
            <Label for="fieldOfStudy">Field of Study *</Label>
            <Input
              id="fieldOfStudy"
              v-model="formData.fieldOfStudy"
              placeholder="e.g., Computer Science, Engineering, Data Science"
              required
            />
          </div>
  
          <div class="space-y-2">
            <Label for="interests">Your Interests *</Label>
            <Textarea
              id="interests"
              v-model="formData.interest"
              placeholder="e.g., Machine Learning, Web Development, IoT, Cybersecurity..."
              :rows="3"
              required
            />
          </div>
  
          <div class="space-y-2">
            <Label for="coursework">Relevant Coursework</Label>
            <Textarea
              id="coursework"
              v-model="formData.coursework"
              placeholder="e.g., Database Systems, Algorithms, Networks, AI..."
              :rows="3"
            />
          </div>
  
          <div class="space-y-2">
            <Label for="skills">Technical Skills</Label>
            <Input
              id="skills"
              v-model="formData.skills"
              placeholder="e.g., Python, JavaScript, React, TensorFlow..."
            />
          </div>
  
          <Button
            type="submit"
            class="w-full bg-gradient-accent font-semibold shadow-md hover:shadow-lg transition-all"
            :disabled="isGenerating"
          >
            <template v-if="isGenerating">
              <Loader2 :size="16" class="mr-2 animate-spin" />
              Generating Ideas...
            </template>
            <template v-else>
              <Sparkles :size="16" class="mr-2" />
              Generate Project Ideas
            </template>
          </Button>
        </form>
      </CardContent>
    </Card>
  </template>