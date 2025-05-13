from ultralytics import YOLO
import cv2
import json

# === CONFIGURATION ===
image_path = "scene_step0.png"  # output figure path
pose_path = "pose_step0.json"  # pose JSON path
output_path = "semantic_map_step0.json"  # fina output path

# === LOAD POSE ===
with open(pose_path, "r") as f:
    pose_data = json.load(f)

# === RUN YOLO DETECTION ===
model = YOLO("yolov8n.pt")  # YOLOv8 model
results = model(image_path)

vision = []
for r in results:
    for box in r.boxes:
        cls_id = int(box.cls[0])
        cls_name = model.names[cls_id]
        conf = float(box.conf[0])
        xyxy = box.xyxy[0].tolist()
        vision.append({
            "type": cls_name,
            "bbox": [round(c, 2) for c in xyxy],
            "confidence": round(conf, 2)
        })

# === COMBINE STRUCTURE ===
final_data = {
    "agent": pose_data,
    "vision": vision
}

# === EXPORT TO JSON ===
with open(output_path, "w") as f:
    json.dump(final_data, f, indent=2)

print(f"[✓] Semantic map saved to: {output_path}")