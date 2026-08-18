# 👤 Real-Time Face Recognition

A real-time face recognition system built with Python, using a webcam feed to detect and identify known faces on the fly.

## 🧠 How It Works

1. The script loads reference images from the `knowns/` folder — each filename becomes the person's label (e.g. `steve_jobs.jpg` → "steve_jobs").
2. Face encodings are generated for each known image using the `face_recognition` library (built on `dlib`).
3. The webcam feed is captured with OpenCV, and every frame is scanned for faces.
4. Each detected face is compared against the known encodings using Euclidean distance; the closest match is labeled, otherwise the face is marked as `UNKNOWN`.
5. Bounding boxes and names are drawn live on the video feed.

## 🛠️ Tech Stack

- **Python 3**
- **face_recognition** — face detection & encoding (built on dlib)
- **OpenCV (cv2)** — video capture & rendering
- **NumPy** — distance calculations

## 📦 Installation

\`\`\`bash
git clone https://github.com/HADi-Shahrivary/face-recognition.git
cd face-recognition
pip install -r requirements.txt
\`\`\`

> **Note:** `dlib` (a dependency of `face_recognition`) can be tricky to install on some systems.
> - **Windows:** install CMake and Visual Studio Build Tools first.
> - **Linux/Mac:** `sudo apt install cmake` (or `brew install cmake` on Mac) before running `pip install`.

## 📁 Project Structure

\`\`\`
face-recognition/
├── main.py              # Main script
├── requirements.txt      # Dependencies
├── knowns/               # Reference images (one clear face per file)
│   ├── steve_jobs.jpg
│   └── ...
└── README.md
\`\`\`

## ▶️ Usage

1. Add one or more clear, front-facing photos to the `knowns/` folder. Name each file after the person (this becomes their label).
2. Run the script:

\`\`\`bash
python main.py
\`\`\`

3. A webcam window will open. Recognized faces are boxed and labeled with their name; unrecognized faces are labeled `UNKNOWN`.
4. Press **ESC** to quit.


## ⚠️ Notes

- The reference photos used in this demo are public images of well-known public figures (e.g. Steve Jobs), used purely for demonstration purposes.
- This project is for educational/portfolio purposes and is not optimized for production-grade security or large-scale deployment.

## 🚀 Possible Improvements

- [ ] Support recognition from static images/video files, not just webcam
- [ ] Add a simple GUI (e.g. with Tkinter or Streamlit)
- [ ] Improve performance with face detection model selection (`hog` vs `cnn`)
- [ ] Store encodings in a database instead of recomputing on every run

## 📄 License

This project is open-source and available under the MIT License.
