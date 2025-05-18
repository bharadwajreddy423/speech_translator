````markdown
# 🎙️ Speech Translator

A command-line based **speech translation pipeline** that automatically:
1. Transcribes spoken language from an audio file (using [FasterWhisper](https://github.com/SYSTRAN/faster-whisper))
2. Translates the transcript into a desired language (using [MarianMT](https://huggingface.co/Helsinki-NLP))

---

## 🚀 Features

- 🔊 Transcribe speech from `.mp3`, `.wav`, `.flac`, `.m4a`
- 🌐 Translate from any detected spoken language to any supported target language
- 🧠 Uses FasterWhisper for fast and accurate ASR
- 🤖 Uses MarianMT models for multilingual neural machine translation
- 🔁 Batch processing via CLI (multiple audio files at once)
- 🧪 Includes unit tests with `pytest`
- 🖥️ Runs on CPU or GPU with configurable precision

---

## 📁 Project Structure

```text
speech_translator/
├── audio/                    # Sample audio files for testing
│   ├── audio01.mp3
│   ├── audio02.mp3
│   └── ...
├── tests/                    # Unit tests for each module
│   ├── test_transcription.py
│   ├── test_translation.py
│   └── test_utils.py
├── transcription.py          # ASR module using FasterWhisper
├── translation.py            # Translation module using MarianMT
├── run_pipeline.py           # Main CLI pipeline
├── requirements.txt          # Python dependencies
├── pytest.ini                # Pytest configuration
├── .gitignore                # Ignore venv, cache, and audio outputs
└── README.md                 # Project documentation
````

---

## ✅ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/bharadwajreddy423/speech_translator.git
cd speech_translator
```

### 2. Create and activate virtual environment

```bash
# macOS/Linux
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

### Command format

```bash
python run_pipeline.py \
  --inputs audio/audio01.mp3:en audio/audio02.mp3:hi \
  --device cpu \
  --compute_type int8
```

### Parameters

* `--inputs`: Space-separated list of audio files and target language pairs (e.g., `file.mp3:en`)
* `--device`: `cpu` or `cuda` (if using GPU)
* `--compute_type`: Precision mode (`int8`, `float16`, `float32`)

### Example Output

```
========== Result ==========
File: audio/audio01.mp3
Detected Language: fr
Transcript:
 Bonjour, je m'appelle Sophie. Je suis très heureuse de vous rencontrer.
Translated to en:
 Hello, my name is Sophie. I am very happy to meet you.
============================
```

---

## 🧪 Running Tests

Run unit tests using:

```bash
pytest -v
```

Tests will validate:

* Transcription accuracy
* Translation consistency
* Input parsing logic

