<template>
  <div class="profile">
    <div class="container">
      <h1 class="page-title">Profile</h1>
      
      <div class="profile-content">
        <div class="profile-card card">
          <div class="profile-header">
            <div class="profile-avatar">
              <img src="https://via.placeholder.com/120x120/667eea/ffffff?text=JD" alt="Profile Avatar" />
            </div>
            <div class="profile-info">
              <h2 class="profile-name">John Doe</h2>
              <p class="profile-role">Computer Science Student</p>
              <p class="profile-email">john.doe@university.edu</p>
            </div>
            <button class="btn btn-secondary">Edit Profile</button>
          </div>
        </div>
        
        <div class="profile-details">
          <div class="detail-section card">
            <h3>Academic Information</h3>
            <div class="detail-grid">
              <div class="detail-item">
                <label>Student ID</label>
                <span>CS2024001</span>
              </div>
              <div class="detail-item">
                <label>Program</label>
                <span>Bachelor of Computer Science</span>
              </div>
              <div class="detail-item">
                <label>Year</label>
                <span>Final Year</span>
              </div>
              <div class="detail-item">
                <label>GPA</label>
                <span>3.8/4.0</span>
              </div>
            </div>
          </div>
          
          <div class="detail-section card">
            <h3>Project Preferences</h3>
            <div class="preferences-list">
              <div class="preference-item">
                <span class="preference-label">Preferred Technology Stack</span>
                <div class="preference-tags">
                  <span class="tag">Vue.js</span>
                  <span class="tag">Node.js</span>
                  <span class="tag">MongoDB</span>
                  <span class="tag">Python</span>
                </div>
              </div>
              <div class="preference-item">
                <span class="preference-label">Project Type</span>
                <div class="preference-tags">
                  <span class="tag">Web Application</span>
                  <span class="tag">Machine Learning</span>
                </div>
              </div>
              <div class="preference-item">
                <span class="preference-label">Supervisor</span>
                <span class="preference-value">Dr. Sarah Johnson</span>
              </div>
            </div>
          </div>
          
          <div class="detail-section card">
            <h3>Recent Achievements</h3>
            <div class="achievements-list">
              <div class="achievement-item">
                <div class="achievement-icon">🏆</div>
                <div class="achievement-content">
                  <h4>Best Project Proposal</h4>
                  <p>Won the best project proposal award for Q3 2024</p>
                  <span class="achievement-date">October 2024</span>
                </div>
              </div>
              <div class="achievement-item">
                <div class="achievement-icon">📚</div>
                <div class="achievement-content">
                  <h4>Research Paper Published</h4>
                  <p>Published paper on "AI in Education" in IEEE Conference</p>
                  <span class="achievement-date">September 2024</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Profile'
}
</script>

<style scoped>
.profile {
  padding: 2rem 0;
}

.page-title {
  font-size: 2.5rem;
  margin-bottom: 2rem;
  color: #333;
  text-align: center;
}

.profile-content {
  max-width: 800px;
  margin: 0 auto;
}

.profile-card {
  margin-bottom: 2rem;
}

.profile-header {
  display: flex;
  align-items: center;
  gap: 2rem;
}

.profile-avatar img {
  width: 120px;
  height: 120px;
  border-radius: 50%;
  object-fit: cover;
  border: 4px solid #667eea;
}

.profile-info {
  flex: 1;
}

.profile-name {
  font-size: 2rem;
  margin-bottom: 0.5rem;
  color: #333;
}

.profile-role {
  font-size: 1.1rem;
  color: #667eea;
  margin-bottom: 0.25rem;
  font-weight: 500;
}

.profile-email {
  color: #6c757d;
  margin: 0;
}

.detail-section {
  margin-bottom: 2rem;
}

.detail-section h3 {
  margin-bottom: 1.5rem;
  color: #333;
  font-size: 1.5rem;
}

.detail-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1.5rem;
}

.detail-item {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.detail-item label {
  font-weight: 500;
  color: #495057;
  font-size: 0.9rem;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.detail-item span {
  color: #333;
  font-size: 1.1rem;
}

.preferences-list {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.preference-item {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}

.preference-label {
  font-weight: 500;
  color: #495057;
}

.preference-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
}

.tag {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  padding: 0.25rem 0.75rem;
  border-radius: 20px;
  font-size: 0.8rem;
  font-weight: 500;
}

.preference-value {
  color: #333;
  font-size: 1.1rem;
}

.achievements-list {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.achievement-item {
  display: flex;
  align-items: flex-start;
  gap: 1rem;
  padding: 1rem;
  background: #f8f9fa;
  border-radius: 8px;
  border-left: 4px solid #667eea;
}

.achievement-icon {
  font-size: 2rem;
  flex-shrink: 0;
}

.achievement-content h4 {
  margin: 0 0 0.5rem 0;
  color: #333;
  font-size: 1.1rem;
}

.achievement-content p {
  margin: 0 0 0.5rem 0;
  color: #6c757d;
  line-height: 1.5;
}

.achievement-date {
  font-size: 0.9rem;
  color: #667eea;
  font-weight: 500;
}

@media (max-width: 768px) {
  .profile-header {
    flex-direction: column;
    text-align: center;
    gap: 1rem;
  }
  
  .detail-grid {
    grid-template-columns: 1fr;
  }
  
  .achievement-item {
    flex-direction: column;
    text-align: center;
  }
}
</style>
