Video Frame Preprocessing Script

This project provides a Python script that extracts frames from video files at a reduced frame rate, resizes them to a consistent resolution, and saves them as PNG images. It is useful for dataset creation, preprocessing for machine learning, and time-based analysis.

📌 Features

Select between morning, day, or evening video sources.

Extract frames at 1 FPS (or your chosen target FPS).

Automatically resizes frames to 640 × 640.

Saves frames with sequential filenames.

Organizes output frames into separate folders based on time of day.

📂 Project Structure
project/
│
├── originalData/
│   ├── Jam pagi.mp4
│   ├── Jam siang.mp4
│   └── Jam malam.mp4
│
├── processedPictures/
│   ├── morning/
│   ├── day/
│   └── evening/
│
└── preprocess.py   # (your script)


Make sure the folders above exist before running the script.
If they don’t, create them manually.

🔧 Requirements

Install Python 3.8+ and the required libraries:

pip install opencv-python numpy

▶️ How to Run

Place your video files inside the originalData/ folder.

Run the script:

python preprocess.py


When prompted, enter:

0 → For morning video
1 → For daytime video
2 → For nighttime video


Example:

Select which file to preprocess: 0 is morning, 1 is daytime, 2 is nighttime 1

📤 Output

Frames will be saved as PNG images in:

Input Choice	Output Folder	Example Filename
0 (morning)	processedPictures/morning/	cv2_morning_frame_0001.png
1 (daytime)	processedPictures/day/	cv2_day_frame_0001.png
2 (night)	processedPictures/evening/	cv2_evening_frame_0001.png

Every frame is:

Resized to 640 × 640

Extracted at 1 FPS

Saved with maximum PNG compression

🛠️ How It Works (Brief Explanation)

The script reads the chosen video using cv2.VideoCapture.

It calculates how many frames to skip based on the original FPS.

Every Nth frame is resized and saved.

Processing continues until the video ends.

✔️ Example Terminal Output
Processing video at 29.97 FPS. Outputting frames at 1/30 rate.
Saved 100 frames...
Saved 200 frames...
Saved 300 frames...

Processing complete.
Total frames saved: 328

📄 Notes

If OpenCV cannot detect the video’s FPS, it defaults to 30 FPS.

PNG compression level is set to 9 (highest compression, smallest file).

Make sure output directories exist, or OpenCV may fail to write files.
