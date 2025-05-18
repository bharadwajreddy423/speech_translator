```markdown
# 🎙️ Speech Translator – Multilingual Audio to Text & Translation Pipeline

This project enables **automatic transcription and translation** of speech from audio files using:

- 🧠 [FasterWhisper](https://github.com/SYSTRAN/faster-whisper) for automatic speech recognition (ASR)
- 🌍 [Helsinki-NLP MarianMT](https://huggingface.co/Helsinki-NLP) models for neural machine translation (NMT)
- ✅ Command-line interface for batch processing
- 🧪 Unit-tested with Pytest for reliability

---

## ✅ Features

- 🔁 Transcribes spoken language from `.mp3`, `.wav`, `.m4a`, `.flac` files
- 🌐 Translates into **any supported language**
- 🧾 Accepts input like `audio/german.mp3:en` to convert from German audio to English text
- 🧠 Automatically detects source language
- ⚙️ Supports CPU and GPU, with customizable compute precision
- 🔬 Includes unit tests to ensure accurate processing

---

## 📁 Project Structure

```

speech\_translator/
├── audio/                  # Input audio samples
├── tests/                  # Unit tests
├── transcription.py        # Whisper ASR logic
├── translation.py          # MarianMT translation logic
├── run\_pipeline.py         # Main CLI pipeline
├── requirements.txt        # Dependencies
├── pytest.ini              # Test configuration
├── .gitignore              # Ignore virtual env and cache
└── README.md               # Project documentation

````

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/bharadwajreddy423/speech_translator.git
cd speech_translator
````

### 2. Create and activate virtual environment

```bash
python -m venv venv
source venv/bin/activate    # macOS/Linux
venv\Scripts\activate       # Windows
```

### 3. Install all dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

Run the pipeline with any number of input audio files:

```bash
python run_pipeline.py \
  --inputs audio/german.mp3:en audio/french.mp3:hi \
  --device cpu \
  --compute_type int8
```

### 🔍 Parameters:

* `--inputs`: Space-separated list of `audio_file:target_lang` pairs
* `--device`: `cpu` or `cuda` (for GPU inference)
* `--compute_type`: `int8`, `float16`, or `float32` precision

### ✅ Example Output:

```
========== Result ==========
File: audio/german.mp3
Detected Language: de
Transcript:
 Janusz, wie hältst du dich glücklich? ...
Translated to en:
 Janusz, how do you feel happy? ...
============================
```

---

## 🧪 Running Unit Tests

Run all tests using Pytest:

```bash
pytest -v
```

This will run tests for:

* Audio transcription
* Language translation
* Input validation logic

---

