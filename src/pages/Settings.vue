<template>
  <div class="grid">
    <div class="col-12">
      <Card>
        <template #content>
          <h2 class="text-2xl font-bold mb-4">Settings</h2>
          <p class="text-600">Manage your application preferences and account settings.</p>
        </template>
      </Card>
    </div>

    <!-- Profile Settings -->
    <div class="col-12 lg:col-6">
      <Card>
        <template #content>
          <h3 class="text-xl font-bold mb-4">Profile Settings</h3>
          <div class="flex flex-column gap-4">
            <div class="field">
              <label for="fullName" class="font-semibold">Full Name</label>
              <InputText 
                id="fullName"
                v-model="profileSettings.fullName" 
                class="w-full"
              />
            </div>
            
            <div class="field">
              <label for="email" class="font-semibold">Email</label>
              <InputText 
                id="email"
                v-model="profileSettings.email" 
                type="email"
                class="w-full"
              />
            </div>
            
            <div class="field">
              <label for="studentId" class="font-semibold">Student ID</label>
              <InputText 
                id="studentId"
                v-model="profileSettings.studentId" 
                class="w-full"
              />
            </div>
            
            <div class="field">
              <label for="department" class="font-semibold">Department</label>
              <Dropdown 
                id="department"
                v-model="profileSettings.department" 
                :options="departments"
                placeholder="Select department"
                class="w-full"
              />
            </div>
            
            <div class="field">
              <label for="bio" class="font-semibold">Bio</label>
              <Textarea 
                id="bio"
                v-model="profileSettings.bio" 
                rows="4"
                class="w-full"
              />
            </div>
            
            <Button 
              label="Save Profile" 
              icon="pi pi-save"
              @click="saveProfile"
              :loading="savingProfile"
            />
          </div>
        </template>
      </Card>
    </div>

    <!-- Notification Settings -->
    <div class="col-12 lg:col-6">
      <Card>
        <template #content>
          <h3 class="text-xl font-bold mb-4">Notification Settings</h3>
          <div class="flex flex-column gap-4">
            <div class="flex justify-content-between align-items-center">
              <div>
                <div class="font-semibold">Email Notifications</div>
                <div class="text-600 text-sm">Receive notifications via email</div>
              </div>
              <InputSwitch v-model="notificationSettings.email" />
            </div>
            
            <div class="flex justify-content-between align-items-center">
              <div>
                <div class="font-semibold">Project Updates</div>
                <div class="text-600 text-sm">Get notified about project changes</div>
              </div>
              <InputSwitch v-model="notificationSettings.projectUpdates" />
            </div>
            
            <div class="flex justify-content-between align-items-center">
              <div>
                <div class="font-semibold">Deadline Reminders</div>
                <div class="text-600 text-sm">Remind me about upcoming deadlines</div>
              </div>
              <InputSwitch v-model="notificationSettings.deadlineReminders" />
            </div>
            
            <div class="flex justify-content-between align-items-center">
              <div>
                <div class="font-semibold">Meeting Alerts</div>
                <div class="text-600 text-sm">Alert me about scheduled meetings</div>
              </div>
              <InputSwitch v-model="notificationSettings.meetingAlerts" />
            </div>
            
            <div class="field">
              <label for="reminderTime" class="font-semibold">Reminder Time</label>
              <Dropdown 
                id="reminderTime"
                v-model="notificationSettings.reminderTime" 
                :options="reminderTimes"
                placeholder="Select reminder time"
                class="w-full"
              />
            </div>
          </div>
        </template>
      </Card>
    </div>

    <!-- Application Settings -->
    <div class="col-12">
      <Card>
        <template #content>
          <h3 class="text-xl font-bold mb-4">Application Settings</h3>
          <div class="grid">
            <div class="col-12 md:col-6">
              <div class="flex flex-column gap-4">
                <div class="field">
                  <label for="theme" class="font-semibold">Theme</label>
                  <Dropdown 
                    id="theme"
                    v-model="appSettings.theme" 
                    :options="themes"
                    placeholder="Select theme"
                    class="w-full"
                  />
                </div>
                
                <div class="field">
                  <label for="language" class="font-semibold">Language</label>
                  <Dropdown 
                    id="language"
                    v-model="appSettings.language" 
                    :options="languages"
                    placeholder="Select language"
                    class="w-full"
                  />
                </div>
                
                <div class="flex justify-content-between align-items-center">
                  <div>
                    <div class="font-semibold">Auto-save</div>
                    <div class="text-600 text-sm">Automatically save changes</div>
                  </div>
                  <InputSwitch v-model="appSettings.autoSave" />
                </div>
              </div>
            </div>
            
            <div class="col-12 md:col-6">
              <div class="flex flex-column gap-4">
                <div class="field">
                  <label for="itemsPerPage" class="font-semibold">Items per Page</label>
                  <Dropdown 
                    id="itemsPerPage"
                    v-model="appSettings.itemsPerPage" 
                    :options="itemsPerPageOptions"
                    placeholder="Select items per page"
                    class="w-full"
                  />
                </div>
                
                <div class="flex justify-content-between align-items-center">
                  <div>
                    <div class="font-semibold">Dark Mode</div>
                    <div class="text-600 text-sm">Use dark theme</div>
                  </div>
                  <InputSwitch v-model="appSettings.darkMode" />
                </div>
                
                <div class="flex justify-content-between align-items-center">
                  <div>
                    <div class="font-semibold">Compact Mode</div>
                    <div class="text-600 text-sm">Use compact interface</div>
                  </div>
                  <InputSwitch v-model="appSettings.compactMode" />
                </div>
              </div>
            </div>
          </div>
          
          <div class="flex gap-2 mt-4">
            <Button 
              label="Save Settings" 
              icon="pi pi-save"
              @click="saveSettings"
              :loading="savingSettings"
            />
            <Button 
              label="Reset to Default" 
              icon="pi pi-refresh"
              class="p-button-outlined"
              @click="resetSettings"
            />
          </div>
        </template>
      </Card>
    </div>

    <!-- Account Actions -->
    <div class="col-12">
      <Card>
        <template #content>
          <h3 class="text-xl font-bold mb-4">Account Actions</h3>
          <div class="flex flex-column gap-3">
            <div class="flex justify-content-between align-items-center p-3 border-1 border-200 border-round">
              <div>
                <div class="font-semibold">Change Password</div>
                <div class="text-600 text-sm">Update your account password</div>
              </div>
              <Button 
                label="Change" 
                icon="pi pi-key"
                class="p-button-outlined"
                @click="changePassword"
              />
            </div>
            
            <div class="flex justify-content-between align-items-center p-3 border-1 border-200 border-round">
              <div>
                <div class="font-semibold">Export Data</div>
                <div class="text-600 text-sm">Download your project data</div>
              </div>
              <Button 
                label="Export" 
                icon="pi pi-download"
                class="p-button-outlined"
                @click="exportData"
              />
            </div>
            
            <div class="flex justify-content-between align-items-center p-3 border-1 border-200 border-round">
              <div>
                <div class="font-semibold text-red-500">Delete Account</div>
                <div class="text-600 text-sm">Permanently delete your account</div>
              </div>
              <Button 
                label="Delete" 
                icon="pi pi-trash"
                class="p-button-outlined p-button-danger"
                @click="deleteAccount"
              />
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
import Button from 'primevue/button'
import InputText from 'primevue/inputtext'
import Textarea from 'primevue/textarea'
import Dropdown from 'primevue/dropdown'
import InputSwitch from 'primevue/inputswitch'

