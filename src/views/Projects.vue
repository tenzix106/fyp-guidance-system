<template>
  <div class="projects">
    <div class="container">
      <div class="page-header">
        <h1 class="page-title">My Projects</h1>
        <button class="btn">Create New Project</button>
      </div>
      
      <div class="projects-grid">
        <div class="project-card card" v-for="project in projects" :key="project.id">
          <div class="project-header">
            <h3 class="project-title">{{ project.title }}</h3>
            <span class="project-status" :class="project.status">{{ project.status }}</span>
          </div>
          
          <p class="project-description">{{ project.description }}</p>
          
          <div class="project-meta">
            <div class="meta-item">
              <span class="meta-label">Start Date:</span>
              <span class="meta-value">{{ project.startDate }}</span>
            </div>
            <div class="meta-item">
              <span class="meta-label">Due Date:</span>
              <span class="meta-value">{{ project.dueDate }}</span>
            </div>
            <div class="meta-item">
              <span class="meta-label">Progress:</span>
              <div class="progress-bar">
                <div class="progress-fill" :style="{ width: project.progress + '%' }"></div>
              </div>
              <span class="progress-text">{{ project.progress }}%</span>
            </div>
          </div>
          
          <div class="project-actions">
            <button class="btn btn-sm">View Details</button>
            <button class="btn btn-sm btn-secondary">Edit</button>
          </div>
        </div>
      </div>
      
      <div class="empty-state" v-if="projects.length === 0">
        <div class="empty-icon">📁</div>
        <h3>No Projects Yet</h3>
        <p>Start your FYP journey by creating your first project.</p>
        <button class="btn">Create Your First Project</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Projects',
  data() {
    return {
      projects: [
        {
          id: 1,
          title: 'AI-Powered Learning Management System',
          description: 'Developing an intelligent LMS with personalized learning paths and automated assessment features.',
          status: 'active',
          startDate: 'Sep 1, 2024',
          dueDate: 'May 15, 2025',
          progress: 65
        },
        {
          id: 2,
          title: 'Blockchain-based Supply Chain Tracking',
          description: 'Creating a transparent and secure supply chain tracking system using blockchain technology.',
          status: 'planning',
          startDate: 'Oct 1, 2024',
          dueDate: 'Apr 30, 2025',
          progress: 25
        },
        {
          id: 3,
          title: 'IoT Smart Home Automation',
          description: 'Building an integrated IoT system for smart home automation with mobile app control.',
          status: 'completed',
          startDate: 'Jan 1, 2024',
          dueDate: 'Aug 31, 2024',
          progress: 100
        }
      ]
    }
  }
}
</script>

<style scoped>
.projects {
  padding: 2rem 0;
}

.page-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 3rem;
}

.page-title {
  font-size: 2.5rem;
  color: #333;
  margin: 0;
}

.projects-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
  gap: 2rem;
}

.project-card {
  transition: transform 0.3s ease;
}

.project-card:hover {
  transform: translateY(-4px);
}

.project-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 1rem;
}

.project-title {
  font-size: 1.25rem;
  color: #333;
  margin: 0;
  flex: 1;
  margin-right: 1rem;
}

.project-status {
  padding: 0.25rem 0.75rem;
  border-radius: 20px;
  font-size: 0.8rem;
  font-weight: 500;
  text-transform: uppercase;
}

.project-status.active {
  background-color: #d4edda;
  color: #155724;
}

.project-status.planning {
  background-color: #fff3cd;
  color: #856404;
}

.project-status.completed {
  background-color: #d1ecf1;
  color: #0c5460;
}

.project-description {
  color: #6c757d;
  margin-bottom: 1.5rem;
  line-height: 1.6;
}

.project-meta {
  margin-bottom: 1.5rem;
}

.meta-item {
  display: flex;
  align-items: center;
  margin-bottom: 0.75rem;
  gap: 0.5rem;
}

.meta-label {
  font-weight: 500;
  color: #495057;
  min-width: 80px;
}

.meta-value {
  color: #6c757d;
}

.progress-bar {
  flex: 1;
  height: 8px;
  background-color: #e9ecef;
  border-radius: 4px;
  overflow: hidden;
  margin: 0 0.5rem;
}

.progress-fill {
  height: 100%;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  transition: width 0.3s ease;
}

.progress-text {
  font-size: 0.9rem;
  color: #667eea;
  font-weight: 500;
  min-width: 35px;
}

.project-actions {
  display: flex;
  gap: 0.75rem;
}

.btn-sm {
  padding: 0.5rem 1rem;
  font-size: 0.9rem;
}

.empty-state {
  text-align: center;
  padding: 4rem 2rem;
  color: #6c757d;
}

.empty-icon {
  font-size: 4rem;
  margin-bottom: 1.5rem;
}

.empty-state h3 {
  font-size: 1.5rem;
  margin-bottom: 1rem;
  color: #333;
}

.empty-state p {
  margin-bottom: 2rem;
  font-size: 1.1rem;
}

@media (max-width: 768px) {
  .page-header {
    flex-direction: column;
    gap: 1rem;
    align-items: stretch;
  }
  
  .projects-grid {
    grid-template-columns: 1fr;
  }
  
  .project-header {
    flex-direction: column;
    gap: 0.5rem;
  }
  
  .project-actions {
    flex-direction: column;
  }
}
</style>
