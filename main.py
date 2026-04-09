import cv2
from ultralytics import YOLO

# Model load (nano version is fast)
model = YOLO('yolov8n.pt') 

cap = cv2.VideoCapture("traffic.mp4")

# Line ki position video ke bottom ke paas (Screen ke 70-80% niche)
# Is video ke liye 450-500 ki range sahi rahegi
line_y = 480 
vehicle_count = 0
offset = 7 # Thoda buffer taaki fast gadiyan miss na hon
already_counted = [] # Taaki ek hi gadi bar bar count na ho

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Frame ko standard size mein resize kar lo testing ke liye
    frame = cv2.resize(frame, (1020, 600))

    # YOLO Detection (Car, Motorcycle, Bus, Truck)
    results = model(frame, classes=[2, 3, 5, 7], conf=0.4) 
    
    # Red Line draw karo (Detection Zone)
    cv2.line(frame, (50, line_y), (970, line_y), (0, 0, 255), 3)

    for result in results[0].boxes:
        x1, y1, x2, y2 = map(int, result.xyxy[0])
        cx = int((x1 + x2) / 2) # Center X
        cy = int((y1 + y2) / 2) # Center Y

        # Gadi ka center point
        cv2.circle(frame, (cx, cy), 4, (0, 255, 255), -1)

        # Logic: Agar car ka center line ke range mein hai
        if cy < (line_y + offset) and cy > (line_y - offset):
            # Yahan hum simplified count kar rahe hain
            vehicle_count += 1
            # Color change for feedback
            cv2.line(frame, (50, line_y), (970, line_y), (0, 255, 0), 3)

    # Dynamic Timer Logic
    # Jitni zyada gadiyan cross hongi, timer badhta jayega
    green_time = 10 + (vehicle_count // 2) # Har 2 gadi par 1 sec extra
    if green_time > 60: green_time = 60 # Max limit 1 min

    # Dashboard display
    cv2.rectangle(frame, (10, 10), (350, 120), (0, 0, 0), -1) # Black background for text
    cv2.putText(frame, f"VEHICLES DETECTED: {vehicle_count}", (20, 50), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
    cv2.putText(frame, f"OPTIMIZED TIMER: {green_time}s", (20, 90), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2)

    cv2.imshow("Shankara Hackathon - Traffic AI", frame)
    
    # Wait for 1 millisecond and check if ESC (27) or 'q' is pressed
    key = cv2.waitKey(1) & 0xFF
    if key == 27 or key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()