# Simple Docker Web App 🐳
A simple Python Flask web application containerized with Docker.
---
## 📋 Steps to Create and Run the Docker Image
### Step 1 — Create the Project Files
Create two files in a folder:
- `app.py` — The Python web application
- `Dockerfile` — Instructions for Docker to build the image
### Step 2 — Build the Docker Image
```bash
docker build -t simple-docker-image .
```
- `docker build` — Tells Docker to build an image
- `-t simple-docker-image` — Gives the image a name (tag)
- `.` — Look for the Dockerfile in the current directory
### Step 3 — Run the Container
```bash
docker run -p 80:8080 simple-docker-image
```
### Step 4 — Open in Browser
Visit the links below to see different outputs.
---
## 🔗 App Routes and Outputs
|
 URL 
|
 Output 
|
|
-----
|
--------
|
|
[
http://localhost/
](
http://localhost/
)
|
`Hey! I am Mathew. This is my first Docker app!`
|
|
[
http://localhost/age
](
http://localhost/age
)
|
`I'd rather not say!`
|
|
[
http://localhost/hobby
](
http://localhost/hobby
)
|
`I love learning DevOps and breaking things in Kubernetes.`
|
|
[
http://localhost/stack
](
http://localhost/stack
)
|
`Python, Docker, Kubernetes, Linux`
|
Each URL after `/` is called a **route**. Every route is defined in `app.py` using `@app.route()` and returns a different message.
---
## 🔌 Port Mapping Explained
When running the container, we use:
```bash
docker run -p 80:8080 simple-docker-image
```
The `-p 80:8080` part is **port mapping**. Here's what it means:
```
-p  HOST_PORT : CONTAINER_PORT
-p     80     :     8080
```
|
 Term 
|
 Meaning 
|
|
------
|
---------
|
|
**
Container Port (8080)
**
|
 The port the Flask app is running on 
**
inside
**
 the container. This is set in 
`app.py`
 with 
`port=8080`
. 
|
|
**
Host Port (80)
**
|
 The port on 
**
your machine
**
 that you use to access the app in the browser. 
|
|
**
Port Mapping
**
|
 Connects the two — when you visit port 80 on your machine, Docker forwards the traffic to port 8080 inside the container. 
|
### How it works:
```
You (Browser)                    Docker Container
      |                                |
      |   Visit http://localhost:80    |
      | -----------------------------> |
      |                                |  Forwards to port 8080
      |                                |  Flask app receives request
      |                                |  Sends back response
      | <----------------------------- |
      |   "Hey! I am Mathew..."        |
```
### Examples of different port mappings:
|
 Command 
|
 How to access 
|
|
---------
|
--------------
|
|
`docker run -p 80:8080`
|
 
`http://localhost`
 (port 80 is the default for browsers) 
|
|
`docker run -p 8080:8080`
|
 
`http://localhost:8080`
|
|
`docker run -p 3000:8080`
|
 
`http://localhost:3000`
|
|
`docker run -p 9090:8080`
|
`http://localhost:9090`
|
> **Note:** The container port (right side) always stays **8080** because that's what the app uses. Only the host port (left side) changes based on where you want to access it.
---
