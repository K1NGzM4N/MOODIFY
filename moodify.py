from flask import Flask, render_template_string, jsonify, request
import cv2
from deepface import DeepFace

app = Flask(__name__)

# Mood to Playlist mapping
emotion_to_playlist = {
    'happy': 'https://open.spotify.com/playlist/37i9dQZF1DXdPec7aLTmlC',
    'sad': 'https://open.spotify.com/playlist/37i9dQZF1DX7qK8ma5wgG1',
    'angry': 'https://open.spotify.com/playlist/37i9dQZF1DWYxwmBaMqxsl',
    'surprise': 'https://open.spotify.com/playlist/37i9dQZF1DWTfrr8pte1rT',
    'fear': 'https://open.spotify.com/playlist/37i9dQZF1DX4sWSpwq3LiO',
    'disgust': 'https://open.spotify.com/playlist/37i9dQZF1DX7gtIfGVzmkY',
    'neutral': 'https://open.spotify.com/playlist/37i9dQZF1DX4WYpdgoIcn6'
}

# Better face detection
def detect_emotion():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cap.release()

    if not ret:
        return "neutral"
    
    try:
        # Enhanced face detection with 'mtcnn' or 'dlib'
        analysis = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=True, detector_backend='mtcnn')
        if isinstance(analysis, list) and len(analysis) > 0:
            emotion = analysis[0].get('dominant_emotion', 'neutral')
        else:
            emotion = 'neutral'
        return emotion
    except Exception as e:
        print(f"[ERROR] Emotion detection failed: {e}")
        return "neutral"

