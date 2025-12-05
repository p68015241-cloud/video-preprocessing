import cv2
import numpy as np

INPUT_FILE = "../originalData/Jam pagi.mp4"
OUTPUT_FILENAME_FORMAT = "./processedPictures/cv2_frame_%04d.png"
TARGET_SIZE = (640, 640)
TARGET_FPS = 1

cap = cv2.VideoCapture(INPUT_FILE)
if not cap.isOpened():
    print(f"Error: Could not open video file {INPUT_FILE}")
    exit()

original_fps = cap.get(cv2.CAP_PROP_FPS)
if original_fps == 0:
    original_fps = 30 
frame_skip_interval = int(round(original_fps / TARGET_FPS))

frame_count = 0
output_frame_index = 0

print(f"Processing video at {original_fps:.2f} FPS. Outputting frames at 1/{frame_skip_interval} rate.")

while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        break

    if frame_count % frame_skip_interval == 0:
        stretched_frame = cv2.resize(
            frame,
            TARGET_SIZE,
            interpolation=cv2.INTER_LINEAR  # Standard interpolation method
        )

        output_filename = OUTPUT_FILENAME_FORMAT % (output_frame_index + 1)
        
        cv2.imwrite(output_filename, stretched_frame, [cv2.IMWRITE_PNG_COMPRESSION, 9])
        
        output_frame_index += 1
        
        if output_frame_index % 100 == 0:
            print(f"Saved {output_frame_index} frames...")

    frame_count += 1

cap.release()
print("\nProcessing complete.")
print(f"Total frames saved: {output_frame_index}")