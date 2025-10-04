<script setup lang="ts">
import { ref } from 'vue';
import HeroSection from '@/components/HeroSection.vue';
import ProjectIdeasSection from '@/components/ProjectIdeasSection.vue';
import StudentProfileForm from '@/components/StudentProfileForm.vue';
import ResourcesSection from '@/components/ResourcesSection.vue';


export interface StudentProfile {
    interest: string;
    coursework: string;
    fieldOfStudy: string;
    skills: string;
}

export interface ProjectIdea {
    id: string;
    title: string;
    description: string;
    difficulty: 'beginner' | 'intermediate' | 'advanced';
    category: string;
    requiredSkills: string[];
    potentialImpact: string;
}

export interface Resource {
    id: string;
    title: string;
    type: 'paper' | 'tool' | 'dataset' | 'methodology';
    url: string;
    description: string;
    relevance: number;
}

const studentProfile = ref<StudentProfile | null>(null);
const projectIdeas = ref<ProjectIdea[]>([]);
const resources = ref<Resource[]>([]);
const isGenerating = ref(false);

const handleSubmit = (profile: StudentProfile) => {
    studentProfile.value = profile;
};

const handleSetProjectIdeas = (ideas: ProjectIdea[]) => {
    projectIdeas.value = ideas;
};

const handleSetResources = (resourcesList: Resource[]) => {
    resources.value = resourcesList;
};

const handleSetIsGenerating = (value: boolean) => {
    isGenerating.value = value;
};
</script>


<template>
    <div class="min-h-screen bg-background">
        <HeroSection/>

        <main class="container mx-auto px-4 py-12 space-y-16">
            <StudentProfileForm 
                @submit="handleSubmit"
                @update:project-ideas="handleSetProjectIdeas"
                @update:resources="handleSetResources"
                @update:is-generating="handleSetIsGenerating"
                :is-generating="isGenerating"
            />
            
            <ProjectIdeasSection 
                v-if="projectIdeas.length > 0"
                :ideas="projectIdeas" 
            />
            
            <ResourcesSection 
                v-if="resources.length > 0"
                :resources="resources" 
            />
        </main>
    </div>
</template>