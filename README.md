SYS_TODO_LIST.EXE

CSC 330 Midterm Assessment

This is a small web application built using Python and Flask. It serves as a fully functional To-Do List but features a highly innovative, retro-cyberpunk aesthetic. The frontend utilizes a pixelated 8-bit font, neon terminal colors, and a custom CSS CRT scanline effect to simulate the look of a vintage arcade machine or retro computer terminal.

🚀 Features

Retro UI/UX: Custom CSS styling featuring a glowing green interface on a deep black background (#050505), complete with blinking cursors and glitch-inspired text shadows.

Task Management: Users can easily enter new "directives" (tasks) and delete them once completed using the [X] button.

Immersive Effects: A CSS-based CRT scanline overlay creates an authentic vintage monitor feel.

Standard Flask Architecture: Follows standard directory structure (app.py in the root, and HTML templates inside the templates/ folder).

🛠️ Technical Specifications (Assessment Requirements)

This project strictly adheres to the CSC 330 Midterm Assessment server configuration requirements:

Host: 0.0.0.0 (Ensures the application is reachable externally from the GCP Virtual Machine).

Port: 8080

Run Command: python3 app.py

💻 Installation & Deployment (GCP VM)

Clone or copy the files into your Google Cloud Platform (GCP) Virtual Machine.

Ensure directory structure is correct:

project_folder/
├── app.py
├── README.md
└── templates/
    └── index.html


Install Flask if you haven't already:

sudo apt update
sudo apt install python3-pip
pip3 install flask


Run the server:

python3 app.py


Access the application: Open your web browser and navigate to http://<YOUR_GCP_VM_EXTERNAL_IP>:8080.
(Note: Ensure your GCP Firewall rules allow TCP traffic on port 8080).

Created for the CSC 330 Midterm Assessment.