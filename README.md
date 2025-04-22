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
| Face Input | OpenCV                                          |
| Frontend  | HTML, CSS, JS (with Poppins font & gradient UI) |
| Music API | Spotify (public playlist links)                 |

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
```

**`requirements.txt`**
```txt
flask
opencv-python
deepface
```

### 🚀 Run the App

```bash
python app.py
```

Visit `http://127.0.0.1:5000` in your browser.

---

## 🎶 Supported Emotions

| Emotion   | Spotify Playlist |
|-----------|------------------|
| Happy     | [Playlist](https://open.spotify.com/playlist/37i9dQZF1DXdPec7aLTmlC) |
| Sad       | [Playlist](https://open.spotify.com/playlist/37i9dQZF1DX7qK8ma5wgG1) |
| Angry     | [Playlist](https://open.spotify.com/playlist/37i9dQZF1DWYxwmBaMqxsl) |
| Surprise  | [Playlist](https://open.spotify.com/playlist/37i9dQZF1DWTfrr8pte1rT) |
| Fear      | [Playlist](https://open.spotify.com/playlist/37i9dQZF1DX4sWSpwq3LiO) |
| Disgust   | [Playlist](https://open.spotify.com/playlist/37i9dQZF1DX7gtIfGVzmkY) |
| Neutral   | [Playlist](https://open.spotify.com/playlist/37i9dQZF1DX4WYpdgoIcn6) |

---

## 👨‍💻 Team

- **Anandhu M S**  
- **Hemendra Patel**  
- **Bhati Akshraj Sinh**

---

## 📜 License

This project is open-source and available under the [MIT License](LICENSE).

---

## 🙌 Acknowledgements

- [DeepFace](https://github.com/serengil/deepface)
- [Spotify](https://spotify.com)

---

> Music connects hearts, heals minds, and fuels moments. Let MOODIFY match your vibes 🎧