@app.route('/')
def index():
    html = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>🎧 Moodify - Feel the Vibe</title>
        <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;500;700&display=swap" rel="stylesheet">
        <style>
            body {
                font-family: 'Poppins', sans-serif;
                background: linear-gradient(135deg, #667eea, #764ba2, #f39c12, #e74c3c);
                background-size: 400% 400%;
                animation: gradientAnimation 10s ease infinite;
                margin: 0;
                padding: 0;
                color: #fff;
            }

            .navbar {
                background-color: rgba(0, 0, 0, 0.25);
                padding: 20px;
                text-align: center;
                font-size: 2rem;
                font-weight: bold;
                letter-spacing: 2px;
                box-shadow: 0 2px 10px rgba(0, 0, 0, 0.3);
            }

            .container {
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                padding: 50px 20px;
                text-align: center;
            }

            .features {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
                gap: 20px;
                max-width: 1000px;
                margin: 40px auto;
                padding: 0 20px;
            }

            .box {
                background-color: rgba(255, 255, 255, 0.1);
                border-radius: 15px;
                padding: 25px;
                backdrop-filter: blur(10px);
                box-shadow: 0 4px 20px rgba(0, 0, 0, 0.2);
                transition: 0.3s ease;
            }

            .box:hover {
                transform: translateY(-5px);
                background-color: rgba(255, 255, 255, 0.15);
            }

            .box h3 {
                margin-top: 0;
                font-size: 1.5rem;
                margin-bottom: 10px;
            }

            .box p {
                font-size: 1rem;
                color: #eee;
            }

            h1 {
                font-size: 3rem;
                margin-bottom: 10px;
                animation: fadeIn 1.5s ease;
            }

            p.description {
                font-size: 1.2rem;
                margin-bottom: 30px;
                max-width: 600px;
                animation: fadeIn 2.5s ease;
            }

            button {
                padding: 15px 30px;
                font-size: 1.2rem;
                background-color: #1DB954;
                color: #fff;
                border: none;
                border-radius: 10px;
                cursor: pointer;
                transition: all 0.3s ease;
                margin-bottom: 20px;
            }

            button:hover {
                background-color: #1ed760;
            }

            input {
                padding: 10px;
                font-size: 1rem;
                margin-top: 20px;
                border-radius: 8px;
                border: none;
                width: 200px;
            }

            #result {
                margin-top: 30px;
                font-size: 1.3rem;
                font-weight: 600;
                animation: fadeIn 3s ease;
            }

            .bottom-note {
                margin-top: 80px;
                font-size: 0.9rem;
                color: rgba(255, 255, 255, 0.7);
                text-align: center;
            }

            .bottom-note .creators {
                margin-top: 5px;
                font-size: 0.8rem;
                letter-spacing: 1px;
                color: #ccc;
            }

            a {
                color: #fff;
                text-decoration: underline;
            }

            @keyframes gradientAnimation {
                0% { background-position: 0% 50%; }
                50% { background-position: 100% 50%; }
                100% { background-position: 0% 50%; }
            }

            @keyframes fadeIn {
                0% { opacity: 0; transform: translateY(20px); }
                100% { opacity: 1; transform: translateY(0); }
            }
        </style>
    </head>
    <body>
        <div class="navbar">🎵 MOODIFY</div>
        <div class="container">
            <h1>Let Your Mood Pick the Music</h1>
            <p class="description">Your emotions decide the rhythm. With AI-powered facial recognition and smart mood detection, we deliver a Spotify playlist tailored just for your vibe.</p>

            <button onclick="getPlaylist()">Detect My Mood</button>

            <div>
                <p style="margin-top:20px;">Or manually tell us how you feel:</p>
                <input type="text" id="manualMood" placeholder="happy / sad / angry..." />
                <button onclick="getManualPlaylist()">Get Playlist</button>
            </div>

            <div id="result"></div>

            <div class="features">
                <div class="box">
                    <h3>🎭 Emotion Detection</h3>
                    <p>Real-time face analysis to detect how you're feeling.</p>
                </div>
                <div class="box">
                    <h3>🎧 Spotify Integration</h3>
                    <p>Instant mood-matching playlists from Spotify.</p>
                </div>
                <div class="box">
                    <h3>⚡ Fast & Lightweight</h3>
                    <p>Loads instantly. Just click & vibe.</p>
                </div>
                <div class="box">
                    <h3>🧠 Powered by AI</h3>
                    <p>Using DeepFace and Python ML libraries under the hood.</p>
                </div>
            </div>

            <div class="bottom-note">
                <p>🎧 Music connects hearts, heals minds, and fuels moments.</p>
                <p class="creators">Made with ❤️ by Meet Prajapati, Zeel Dudhat & Neel Patel</p>
            </div>
        </div>

        <script>
            function getPlaylist() {
                document.getElementById('result').innerHTML = "Detecting mood... 😶";
                fetch('/get_playlist')
                    .then(res => res.json())
                    .then(data => {
                        document.getElementById('result').innerHTML =
                            `Detected Emotion: <strong>${data.emotion}</strong> 😎<br>
                             <a href="${data.playlist}" target="_blank">🎧 Play Moodify Playlist</a>`;
                    });
            }

            function getManualPlaylist() {
                let mood = document.getElementById('manualMood').value.toLowerCase();
                fetch(`/get_playlist_by_mood?mood=${mood}`)
                    .then(res => res.json())
                    .then(data => {
                        document.getElementById('result').innerHTML =
                            `Your Mood: <strong>${data.emotion}</strong> 😎<br>
                             <a href="${data.playlist}" target="_blank">🎧 Play Moodify Playlist</a>`;
                    });
            }
        </script>
    </body>
    </html>
    '''
    return render_template_string(html)

@app.route('/get_playlist', methods=['GET'])
def get_playlist():
    emotion = detect_emotion()
    playlist_url = emotion_to_playlist.get(emotion, emotion_to_playlist['neutral'])
    return jsonify({'emotion': emotion, 'playlist': playlist_url})

@app.route('/get_playlist_by_mood', methods=['GET'])
def get_playlist_by_mood():
    mood = request.args.get('mood', '').lower()
    if mood not in emotion_to_playlist:
        mood = 'neutral'
    playlist_url = emotion_to_playlist[mood]
    return jsonify({'emotion': mood, 'playlist': playlist_url})

if __name__ == '__main__':
    app.run(debug=True)

