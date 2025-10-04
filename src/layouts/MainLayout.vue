<template>
  <div class="min-h-screen flex flex-col">
    <Menubar :model="menuItems" class="sticky top-0 z-50">
      <template #start>
        <Button 
          icon="pi pi-bars" 
          class="p-button-text p-button-plain"
          @click="toggleSidebar"
        />
        <span class="ml-2 font-bold text-xl">FYP Guidance System</span>
      </template>
    </Menubar>

    <div class="flex flex-1">
      <Sidebar v-model:visible="sidebarVisible" class="w-64">
        <div class="p-4">
          <h3 class="text-lg font-semibold mb-3">Navigation</h3>
          <div class="flex flex-col gap-2">
            <Button
              v-for="link in essentialLinks"
              :key="link.title"
              :label="link.title"
              :icon="link.icon"
              class="p-button-text p-button-plain justify-start w-full"
              @click="navigateTo(link.link)"
            />
          </div>
        </div>
      </Sidebar>

      <div class="flex-1 p-4">
        <router-view />
      </div>
    </div>
  </div>
</template>

<script>
import { defineComponent, ref } from 'vue'
import { useRouter } from 'vue-router'
import Menubar from 'primevue/menubar'
import Sidebar from 'primevue/sidebar'
import Button from 'primevue/button'

const linksList = [
  {
    title: 'Home',
    icon: 'pi pi-home',
    link: '/'
  },
  {
    title: 'Dashboard',
    icon: 'pi pi-chart-bar',
    link: '/dashboard'
  },
  {
    title: 'Projects',
    icon: 'pi pi-briefcase',
    link: '/projects'
  },
  {
    title: 'Tasks',
    icon: 'pi pi-list',
    link: '/tasks'
  },
  {
    title: 'Calendar',
    icon: 'pi pi-calendar',
    link: '/calendar'
  },
  {
    title: 'Profile',
    icon: 'pi pi-user',
    link: '/profile'
  },
  {
    title: 'Settings',
    icon: 'pi pi-cog',
    link: '/settings'
  }
]

export default defineComponent({
  name: 'MainLayout',

  components: {
    Menubar,
    Sidebar,
    Button
  },

  setup () {
    const router = useRouter()
    const sidebarVisible = ref(false)
    const menuItems = ref([])

    const toggleSidebar = () => {
      sidebarVisible.value = !sidebarVisible.value
    }

    const navigateTo = (path) => {
      router.push(path)
      sidebarVisible.value = false
    }

    return {
      essentialLinks: linksList,
      menuItems,
      sidebarVisible,
      toggleSidebar,
      navigateTo
    }
  }
})
</script>