export default defineComponent({
  name: 'Settings',
  components: {
    Card,
    Button,
    InputText,
    Textarea,
    Dropdown,
    InputSwitch
  },
  setup () {
    const savingProfile = ref(false)
    const savingSettings = ref(false)
    
    const profileSettings = ref({
      fullName: 'John Doe',
      email: 'john.doe@university.edu',
      studentId: 'STU12345',
      department: 'Computer Science',
      bio: 'Final year student working on innovative projects'
    })
    
    const notificationSettings = ref({
      email: true,
      projectUpdates: true,
      deadlineReminders: true,
      meetingAlerts: false,
      reminderTime: '1 hour before'
    })
    
    const appSettings = ref({
      theme: 'Light',
      language: 'English',
      autoSave: true,
      itemsPerPage: 10,
      darkMode: false,
      compactMode: false
    })
    
    const departments = ['Computer Science', 'Information Technology', 'Software Engineering', 'Data Science', 'Cybersecurity']
    const themes = ['Light', 'Dark', 'Auto']
    const languages = ['English', 'Spanish', 'French', 'German', 'Chinese']
    const reminderTimes = ['15 minutes before', '30 minutes before', '1 hour before', '1 day before']
    const itemsPerPageOptions = [5, 10, 25, 50, 100]
    
    const saveProfile = async () => {
      savingProfile.value = true
      // Simulate API call
      await new Promise(resolve => setTimeout(resolve, 1000))
      savingProfile.value = false
      console.log('Profile saved:', profileSettings.value)
    }
    
    const saveSettings = async () => {
      savingSettings.value = true
      // Simulate API call
      await new Promise(resolve => setTimeout(resolve, 1000))
      savingSettings.value = false
      console.log('Settings saved:', { notificationSettings: notificationSettings.value, appSettings: appSettings.value })
    }
    
    const resetSettings = () => {
      notificationSettings.value = {
        email: true,
        projectUpdates: true,
        deadlineReminders: true,
        meetingAlerts: false,
        reminderTime: '1 hour before'
      }
      appSettings.value = {
        theme: 'Light',
        language: 'English',
        autoSave: true,
        itemsPerPage: 10,
        darkMode: false,
        compactMode: false
      }
      console.log('Settings reset to default')
    }
    
    const changePassword = () => {
      console.log('Change password clicked')
    }
    
    const exportData = () => {
      console.log('Export data clicked')
    }
    
    const deleteAccount = () => {
      console.log('Delete account clicked')
    }
    
    return {
      savingProfile,
      savingSettings,
      profileSettings,
      notificationSettings,
      appSettings,
      departments,
      themes,
      languages,
      reminderTimes,
      itemsPerPageOptions,
      saveProfile,
      saveSettings,
      resetSettings,
      changePassword,
      exportData,
      deleteAccount
    }
  }
})
</script>
