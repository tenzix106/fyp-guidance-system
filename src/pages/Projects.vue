<template>
  <div class="grid">
    <div class="col-12">
      <Card>
        <template #content>
          <div class="flex justify-content-between align-items-center mb-4">
            <h2 class="text-2xl font-bold m-0">My Projects</h2>
            <Button
              label="New Project"
              icon="pi pi-plus"
              @click="showNewProjectDialog = true"
            />
          </div>
        </template>
      </Card>
    </div>

    <div class="col-12">
      <div class="grid">
        <div 
          v-for="project in projects" 
          :key="project.id" 
          class="col-12 md:col-6 lg:col-4"
        >
          <Card class="h-full">
            <template #content>
              <div class="flex flex-column h-full">
                <div class="flex justify-content-between align-items-start mb-3">
                  <h3 class="text-xl font-semibold m-0">{{ project.title }}</h3>
                  <Button
                    icon="pi pi-ellipsis-v"
                    class="p-button-text p-button-plain"
                    @click="showProjectMenu(project)"
                  />
                </div>
                
                <p class="text-600 mb-3 flex-1">{{ project.description }}</p>
                
                <div class="flex gap-2 mb-3">
                  <Tag 
                    :value="project.status" 
                    :severity="getStatusSeverity(project.status)"
                  />
                  <Tag 
                    :value="`${project.progress}% Complete`" 
                    severity="info"
                  />
                </div>
                
                <ProgressBar 
                  :value="project.progress" 
                  class="mb-3"
                />
                
                <div class="flex gap-2">
                  <Button
                    label="View"
                    icon="pi pi-eye"
                    class="p-button-text p-button-sm"
                    @click="viewProject(project)"
                  />
                  <Button
                    label="Edit"
                    icon="pi pi-pencil"
                    class="p-button-text p-button-sm"
                    @click="editProject(project)"
                  />
                </div>
              </div>
            </template>
          </Card>
        </div>
      </div>
    </div>
  </div>

  <!-- New Project Dialog -->
  <Dialog 
    v-model:visible="showNewProjectDialog" 
    header="Create New Project" 
    :style="{ width: '450px' }"
    :modal="true"
  >
    <div class="flex flex-column gap-3">
      <div class="field">
        <label for="title" class="font-semibold">Project Title</label>
        <InputText 
          id="title"
          v-model="newProject.title" 
          placeholder="Enter project title"
          class="w-full"
        />
      </div>
      
      <div class="field">
        <label for="description" class="font-semibold">Description</label>
        <Textarea 
          id="description"
          v-model="newProject.description" 
          placeholder="Enter project description"
          rows="3"
          class="w-full"
        />
      </div>
    </div>
    
    <template #footer>
      <Button 
        label="Cancel" 
        icon="pi pi-times" 
        class="p-button-text" 
        @click="showNewProjectDialog = false" 
      />
      <Button 
        label="Create" 
        icon="pi pi-check" 
        @click="createProject" 
      />
    </template>
  </Dialog>
</template>

<script>
import { defineComponent, ref } from 'vue'
import Card from 'primevue/card'
import Button from 'primevue/button'
import Dialog from 'primevue/dialog'
import InputText from 'primevue/inputtext'
import Textarea from 'primevue/textarea'
import Tag from 'primevue/tag'
import ProgressBar from 'primevue/progressbar'

export default defineComponent({
  name: 'Projects',
  components: {
    Card,
    Button,
    Dialog,
    InputText,
    Textarea,
    Tag,
    ProgressBar
  },
  setup () {
    const showNewProjectDialog = ref(false)
    const newProject = ref({
      title: '',
      description: ''
    })

    const projects = ref([
      {
        id: 1,
        title: 'E-Learning Platform',
        description: 'A comprehensive online learning management system with video streaming, quizzes, and progress tracking features.',
        status: 'In Progress',
        progress: 65,
        startDate: '2024-01-15',
        endDate: '2024-06-15'
      },
      {
        id: 2,
        title: 'Mobile Health App',
        description: 'Health monitoring and tracking application with wearable device integration and health analytics.',
        status: 'Planning',
        progress: 20,
        startDate: '2024-02-01',
        endDate: '2024-08-01'
      },
      {
        id: 3,
        title: 'IoT Smart Home System',
        description: 'Internet of Things based home automation system with voice control and energy monitoring.',
        status: 'Completed',
        progress: 100,
        startDate: '2023-09-01',
        endDate: '2024-01-01'
      },
      {
        id: 4,
        title: 'AI Chatbot Assistant',
        description: 'Intelligent chatbot for customer support with natural language processing capabilities.',
        status: 'In Progress',
        progress: 40,
        startDate: '2024-01-20',
        endDate: '2024-05-20'
      },
      {
        id: 5,
        title: 'Blockchain Voting System',
        description: 'Secure and transparent voting system using blockchain technology for elections.',
        status: 'Planning',
        progress: 10,
        startDate: '2024-03-01',
        endDate: '2024-09-01'
      }
    ])

    const getStatusSeverity = (status) => {
      switch (status) {
        case 'Completed': return 'success'
        case 'In Progress': return 'warning'
        case 'Planning': return 'info'
        default: return 'secondary'
      }
    }

    const showProjectMenu = (project) => {
      console.log('Show menu for project:', project.title)
    }

    const viewProject = (project) => {
      console.log('View project:', project.title)
    }

    const editProject = (project) => {
      console.log('Edit project:', project.title)
    }

    const createProject = () => {
      if (newProject.value.title && newProject.value.description) {
        projects.value.push({
          id: Date.now(),
          title: newProject.value.title,
          description: newProject.value.description,
          status: 'Planning',
          progress: 0,
          startDate: new Date().toISOString().split('T')[0],
          endDate: new Date(Date.now() + 6 * 30 * 24 * 60 * 60 * 1000).toISOString().split('T')[0]
        })
        newProject.value = { title: '', description: '' }
        showNewProjectDialog.value = false
      }
    }

    return {
      showNewProjectDialog,
      newProject,
      projects,
      getStatusSeverity,
      showProjectMenu,
      viewProject,
      editProject,
      createProject
    }
  }
})
</script>
