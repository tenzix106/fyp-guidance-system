# FYP Guidance System

A comprehensive Final Year Project guidance system built with Vue.js, Quasar Framework, and Flask.

## 🚀 Tech Stack

### Frontend
- **Vue.js 3** - Progressive JavaScript framework
- **Quasar Framework** - Vue.js based UI framework
- **Vite** - Fast build tool and development server
- **Axios** - HTTP client for API requests

### Backend
- **Flask** - Lightweight Python web framework
- **Flask-CORS** - Cross-Origin Resource Sharing support
- **Python 3.8+** - Programming language

## 📁 Project Structure

```
fyp-guidance-system/
├── src/                          # Frontend source code
│   ├── components/               # Vue components
│   │   └── EssentialLink.vue
│   ├── layouts/                  # Layout components
│   │   └── MainLayout.vue
│   ├── pages/                    # Page components
│   │   ├── IndexPage.vue
│   │   ├── Dashboard.vue
│   │   ├── Projects.vue
│   │   ├── Profile.vue
│   │   └── ErrorNotFound.vue
│   ├── router/                   # Vue Router configuration
│   │   ├── index.js
│   │   └── routes.js
│   ├── boot/                     # Quasar boot files
│   │   └── axios.js
│   ├── App.vue                   # Root Vue component
│   ├── main.js                   # Application entry point
│   └── quasar-variables.sass     # Quasar theme variables
├── backend/                      # Backend source code
│   ├── app.py                    # Flask application
│   ├── config.py                 # Configuration settings
│   └── requirements.txt          # Python dependencies
├── package.json                  # Node.js dependencies
├── quasar.config.js             # Quasar configuration
├── vite.config.js               # Vite configuration
└── README.md                    # This file
```

## 🛠️ Setup Instructions

### Prerequisites

- **Node.js** (v16 or higher)
- **Python** (v3.8 or higher)
- **npm** or **yarn** package manager

### Frontend Setup

1. **Install dependencies:**
   ```bash
   npm install
   ```

2. **Start development server:**
   ```bash
   npm run dev
   ```
   
   The frontend will be available at `http://localhost:8080`

### Backend Setup

1. **Navigate to backend directory:**
   ```bash
   cd backend
   ```

2. **Create virtual environment (recommended):**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Start Flask server:**
   ```bash
   python app.py
   ```
   
   The backend API will be available at `http://localhost:5000`

## 🚀 Running the Application

### Development Mode

1. **Start the backend server:**
   ```bash
   cd backend
   python app.py
   ```

2. **Start the frontend development server (in a new terminal):**
   ```bash
   npm run dev
   ```

3. **Open your browser and navigate to:**
   ```
   http://localhost:8080
   ```

### Production Build

1. **Build the frontend:**
   ```bash
   npm run build
   ```

2. **The built files will be in the `dist/` directory**

## 📚 API Endpoints

### Health Check
- `GET /api/health` - Check API health status

### Projects
- `GET /api/projects` - Get all projects
- `POST /api/projects` - Create a new project
- `GET /api/projects/{id}` - Get a specific project
- `PUT /api/projects/{id}` - Update a project
- `DELETE /api/projects/{id}` - Delete a project

### User Profile
- `GET /api/user/profile` - Get user profile
- `PUT /api/user/profile` - Update user profile

### Dashboard
- `GET /api/dashboard/stats` - Get dashboard statistics

## 🎨 Features

### Frontend Features
- **Responsive Design** - Works on desktop, tablet, and mobile
- **Modern UI** - Clean and intuitive interface using Quasar components
- **Navigation** - Sidebar navigation with multiple pages
- **Dashboard** - Overview of projects and statistics
- **Project Management** - Create, view, and manage projects
- **User Profile** - Profile management and settings

### Backend Features
- **RESTful API** - Well-structured API endpoints
- **CORS Support** - Cross-origin requests enabled
- **Error Handling** - Proper error responses
- **Data Validation** - Input validation and sanitization

## 🔧 Configuration

### Frontend Configuration
- **Quasar Config** - `quasar.config.js` for Quasar-specific settings
- **Vite Config** - `vite.config.js` for build and development settings
- **ESLint** - `.eslintrc.cjs` for code linting rules

### Backend Configuration
- **Flask Config** - `backend/config.py` for application settings
- **Environment Variables** - Use `.env` file for sensitive configuration

## 📦 Available Scripts

### Frontend Scripts
- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm run lint` - Run ESLint

### Backend Scripts
- `python app.py` - Start Flask development server

## 🚀 Deployment

### Frontend Deployment
1. Build the application: `npm run build`
2. Deploy the `dist/` folder to your web server

### Backend Deployment
1. Install production dependencies: `pip install -r requirements.txt`
2. Use a WSGI server like Gunicorn: `gunicorn -w 4 -b 0.0.0.0:5000 app:app`

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin feature-name`
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License.

## 🆘 Support

If you encounter any issues or have questions, please:
1. Check the documentation
2. Search existing issues
3. Create a new issue with detailed information

## 🔮 Future Enhancements

- [ ] User authentication and authorization
- [ ] Database integration (PostgreSQL/MongoDB)
- [ ] Real-time notifications
- [ ] File upload functionality
- [ ] Advanced project analytics
- [ ] Mobile app development
- [ ] Integration with external APIs
