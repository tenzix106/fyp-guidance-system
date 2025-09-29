<template>
  <div class="home">
    <section class="hero">
      <div class="container">
        <div class="hero-content">
          <h1 class="hero-title">Welcome to FYP Guidance System</h1>
          <p class="hero-description">
            Your comprehensive platform for managing and tracking your Final Year Project journey.
            Get guidance, track progress, and achieve your academic goals.
          </p>
          <div class="hero-actions">
            <router-link to="/dashboard" class="btn">Get Started</router-link>
            <router-link to="/projects" class="btn btn-secondary">View Projects</router-link>
          </div>
        </div>
      </div>
    </section>

    <section class="features">
      <div class="container">
        <h2 class="section-title">Key Features</h2>
        <div class="features-grid">
          <div class="feature-card card">
            <div class="feature-icon">📊</div>
            <h3>Progress Tracking</h3>
            <p>Monitor your project milestones and deadlines with our intuitive dashboard.</p>
          </div>
          <div class="feature-card card">
            <div class="feature-icon">🎯</div>
            <h3>Goal Setting</h3>
            <p>Set and track your academic and project goals with personalized guidance.</p>
          </div>
          <div class="feature-card card">
            <div class="feature-icon">📚</div>
            <h3>Resource Library</h3>
            <p>Access a comprehensive library of resources, templates, and best practices.</p>
          </div>
          <div class="feature-card card">
            <div class="feature-icon">👥</div>
            <h3>Mentor Support</h3>
            <p>Connect with mentors and get personalized guidance throughout your journey.</p>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
export default {
  name: 'Home'
}
</script>

<style scoped>
.hero {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  padding: 4rem 0;
  text-align: center;
}

.hero-title {
  font-size: 3rem;
  font-weight: 700;
  margin-bottom: 1.5rem;
  line-height: 1.2;
}

.hero-description {
  font-size: 1.25rem;
  margin-bottom: 2.5rem;
  max-width: 600px;
  margin-left: auto;
  margin-right: auto;
  opacity: 0.9;
}

.hero-actions {
  display: flex;
  gap: 1rem;
  justify-content: center;
  flex-wrap: wrap;
}

.features {
  padding: 4rem 0;
  background: white;
}

.section-title {
  text-align: center;
  font-size: 2.5rem;
  margin-bottom: 3rem;
  color: #333;
}

.features-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 2rem;
}

.feature-card {
  text-align: center;
  padding: 2.5rem 2rem;
}

.feature-icon {
  font-size: 3rem;
  margin-bottom: 1.5rem;
}

.feature-card h3 {
  font-size: 1.5rem;
  margin-bottom: 1rem;
  color: #333;
}

.feature-card p {
  color: #6c757d;
  line-height: 1.6;
}

@media (max-width: 768px) {
  .hero-title {
    font-size: 2rem;
  }
  
  .hero-description {
    font-size: 1.1rem;
  }
  
  .hero-actions {
    flex-direction: column;
    align-items: center;
  }
}
</style>
