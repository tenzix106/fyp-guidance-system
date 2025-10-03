<template>
  <div class="grid">
    <div class="col-12">
      <Card>
        <template #content>
          <div class="flex justify-content-between align-items-center mb-4">
            <h2 class="text-2xl font-bold m-0">Task Management</h2>
            <Button
              label="Add Task"
              icon="pi pi-plus"
              @click="showNewTaskDialog = true"
            />
          </div>
        </template>
      </Card>
    </div>

    <!-- Task Statistics -->
    <div class="col-12 md:col-3">
      <Card class="bg-blue-500 text-white">
        <template #content>
          <div class="flex flex-column align-items-center">
            <i class="pi pi-list text-4xl mb-2"></i>
            <span class="text-2xl font-bold">{{ totalTasks }}</span>
            <span class="text-sm">Total Tasks</span>
          </div>
        </template>
      </Card>
    </div>

    <div class="col-12 md:col-3">
      <Card class="bg-green-500 text-white">
        <template #content>
          <div class="flex flex-column align-items-center">
            <i class="pi pi-check-circle text-4xl mb-2"></i>
            <span class="text-2xl font-bold">{{ completedTasks }}</span>
            <span class="text-sm">Completed</span>
          </div>
        </template>
      </Card>
    </div>

    <div class="col-12 md:col-3">
      <Card class="bg-orange-500 text-white">
        <template #content>
          <div class="flex flex-column align-items-center">
            <i class="pi pi-clock text-4xl mb-2"></i>
            <span class="text-2xl font-bold">{{ pendingTasks }}</span>
            <span class="text-sm">Pending</span>
          </div>
        </template>
      </Card>
    </div>

    <div class="col-12 md:col-3">
      <Card class="bg-red-500 text-white">
        <template #content>
          <div class="flex flex-column align-items-center">
            <i class="pi pi-exclamation-triangle text-4xl mb-2"></i>
            <span class="text-2xl font-bold">{{ overdueTasks }}</span>
            <span class="text-sm">Overdue</span>
          </div>
        </template>
      </Card>
    </div>

    <!-- Task List -->
    <div class="col-12">
      <Card>
        <template #content>
          <h3 class="text-xl font-bold mb-4">All Tasks</h3>
          
          <DataTable 
            :value="tasks" 
            :paginator="true" 
            :rows="10"
            paginatorTemplate="FirstPageLink PrevPageLink PageLinks NextPageLink LastPageLink CurrentPageReport RowsPerPageDropdown"
            :rowsPerPageOptions="[5,10,25]"
            currentPageReportTemplate="Showing {first} to {last} of {totalRecords} tasks"
            responsiveLayout="scroll"
          >
            <template #header>
              <div class="flex justify-content-between align-items-center">
                <span class="text-lg font-semibold">Task List</span>
                <div class="flex gap-2">
                  <Dropdown 
                    v-model="selectedPriority" 
                    :options="priorityOptions" 
                    placeholder="Filter by Priority"
                    class="w-12rem"
                    @change="filterTasks"
                  />
                  <Dropdown 
                    v-model="selectedStatus" 
                    :options="statusOptions" 
                    placeholder="Filter by Status"
                    class="w-12rem"
                    @change="filterTasks"
                  />
                </div>
              </div>
            </template>

            <Column field="title" header="Task" sortable>
              <template #body="slotProps">
                <div class="flex align-items-center gap-2">
                  <Checkbox 
                    v-model="slotProps.data.completed" 
                    @change="toggleTaskComplete(slotProps.data)"
                  />
                  <span :class="{ 'line-through text-500': slotProps.data.completed }">
                    {{ slotProps.data.title }}
                  </span>
                </div>
              </template>
            </Column>

            <Column field="description" header="Description">
              <template #body="slotProps">
                <span class="text-600">{{ slotProps.data.description }}</span>
              </template>
            </Column>

            <Column field="priority" header="Priority" sortable>
              <template #body="slotProps">
                <Tag 
                  :value="slotProps.data.priority" 
                  :severity="getPrioritySeverity(slotProps.data.priority)"
                />
              </template>
            </Column>

            <Column field="status" header="Status" sortable>
              <template #body="slotProps">
                <Tag 
                  :value="slotProps.data.status" 
                  :severity="getStatusSeverity(slotProps.data.status)"
                />
              </template>
            </Column>

            <Column field="dueDate" header="Due Date" sortable>
              <template #body="slotProps">
                <span :class="{ 'text-red-500': isOverdue(slotProps.data.dueDate) }">
                  {{ formatDate(slotProps.data.dueDate) }}
                </span>
              </template>
            </Column>

            <Column header="Actions">
              <template #body="slotProps">
                <div class="flex gap-2">
                  <Button
                    icon="pi pi-pencil"
                    class="p-button-text p-button-sm"
                    @click="editTask(slotProps.data)"
                  />
                  <Button
                    icon="pi pi-trash"
                    class="p-button-text p-button-sm p-button-danger"
                    @click="deleteTask(slotProps.data)"
                  />
                </div>
              </template>
            </Column>
          </DataTable>
        </template>
      </Card>
    </div>
  </div>

  <!-- New Task Dialog -->
  <Dialog 
    v-model:visible="showNewTaskDialog" 
    header="Add New Task" 
    :style="{ width: '500px' }"
    :modal="true"
  >
    <div class="flex flex-column gap-3">
      <div class="field">
        <label for="taskTitle" class="font-semibold">Task Title</label>
        <InputText 
          id="taskTitle"
          v-model="newTask.title" 
          placeholder="Enter task title"
          class="w-full"
        />
      </div>
      
      <div class="field">
        <label for="taskDescription" class="font-semibold">Description</label>
        <Textarea 
          id="taskDescription"
          v-model="newTask.description" 
          placeholder="Enter task description"
          rows="3"
          class="w-full"
        />
      </div>

      <div class="grid">
        <div class="col-6">
          <div class="field">
            <label for="taskPriority" class="font-semibold">Priority</label>
            <Dropdown 
              id="taskPriority"
              v-model="newTask.priority" 
              :options="priorityOptions"
              placeholder="Select priority"
              class="w-full"
            />
          </div>
        </div>
        <div class="col-6">
          <div class="field">
            <label for="taskDueDate" class="font-semibold">Due Date</label>
            <Calendar 
              id="taskDueDate"
              v-model="newTask.dueDate" 
              placeholder="Select due date"
              class="w-full"
            />
          </div>
        </div>
      </div>
    </div>
    
    <template #footer>
      <Button 
        label="Cancel" 
        icon="pi pi-times" 
        class="p-button-text" 
        @click="showNewTaskDialog = false" 
      />
      <Button 
        label="Add Task" 
        icon="pi pi-check" 
        @click="addTask" 
      />
    </template>
  </Dialog>
