<template>
  <div class="grid">
    <div class="col-12">
      <Card>
        <template #content>
          <div class="flex justify-content-between align-items-center mb-4">
            <h2 class="text-2xl font-bold m-0">Calendar & Events</h2>
            <Button
              label="Add Event"
              icon="pi pi-plus"
              @click="showNewEventDialog = true"
            />
          </div>
        </template>
      </Card>
    </div>

    <!-- Calendar View -->
    <div class="col-12 lg:col-8">
      <Card>
        <template #content>
          <FullCalendar 
            :options="calendarOptions"
            class="w-full"
          />
        </template>
      </Card>
    </div>

    <!-- Upcoming Events -->
    <div class="col-12 lg:col-4">
      <Card>
        <template #content>
          <h3 class="text-xl font-bold mb-4">Upcoming Events</h3>
          <div class="flex flex-column gap-3">
            <div 
              v-for="event in upcomingEvents" 
              :key="event.id"
              class="flex align-items-center gap-3 p-3 border-1 border-200 border-round"
            >
              <div class="flex flex-column align-items-center">
                <span class="text-sm font-semibold">{{ formatDay(event.start) }}</span>
                <span class="text-xs text-600">{{ formatMonth(event.start) }}</span>
              </div>
              <div class="flex-1">
                <div class="font-semibold">{{ event.title }}</div>
                <div class="text-600 text-sm">{{ formatTime(event.start) }}</div>
              </div>
              <Tag 
                :value="event.type" 
                :severity="getEventTypeSeverity(event.type)"
              />
            </div>
          </div>
        </template>
      </Card>

      <!-- Quick Stats -->
      <Card class="mt-4">
        <template #content>
          <h3 class="text-xl font-bold mb-4">This Month</h3>
          <div class="flex flex-column gap-3">
            <div class="flex justify-content-between align-items-center">
              <span class="text-600">Total Events</span>
              <span class="font-semibold">{{ monthlyStats.totalEvents }}</span>
            </div>
            <div class="flex justify-content-between align-items-center">
              <span class="text-600">Meetings</span>
              <span class="font-semibold">{{ monthlyStats.meetings }}</span>
            </div>
            <div class="flex justify-content-between align-items-center">
              <span class="text-600">Deadlines</span>
              <span class="font-semibold">{{ monthlyStats.deadlines }}</span>
            </div>
            <div class="flex justify-content-between align-items-center">
              <span class="text-600">Presentations</span>
              <span class="font-semibold">{{ monthlyStats.presentations }}</span>
            </div>
          </div>
        </template>
      </Card>
    </div>
  </div>

  <!-- New Event Dialog -->
  <Dialog 
    v-model:visible="showNewEventDialog" 
    header="Add New Event" 
    :style="{ width: '500px' }"
    :modal="true"
  >
    <div class="flex flex-column gap-3">
      <div class="field">
        <label for="eventTitle" class="font-semibold">Event Title</label>
        <InputText 
          id="eventTitle"
          v-model="newEvent.title" 
          placeholder="Enter event title"
          class="w-full"
        />
      </div>
      
      <div class="field">
        <label for="eventDescription" class="font-semibold">Description</label>
        <Textarea 
          id="eventDescription"
          v-model="newEvent.description" 
          placeholder="Enter event description"
          rows="3"
          class="w-full"
        />
      </div>

      <div class="grid">
        <div class="col-6">
          <div class="field">
            <label for="eventType" class="font-semibold">Event Type</label>
            <Dropdown 
              id="eventType"
              v-model="newEvent.type" 
              :options="eventTypes"
              placeholder="Select type"
              class="w-full"
            />
          </div>
        </div>
        <div class="col-6">
          <div class="field">
            <label for="eventLocation" class="font-semibold">Location</label>
            <InputText 
              id="eventLocation"
              v-model="newEvent.location" 
              placeholder="Enter location"
              class="w-full"
            />
          </div>
        </div>
      </div>

      <div class="grid">
        <div class="col-6">
          <div class="field">
            <label for="eventStart" class="font-semibold">Start Date & Time</label>
            <Calendar 
              id="eventStart"
              v-model="newEvent.start" 
              showTime
              hourFormat="12"
              placeholder="Select start time"
              class="w-full"
            />
          </div>
        </div>
        <div class="col-6">
          <div class="field">
            <label for="eventEnd" class="font-semibold">End Date & Time</label>
            <Calendar 
              id="eventEnd"
              v-model="newEvent.end" 
              showTime
              hourFormat="12"
              placeholder="Select end time"
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
        @click="showNewEventDialog = false" 
      />
      <Button 
        label="Add Event" 
        icon="pi pi-check" 
        @click="addEvent" 
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
import Tag from 'primevue/tag'

