<template>
  <div class="dashboard">
    <div class="container">
      <h1 class="page-title">Dashboard</h1>
      
      <div class="dashboard-grid">
        <div class="stats-section">
          <div class="stat-card card">
            <h3>Project Progress</h3>
            <div class="progress-circle">
              <div class="progress-value">75%</div>
            </div>
            <p class="stat-description">Overall completion</p>
          </div>
          
          <div class="stat-card card">
            <h3>Deadlines</h3>
            <div class="deadline-count">3</div>
            <p class="stat-description">Upcoming deadlines</p>
          </div>
          
          <div class="stat-card card">
            <h3>Milestones</h3>
            <div class="milestone-count">8/12</div>
            <p class="stat-description">Completed milestones</p>
          </div>
        </div>
        
        <div class="recent-activity card">
          <h3>Recent Activity</h3>
          <div class="activity-list">
            <div class="activity-item">
              <div class="activity-icon">✅</div>
              <div class="activity-content">
                <p><strong>Literature Review</strong> completed</p>
                <span class="activity-time">2 hours ago</span>
              </div>
            </div>
            <div class="activity-item">
              <div class="activity-icon">📝</div>
              <div class="activity-content">
                <p><strong>Methodology</strong> section updated</p>
                <span class="activity-time">1 day ago</span>
              </div>
            </div>
            <div class="activity-item">
              <div class="activity-icon">📊</div>
              <div class="activity-content">
                <p><strong>Data Collection</strong> phase started</p>
                <span class="activity-time">3 days ago</span>
              </div>
            </div>
          </div>
        </div>
        
        <div class="upcoming-tasks card">
          <h3>Upcoming Tasks</h3>
          <div class="task-list">
            <div class="task-item">
              <input type="checkbox" id="task1">
              <label for="task1">Complete data analysis</label>
              <span class="task-due">Due: Dec 15</span>
            </div>
            <div class="task-item">
              <input type="checkbox" id="task2">
              <label for="task2">Write results section</label>
              <span class="task-due">Due: Dec 20</span>
            </div>
            <div class="task-item">
              <input type="checkbox" id="task3">
              <label for="task3">Prepare presentation</label>
              <span class="task-due">Due: Dec 25</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Dashboard'
}
</script>

<style scoped>
.dashboard {
  padding: 2rem 0;
}

.page-title {
  font-size: 2.5rem;
  margin-bottom: 2rem;
  color: #333;
  text-align: center;
}

.dashboard-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 2rem;
}

.stats-section {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1.5rem;
}

.stat-card {
  text-align: center;
  padding: 2rem;
}

.stat-card h3 {
  margin-bottom: 1.5rem;
  color: #333;
}

.progress-circle {
  width: 100px;
  height: 100px;
  border-radius: 50%;
  background: conic-gradient(#667eea 0deg 270deg, #e9ecef 270deg 360deg);
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 0 auto 1rem;
  position: relative;
}

.progress-circle::before {
  content: '';
  width: 80px;
  height: 80px;
  border-radius: 50%;
  background: white;
  position: absolute;
}

.progress-value {
  font-size: 1.5rem;
  font-weight: bold;
  color: #667eea;
  z-index: 1;
}

.deadline-count,
.milestone-count {
  font-size: 3rem;
  font-weight: bold;
  color: #667eea;
  margin-bottom: 1rem;
}

.stat-description {
  color: #6c757d;
  font-size: 0.9rem;
}

.recent-activity,
.upcoming-tasks {
  grid-column: span 2;
}

.activity-list,
.task-list {
  margin-top: 1.5rem;
}

.activity-item,
.task-item {
  display: flex;
  align-items: center;
  padding: 1rem 0;
  border-bottom: 1px solid #e9ecef;
}

.activity-item:last-child,
.task-item:last-child {
  border-bottom: none;
}

.activity-icon {
  font-size: 1.5rem;
  margin-right: 1rem;
  width: 40px;
  text-align: center;
}

.activity-content {
  flex: 1;
}

.activity-content p {
  margin: 0;
  color: #333;
}

.activity-time {
  font-size: 0.9rem;
  color: #6c757d;
}

.task-item {
  gap: 1rem;
}

.task-item input[type="checkbox"] {
  width: 18px;
  height: 18px;
  accent-color: #667eea;
}

.task-item label {
  flex: 1;
  color: #333;
  cursor: pointer;
}

.task-due {
  font-size: 0.9rem;
  color: #6c757d;
  background: #f8f9fa;
  padding: 0.25rem 0.5rem;
  border-radius: 4px;
}

@media (max-width: 768px) {
  .dashboard-grid {
    grid-template-columns: 1fr;
  }
  
  .recent-activity,
  .upcoming-tasks {
    grid-column: span 1;
  }
  
  .stats-section {
    grid-template-columns: 1fr;
  }
}
</style>
