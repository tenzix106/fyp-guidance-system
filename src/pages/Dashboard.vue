<template>
  <div class="grid">
    <div class="col-12">
      <Card>
        <template #content>
          <h2 class="text-2xl font-bold mb-2">Dashboard Overview</h2>
          <p class="text-600">Welcome back to your FYP dashboard</p>
        </template>
      </Card>
    </div>

    <div class="col-12 md:col-4">
      <Card class="bg-primary text-white">
        <template #content>
          <div class="flex flex-column">
            <span class="text-lg font-semibold">Active Projects</span>
            <span class="text-4xl font-bold">{{ stats.activeProjects }}</span>
          </div>
        </template>
      </Card>
    </div>

    <div class="col-12 md:col-4">
      <Card class="bg-green-500 text-white">
        <template #content>
          <div class="flex flex-column">
            <span class="text-lg font-semibold">Completed Tasks</span>
            <span class="text-4xl font-bold">{{ stats.completedTasks }}</span>
          </div>
        </template>
      </Card>
    </div>

    <div class="col-12 md:col-4">
      <Card class="bg-orange-500 text-white">
        <template #content>
          <div class="flex flex-column">
            <span class="text-lg font-semibold">Progress</span>
            <span class="text-4xl font-bold">{{ stats.progress }}%</span>
          </div>
        </template>
      </Card>
    </div>

    <div class="col-12">
      <Card>
        <template #content>
          <h3 class="text-xl font-bold mb-4">Recent Activity</h3>
          <div class="flex flex-column gap-3">
            <div 
              v-for="activity in recentActivity" 
              :key="activity.id"
              class="flex align-items-center gap-3 p-3 border-1 border-200 border-round"
            >
              <i :class="activity.icon" class="text-2xl text-primary"></i>
              <div class="flex-1">
                <div class="font-semibold">{{ activity.title }}</div>
                <div class="text-600 text-sm">{{ activity.description }}</div>
              </div>
              <div class="text-600 text-sm">{{ activity.time }}</div>
            </div>
          </div>
        </template>
      </Card>
    </div>
  </div>
</template>

<script>
import { defineComponent, ref } from 'vue'
import Card from 'primevue/card'

export default defineComponent({
  name: 'Dashboard',
  components: {
    Card
  },
  setup () {
    const stats = ref({
      activeProjects: 3,
      completedTasks: 12,
      progress: 75
    })

    const recentActivity = ref([
      {
        id: 1,
        title: 'Project Proposal Submitted',
        description: 'Final Year Project proposal has been submitted for review',
        icon: 'pi pi-check-circle',
        time: '2 hours ago'
      },
      {
        id: 2,
        title: 'Meeting Scheduled',
        description: 'Supervisor meeting scheduled for tomorrow at 2 PM',
        icon: 'pi pi-calendar',
        time: '1 day ago'
      },
      {
        id: 3,
        title: 'Documentation Updated',
        description: 'Project documentation has been updated with latest changes',
        icon: 'pi pi-file',
        time: '3 days ago'
      }
    ])

    return {
      stats,
      recentActivity
    }
  }
})
</script>
