# 🎵 MOODIFY - Emotion-Based Music Recommender

Welcome to **Moodify** — a fun and powerful web application that detects your mood using facial expressions and recommends Spotify playlists that match your emotion.

Made with ❤️ by **Anandhu M S**, **Hemendra Patel**, and **Bhati Akshraj Sinh**.

---

## 🌟 Features

- 🎭 Real-time Emotion Detection via webcam
- 🤖 DeepFace-based facial analysis using AI
- 🎧 Instant Spotify Playlist Recommendations
- ⚡ Smooth UI with manual mood selection as fallback

---

## 📸 How It Works

1. Open the app in your browser.
2. Click **"Detect My Mood"** to use webcam-based emotion recognition.
3. Alternatively, type your mood manually (happy, sad, angry, etc.).
4. Get a direct link to a curated **Spotify playlist** matching your emotion!

---

## 💻 Tech Stack

| Layer     | Tools/Libraries                                 |
|-----------|--------------------------------------------------|
| Backend   | Python, Flask                                   |
| AI Model  | [DeepFace](https://github.com/serengil/deepface) |
| Face Input | MTCNN                                          |
| Frontend  | HTML, CSS, JS (with Poppins font & gradient UI) |
| Music API | Spotify (public playlist links)                 |

---

## 📂 Dataset Used

### FER-2013 (Facial Expression Recognition)

- **Source**: [Kaggle - FER 2013](https://www.kaggle.com/datasets/msambare/fer2013)
- **Description**: A publicly available dataset containing 35,887 grayscale images (48x48 pixels) of faces classified into 7 emotions: `Angry`, `Disgust`, `Fear`, `Happy`, `Sad`, `Surprise`, and `Neutral`.
- **Usage in Moodify**: The dataset was used for testing, model evaluation, and customizing mood detection features for better performance.

---

## 📦 Installation

### 🛠 Requirements

- Python 3.7 or above
- pip
- Webcam

### 🔧 Setup

```bash
# Clone the repository
git clone https://github.com/K1NGzM4N/MOODIFY.git
cd MOODIFY

# Install required Python packages
pip install -r requirements.txt
🎶 Supported Emotions

Emotion	Spotify Playlist
Happy	Playlist
Sad	Playlist
Angry	Playlist
Surprise	Playlist
Fear	Playlist
Disgust	Playlist
Neutral	Playlist
👨‍💻 Team
Anandhu M S

Hemendra Patel

Bhati Akshraj Sinh

📜 License
This project is open-source and available under the MIT License.

🙌 Acknowledgements
DeepFace

Spotify

FER-2013 Dataset

🌐 Website
https://moodify-yb7c.onrender.com

Music connects hearts, heals minds, and fuels moments. Let MOODIFY match your vibes 🎧
