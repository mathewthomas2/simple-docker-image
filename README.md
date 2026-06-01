# Simple Docker Web App 🐳
A simple Python Flask web application containerized with Docker. This project demonstrates how to build a Docker image, run a container, and understand port mapping.
---
## 📁 Project Structure
```
simple-docker-image/
├── app.py           # Flask web application with multiple routes
├── Dockerfile       # Instructions to build the Docker image
└── README.md        # Documentation
```
---
## 📋 Steps to Create and Run the Docker Image
### Step 1 — Clone the Repository
```bash
git clone https://github.com/mathewthomas2/simple-docker-image.git
cd simple-docker-image
```
### Step 2 — Build the Docker Image
```bash
docker build -t simple-docker-image .
```
What each part means:
- `docker build` — Tells Docker to build an image from a Dockerfile
- `-t simple-docker-image` — Names the image `simple-docker-image`
- `.` — Tells Docker to look for the Dockerfile in the current directory
### Step 3 — Run the Container
```bash
docker run -p 80:8080 simple-docker-image
```
### Step 4 — Access the App
Open your browser and visit `http://localhost`
---
## 🔗 App Routes and Outputs
- **/** → `Hey! I am Mathew. This is my first Docker app!`
- **/age** → `I'd rather not say!`
- **/hobby** → `I love learning DevOps and breaking things in Kubernetes.`
- **/stack** → `Python, Docker, Kubernetes, Linux`
---

