# AI-Powered Traffic Timer Optimization 🚦🤖

### **Project Overview**
This project was developed during the **Shankara Hackathon** to solve the problem of urban traffic congestion. Unlike traditional static timers, this system uses **Computer Vision** to proactively adjust traffic signal timings based on real-time vehicle density.

### **The "1 KM Strategy"**
The core idea is to place cameras **500m to 1km ahead** of the intersection. This allows the system to:
* **Predict Arrival:** Calculate the incoming traffic volume before it reaches the signal.
* **Proactive Timing:** Adjust the green light duration in advance to maintain a smooth flow (Green Wave).

### **Key Features**
* **Object Detection:** Powered by **YOLOv8** for high-speed vehicle identification.
* **Virtual Induction Loops:** A digital detection line counts vehicles crossing into the priority zone.
* **Dynamic Logic:** Real-time calculation of Green Light duration ($T_{green}$) based on live counts.

### **Tech Stack**
* **Language:** Python
* **AI Model:** YOLOv8 (Ultralytics)
* **Computer Vision:** OpenCV
* **Data Processing:** NumPy

### **How to Run**
1. Clone this repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
