# FYP Guidance System

A comprehensive Vue.js application designed to help students manage and track their Final Year Project (FYP) journey. This system provides project management, progress tracking, and academic guidance features.

## 🚀 Features

- **Dashboard**: Overview of project progress, deadlines, and recent activity
- **Project Management**: Create, track, and manage multiple FYP projects
- **Progress Tracking**: Visual progress indicators and milestone tracking
- **Profile Management**: Student profile with academic information and preferences
- **Responsive Design**: Modern, mobile-friendly interface
- **Vue 3 Composition API**: Built with the latest Vue.js features

## 🛠️ Tech Stack

- **Frontend**: Vue.js 3 with Composition API
- **Build Tool**: Vite
- **Routing**: Vue Router 4
- **State Management**: Pinia
- **HTTP Client**: Axios
- **Styling**: CSS3 with modern features
- **Linting**: ESLint with Vue.js rules

## 📋 Prerequisites

Before you begin, ensure you have the following installed:
- Node.js (version 16 or higher)
- npm or yarn package manager

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone <repository-url>
cd fyp-guidance-system
```

### 2. Install dependencies
```bash
npm install
# or
yarn install
```

### 3. Start the development server
```bash
npm run dev
# or
yarn dev
```

The application will be available at `http://localhost:3000`

### 4. Build for production
```bash
npm run build
# or
yarn build
```

### 5. Preview production build
```bash
npm run preview
# or
yarn preview
```

## 📁 Project Structure

```
fyp-guidance-system/
├── public/                 # Static assets
├── src/
│   ├── components/         # Reusable Vue components
│   ├── views/             # Page components
│   │   ├── Home.vue       # Landing page
│   │   ├── Dashboard.vue  # Main dashboard
│   │   ├── Projects.vue   # Project management
│   │   └── Profile.vue    # User profile
│   ├── stores/            # Pinia stores
│   ├── router/            # Vue Router configuration
│   ├── assets/            # Images, fonts, etc.
│   ├── App.vue            # Root component
│   ├── main.js            # Application entry point
│   └── style.css          # Global styles
├── index.html             # HTML template
├── package.json           # Dependencies and scripts
├── vite.config.js         # Vite configuration
└── README.md              # Project documentation
```

## 🎨 Customization

### Adding New Pages
1. Create a new Vue component in `src/views/`
2. Add the route in `src/main.js`
3. Update the navigation in `src/App.vue`

### Styling
- Global styles are in `src/style.css`
- Component-specific styles use scoped CSS
- The design system uses CSS custom properties for consistent theming

### State Management
- Pinia stores are located in `src/stores/`
- Create new stores for different data domains

## 🔧 Available Scripts

- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm run preview` - Preview production build
- `npm run lint` - Run ESLint

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support

If you encounter any issues or have questions, please:
1. Check the existing issues on GitHub
2. Create a new issue with detailed information
3. Contact the development team

## 🎯 Roadmap

- [ ] User authentication and authorization
- [ ] Real-time notifications
- [ ] File upload and management
- [ ] Advanced project templates
- [ ] Integration with external APIs
- [ ] Mobile app version
- [ ] Advanced analytics and reporting

---

**Happy Coding! 🎉**
