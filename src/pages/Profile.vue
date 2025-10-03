<template>
  <div class="grid">
    <div class="col-12 md:col-4">
      <Card>
        <template #content>
          <div class="text-center">
            <Avatar 
              :image="user.avatar" 
              size="xlarge" 
              shape="circle" 
              class="mb-3"
            />
            <h3 class="text-xl font-bold mb-2">{{ user.name }}</h3>
            <p class="text-600 mb-1">{{ user.email }}</p>
            <Tag :value="user.role" severity="info" />
          </div>
        </template>
      </Card>
    </div>

    <div class="col-12 md:col-8">
      <Card>
        <template #content>
          <h2 class="text-2xl font-bold mb-4">Profile Information</h2>
          <div class="grid">
            <div class="col-12 md:col-6">
              <div class="field">
                <label for="fullName" class="font-semibold">Full Name</label>
                <InputText 
                  id="fullName"
                  v-model="user.name" 
                  class="w-full"
                />
              </div>
            </div>
            <div class="col-12 md:col-6">
              <div class="field">
                <label for="email" class="font-semibold">Email</label>
                <InputText 
                  id="email"
                  v-model="user.email" 
                  type="email"
                  class="w-full"
                />
              </div>
            </div>
            <div class="col-12 md:col-6">
              <div class="field">
                <label for="studentId" class="font-semibold">Student ID</label>
                <InputText 
                  id="studentId"
                  v-model="user.studentId" 
                  class="w-full"
                />
              </div>
            </div>
            <div class="col-12 md:col-6">
              <div class="field">
                <label for="department" class="font-semibold">Department</label>
                <InputText 
                  id="department"
                  v-model="user.department" 
                  class="w-full"
                />
              </div>
            </div>
            <div class="col-12">
              <div class="field">
                <label for="bio" class="font-semibold">Bio</label>
                <Textarea 
                  id="bio"
                  v-model="user.bio" 
                  rows="4"
                  class="w-full"
                />
              </div>
            </div>
          </div>
          <div class="mt-4">
            <Button 
              label="Update Profile" 
              icon="pi pi-save"
              :loading="updating"
              @click="updateProfile"
            />
          </div>
        </template>
      </Card>
    </div>
  </div>
</template>

<script>
import { defineComponent, ref } from 'vue'
import Card from 'primevue/card'
import Button from 'primevue/button'
import InputText from 'primevue/inputtext'
import Textarea from 'primevue/textarea'
import Avatar from 'primevue/avatar'
import Tag from 'primevue/tag'

export default defineComponent({
  name: 'Profile',
  components: {
    Card,
    Button,
    InputText,
    Textarea,
    Avatar,
    Tag
  },
  setup () {
    const updating = ref(false)
    const user = ref({
      name: 'John Doe',
      email: 'john.doe@university.edu',
      studentId: 'STU12345',
      department: 'Computer Science',
      bio: 'Final year student working on innovative projects',
      role: 'Student',
      avatar: 'https://primefaces.org/cdn/primevue/images/avatar/amyelsner.png'
    })

    const updateProfile = async () => {
      updating.value = true
      // Simulate API call
      await new Promise(resolve => setTimeout(resolve, 1000))
      updating.value = false
      // Show success message
      console.log('Profile updated successfully')
    }

    return {
      user,
      updating,
      updateProfile
    }
  }
})
</script>
