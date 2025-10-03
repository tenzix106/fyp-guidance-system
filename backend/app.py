from flask import Flask, jsonify, request
from flask_cors import CORS
from datetime import datetime
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Sample data
projects = [
    {
        'id': 1,
        'title': 'E-Learning Platform',
        'description': 'A comprehensive online learning management system',
        'status': 'In Progress',
        'progress': 65,
        'created_at': '2024-01-15',
        'updated_at': '2024-01-20'
    },
    {
        'id': 2,
        'title': 'Mobile Health App',
        'description': 'Health monitoring and tracking application',
        'status': 'Planning',
        'progress': 20,
        'created_at': '2024-01-10',
        'updated_at': '2024-01-18'
    },
    {
        'id': 3,
        'title': 'IoT Smart Home System',
        'description': 'Internet of Things based home automation',
        'status': 'Completed',
        'progress': 100,
        'created_at': '2024-01-05',
        'updated_at': '2024-01-25'
    }
]

users = [
    {
        'id': 1,
        'name': 'John Doe',
        'email': 'john.doe@university.edu',
        'student_id': 'STU12345',
        'department': 'Computer Science',
        'role': 'Student'
    }
]

# API Routes
@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'message': 'FYP Guidance System API is running'
    })

@app.route('/api/projects', methods=['GET'])
def get_projects():
    return jsonify({
        'success': True,
        'data': projects,
        'count': len(projects)
    })

@app.route('/api/projects', methods=['POST'])
def create_project():
    data = request.get_json()
    
    if not data or not data.get('title') or not data.get('description'):
        return jsonify({
            'success': False,
            'message': 'Title and description are required'
        }), 400
    
    new_project = {
        'id': max([p['id'] for p in projects]) + 1 if projects else 1,
        'title': data['title'],
        'description': data['description'],
        'status': 'Planning',
        'progress': 0,
        'created_at': datetime.now().strftime('%Y-%m-%d'),
        'updated_at': datetime.now().strftime('%Y-%m-%d')
    }
    
    projects.append(new_project)
    
    return jsonify({
        'success': True,
        'data': new_project,
        'message': 'Project created successfully'
    }), 201

@app.route('/api/projects/<int:project_id>', methods=['GET'])
def get_project(project_id):
    project = next((p for p in projects if p['id'] == project_id), None)
    
    if not project:
        return jsonify({
            'success': False,
            'message': 'Project not found'
        }), 404
    
    return jsonify({
        'success': True,
        'data': project
    })

@app.route('/api/projects/<int:project_id>', methods=['PUT'])
def update_project(project_id):
    project = next((p for p in projects if p['id'] == project_id), None)
    
    if not project:
        return jsonify({
            'success': False,
            'message': 'Project not found'
        }), 404
    
    data = request.get_json()
    
    if 'title' in data:
        project['title'] = data['title']
    if 'description' in data:
        project['description'] = data['description']
    if 'status' in data:
        project['status'] = data['status']
    if 'progress' in data:
        project['progress'] = data['progress']
    
    project['updated_at'] = datetime.now().strftime('%Y-%m-%d')
    
    return jsonify({
        'success': True,
        'data': project,
        'message': 'Project updated successfully'
    })

@app.route('/api/projects/<int:project_id>', methods=['DELETE'])
def delete_project(project_id):
    global projects
    project = next((p for p in projects if p['id'] == project_id), None)
    
    if not project:
        return jsonify({
            'success': False,
            'message': 'Project not found'
        }), 404
    
    projects = [p for p in projects if p['id'] != project_id]
    
    return jsonify({
        'success': True,
        'message': 'Project deleted successfully'
    })

@app.route('/api/user/profile', methods=['GET'])
def get_user_profile():
    return jsonify({
        'success': True,
        'data': users[0] if users else None
    })

@app.route('/api/user/profile', methods=['PUT'])
def update_user_profile():
    data = request.get_json()
    
    if not users:
        return jsonify({
            'success': False,
            'message': 'User not found'
        }), 404
    
    user = users[0]
    
    if 'name' in data:
        user['name'] = data['name']
    if 'email' in data:
        user['email'] = data['email']
    if 'student_id' in data:
        user['student_id'] = data['student_id']
    if 'department' in data:
        user['department'] = data['department']
    
    return jsonify({
        'success': True,
        'data': user,
        'message': 'Profile updated successfully'
    })

@app.route('/api/dashboard/stats', methods=['GET'])
def get_dashboard_stats():
    active_projects = len([p for p in projects if p['status'] == 'In Progress'])
    completed_projects = len([p for p in projects if p['status'] == 'Completed'])
    total_progress = sum(p['progress'] for p in projects) / len(projects) if projects else 0
    
    return jsonify({
        'success': True,
        'data': {
            'active_projects': active_projects,
            'completed_projects': completed_projects,
            'total_projects': len(projects),
            'average_progress': round(total_progress, 1)
        }
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_ENV') == 'development'
    
    print(f"Starting Flask server on port {port}")
    print(f"Debug mode: {debug}")
    
    app.run(host='0.0.0.0', port=port, debug=debug)