export default defineComponent({
  name: 'Calendar',
  components: {
    Card,
    Button,
    Dialog,
    InputText,
    Textarea,
    Dropdown,
    Calendar,
    Tag
  },
  setup () {
    const showNewEventDialog = ref(false)
    
    const newEvent = ref({
      title: '',
      description: '',
      type: 'Meeting',
      location: '',
      start: null,
      end: null
    })

    const eventTypes = ['Meeting', 'Deadline', 'Presentation', 'Review', 'Other']

    const events = ref([
      {
        id: 1,
        title: 'Project Proposal Review',
        description: 'Review and discuss project proposal with supervisor',
        type: 'Meeting',
        location: 'Room 201',
        start: new Date('2024-02-15T10:00:00'),
        end: new Date('2024-02-15T11:00:00')
      },
      {
        id: 2,
        title: 'Database Design Deadline',
        description: 'Submit final database design document',
        type: 'Deadline',
        location: 'Online',
        start: new Date('2024-02-20T23:59:00'),
        end: new Date('2024-02-20T23:59:00')
      },
      {
        id: 3,
        title: 'Progress Presentation',
        description: 'Present project progress to committee',
        type: 'Presentation',
        location: 'Auditorium A',
        start: new Date('2024-02-25T14:00:00'),
        end: new Date('2024-02-25T15:30:00')
      },
      {
        id: 4,
        title: 'Code Review Session',
        description: 'Review code implementation with team',
        type: 'Review',
        location: 'Lab 3',
        start: new Date('2024-02-28T16:00:00'),
        end: new Date('2024-02-28T17:00:00')
      }
    ])

    const upcomingEvents = computed(() => {
      const today = new Date()
      return events.value
        .filter(event => new Date(event.start) >= today)
        .sort((a, b) => new Date(a.start) - new Date(b.start))
        .slice(0, 5)
    })

    const monthlyStats = computed(() => {
      const currentMonth = new Date().getMonth()
      const currentYear = new Date().getFullYear()
      
      const monthlyEvents = events.value.filter(event => {
        const eventDate = new Date(event.start)
        return eventDate.getMonth() === currentMonth && eventDate.getFullYear() === currentYear
      })

      return {
        totalEvents: monthlyEvents.length,
        meetings: monthlyEvents.filter(e => e.type === 'Meeting').length,
        deadlines: monthlyEvents.filter(e => e.type === 'Deadline').length,
        presentations: monthlyEvents.filter(e => e.type === 'Presentation').length
      }
    })

    const calendarOptions = ref({
      plugins: [],
      initialView: 'dayGridMonth',
      headerToolbar: {
        left: 'prev,next today',
        center: 'title',
        right: 'dayGridMonth,timeGridWeek,timeGridDay'
      },
      events: events.value.map(event => ({
        id: event.id,
        title: event.title,
        start: event.start,
        end: event.end,
        extendedProps: {
          description: event.description,
          type: event.type,
          location: event.location
        }
      })),
      eventClick: (info) => {
        console.log('Event clicked:', info.event.title)
      }
    })

    const getEventTypeSeverity = (type) => {
      switch (type) {
        case 'Deadline': return 'danger'
        case 'Presentation': return 'warning'
        case 'Meeting': return 'info'
        case 'Review': return 'success'
        default: return 'secondary'
      }
    }

    const formatDay = (date) => {
      return new Date(date).getDate()
    }

    const formatMonth = (date) => {
      return new Date(date).toLocaleDateString('en-US', { month: 'short' })
    }

    const formatTime = (date) => {
      return new Date(date).toLocaleTimeString('en-US', { 
        hour: '2-digit', 
        minute: '2-digit' 
      })
    }

    const addEvent = () => {
      if (newEvent.value.title && newEvent.value.start) {
        events.value.push({
          id: Date.now(),
          title: newEvent.value.title,
          description: newEvent.value.description,
          type: newEvent.value.type,
          location: newEvent.value.location,
          start: newEvent.value.start,
          end: newEvent.value.end || newEvent.value.start
        })
        
        // Update calendar events
        calendarOptions.value.events = events.value.map(event => ({
          id: event.id,
          title: event.title,
          start: event.start,
          end: event.end,
          extendedProps: {
            description: event.description,
            type: event.type,
            location: event.location
          }
        }))
        
        newEvent.value = {
          title: '',
          description: '',
          type: 'Meeting',
          location: '',
          start: null,
          end: null
        }
        showNewEventDialog.value = false
      }
    }

    return {
      showNewEventDialog,
      newEvent,
      eventTypes,
      events,
      upcomingEvents,
      monthlyStats,
      calendarOptions,
      getEventTypeSeverity,
      formatDay,
      formatMonth,
      formatTime,
      addEvent
    }
  }
})
</script>