</template>

<script>
import { defineComponent, ref, computed } from 'vue'
import Card from 'primevue/card'
import Button from 'primevue/button'
import Dialog from 'primevue/dialog'
import InputText from 'primevue/inputtext'
import Textarea from 'primevue/textarea'
import Dropdown from 'primevue/dropdown'
import Calendar from 'primevue/calendar'
import DataTable from 'primevue/datatable'
import Column from 'primevue/column'
import Tag from 'primevue/tag'
import Checkbox from 'primevue/checkbox'

export default defineComponent({
  name: 'Tasks',
  components: {
    Card,
    Button,
    Dialog,
    InputText,
    Textarea,
    Dropdown,
    Calendar,
    DataTable,
    Column,
    Tag,
    Checkbox
  },
  setup () {
    const showNewTaskDialog = ref(false)
    const selectedPriority = ref(null)
    const selectedStatus = ref(null)
    
    const newTask = ref({
      title: '',
      description: '',
      priority: 'Medium',
      dueDate: null
    })

    const tasks = ref([
      {
        id: 1,
        title: 'Design database schema',
        description: 'Create ERD and database tables for user management',
        priority: 'High',
        status: 'In Progress',
        dueDate: new Date('2024-02-15'),
        completed: false
      },
      {
        id: 2,
        title: 'Implement user authentication',
        description: 'Add login, register, and password reset functionality',
        priority: 'High',
        status: 'Pending',
        dueDate: new Date('2024-02-20'),
        completed: false
      },
      {
        id: 3,
        title: 'Create API documentation',
        description: 'Write comprehensive API documentation using Swagger',
        priority: 'Medium',
        status: 'Completed',
        dueDate: new Date('2024-02-10'),
        completed: true
      },
      {
        id: 4,
        title: 'Setup CI/CD pipeline',
        description: 'Configure automated testing and deployment',
        priority: 'Low',
        status: 'Pending',
        dueDate: new Date('2024-03-01'),
        completed: false
      },
      {
        id: 5,
        title: 'Write unit tests',
        description: 'Add unit tests for all core functionality',
        priority: 'Medium',
        status: 'In Progress',
        dueDate: new Date('2024-02-25'),
        completed: false
      }
    ])

    const priorityOptions = ['Low', 'Medium', 'High', 'Critical']
    const statusOptions = ['Pending', 'In Progress', 'Completed', 'Cancelled']

    const totalTasks = computed(() => tasks.value.length)
    const completedTasks = computed(() => tasks.value.filter(task => task.completed).length)
    const pendingTasks = computed(() => tasks.value.filter(task => !task.completed && task.status !== 'Cancelled').length)
    const overdueTasks = computed(() => {
      const today = new Date()
      return tasks.value.filter(task => 
        !task.completed && 
        task.dueDate && 
        new Date(task.dueDate) < today
      ).length
    })

    const getPrioritySeverity = (priority) => {
      switch (priority) {
        case 'Critical': return 'danger'
        case 'High': return 'warning'
        case 'Medium': return 'info'
        case 'Low': return 'success'
        default: return 'secondary'
      }
    }

    const getStatusSeverity = (status) => {
      switch (status) {
        case 'Completed': return 'success'
        case 'In Progress': return 'warning'
        case 'Pending': return 'info'
        case 'Cancelled': return 'danger'
        default: return 'secondary'
      }
    }

    const isOverdue = (dueDate) => {
      if (!dueDate) return false
      return new Date(dueDate) < new Date() && !tasks.value.find(t => t.dueDate === dueDate)?.completed
    }

    const formatDate = (date) => {
      if (!date) return 'No date'
      return new Date(date).toLocaleDateString()
    }

    const toggleTaskComplete = (task) => {
      task.status = task.completed ? 'Completed' : 'Pending'
    }

    const editTask = (task) => {
      console.log('Edit task:', task.title)
    }

    const deleteTask = (task) => {
      const index = tasks.value.findIndex(t => t.id === task.id)
      if (index > -1) {
        tasks.value.splice(index, 1)
      }
    }

    const addTask = () => {
      if (newTask.value.title) {
        tasks.value.push({
          id: Date.now(),
          title: newTask.value.title,
          description: newTask.value.description,
          priority: newTask.value.priority,
          status: 'Pending',
          dueDate: newTask.value.dueDate,
          completed: false
        })
        newTask.value = {
          title: '',
          description: '',
          priority: 'Medium',
          dueDate: null
        }
        showNewTaskDialog.value = false
      }
    }

    const filterTasks = () => {
      // Filter logic would go here
      console.log('Filtering tasks by:', selectedPriority.value, selectedStatus.value)
    }

    return {
      showNewTaskDialog,
      selectedPriority,
      selectedStatus,
      newTask,
      tasks,
      priorityOptions,
      statusOptions,
      totalTasks,
      completedTasks,
      pendingTasks,
      overdueTasks,
      getPrioritySeverity,
      getStatusSeverity,
      isOverdue,
      formatDate,
      toggleTaskComplete,
      editTask,
      deleteTask,
      addTask,
      filterTasks
    }
  }
})
</script>
