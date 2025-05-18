import os
import pytest
from transcription import transcribe_audio

def test_transcribe_audio_returns_text_and_lang():
    audio_path = "audio/audio04.mp3"  # Provide this short test audio
    if not os.path.exists(audio_path):
        pytest.skip("Test audio not available.")

    transcript, lang = transcribe_audio(audio_path, model_size="tiny", device="cpu", compute_type="int8")
    assert isinstance(transcript, str)
    assert len(transcript.strip()) > 0
    assert isinstance(lang, str)
