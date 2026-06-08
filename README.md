# 🤖 Nova - AI Voice Assistant

A Python-based voice assistant that listens for your voice, responds intelligently using Google Gemini AI, reads the news, plays music, and speaks back in a natural voice.

Built by **Nilkamal Giri** | Inspired by Code with Harry

---

## ✨ Features

- 🎤 Wake word detection — say **"Nova"** to activate
- 🌐 Open websites — Google, YouTube, Instagram
- 🎵 Play music from your personal library
- 📰 Fetch top 5 live news headlines (India)
- 🤖 AI-powered responses using **Google Gemini 2.5 Flash**
- 🔊 Natural voice output using **gTTS** (Google Text-to-Speech)

---

## 📁 Project Structure

```
nova-voice-assistant/
├── main.py            # Main program — wake word, commands, voice
├── client.py          # Gemini AI integration
├── news.py            # GNews API — fetches headlines
├── musiclibrary.py    # Your music links
├── requirements.txt   # All Python dependencies
├── .env               # API keys (NOT shared — create your own)
└── .gitignore         # Keeps .env safe from GitHub
```

---

## ⚙️ Requirements

### 1. Python 3.12.3
Download from: https://python.org/downloads

> ✅ During install, check **"Add Python to PATH"**

### 2. FFmpeg
Required by `pydub` for audio speed control.

1. Download from: https://www.gyan.dev/ffmpeg/builds/
2. Download `ffmpeg-release-essentials.zip`
3. Extract and move to `C:\ffmpeg` or your choice
4. Add `C:\ffmpeg\bin` or the bin folder location to your **System PATH**

To verify:
```bash
ffmpeg -version
```

### 3. A working microphone
Built-in laptop mic works fine.

---

## 🚀 Setup & Installation

### Step 1 — Clone the repository
```bash
git clone https://github.com/nilkamalgiri22-lab/Nova-voice-assistant.git
cd Nova-voice-assistant
```

### Step 2 — Create virtual environment
```bash
python -m venv .venv
```

### Step 3 — Activate virtual environment
```bash
# Windows
.venv\Scripts\activate
```

### Step 4 — Install dependencies
```bash
pip install -r requirements.txt
```

### Step 5 — Create your `.env` file
Create a file named `.env` in the project folder:
```
GEMINI_API_KEY=your_gemini_key_here
GNEWS_API_KEY=your_gnews_key_here
```

Get your free API keys here:
- **Gemini**: https://aistudio.google.com (free)
- **GNews**: https://gnews.io (free, 100 requests/day)

### Step 6 — Run!
```bash
python main.py
```

---

## 🎙️ How to Use

| You say | Nova does |
|---|---|
| `"Nova"` | Wakes up and says *"Yes"* |
| `"open google"` | Opens Google in browser |
| `"open youtube"` | Opens YouTube in browser |
| `"open instagram"` | Opens Instagram in browser |
| `"play set"` | Plays music from your library |
| `"tell news"` | Reads top 5 India headlines |
| anything else | Answered by Gemini AI |

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| `SpeechRecognition` | Microphone input & Google STT |
| `gTTS` | Google Text-to-Speech |
| `pygame` | Audio playback |
| `pydub` + `ffmpeg` | Audio speed control |
| `google-genai` | Gemini AI responses |
| `requests` | News API calls |
| `python-dotenv` | Secure API key loading |

---

## 📝 Notes

- Internet connection is required (gTTS, Gemini, GNews all need it)
- Currently optimized for **Windows**
- News headlines are fetched for **India** by default
- Voice speed is set to `1.3x` for an Alexa-like feel — tune it in `main.py`

---

## 🔒 Security

Never share your `.env` file. It contains your private API keys.
The `.gitignore` file ensures `.env` is never uploaded to GitHub.
