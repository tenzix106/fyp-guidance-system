#!/bin/bash

echo "Starting FYP Guidance System Development Environment"
echo

echo "Starting Flask Backend Server..."
cd backend
python app.py &
BACKEND_PID=$!

echo "Waiting for backend to start..."
sleep 3

echo "Starting Vue.js Frontend Server..."
cd ..
npm run dev &
FRONTEND_PID=$!

echo
echo "Both servers are starting up..."
echo "Backend: http://localhost:5000"
echo "Frontend: http://localhost:8080"
echo
echo "Press Ctrl+C to stop both servers"

# Function to cleanup processes on exit
cleanup() {
    echo "Stopping servers..."
    kill $BACKEND_PID 2>/dev/null
    kill $FRONTEND_PID 2>/dev/null
    exit
}

# Trap Ctrl+C
trap cleanup INT

# Wait for processes
wait
