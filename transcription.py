# transcription.py

from faster_whisper import WhisperModel

def transcribe_audio(
    audio_path: str,
    model_size: str = "small",
    device: str = "cpu",
    compute_type: str = "int8"
) -> tuple[str, str]:
    """
    Transcribes an audio file and returns the detected language and transcript.

    Parameters:
        audio_path (str): Path to the input audio file (e.g., WAV, MP3).
        model_size (str): Whisper model variant to load ('tiny', 'small', 'medium', etc.).
        device (str): Device to use for inference ('cpu' or 'cuda').
        compute_type (str): Computation precision ('int8', 'float16', etc.).

    Returns:
        transcript (str): Full transcribed text from the audio.
        detected_language (str): ISO 639-1 language code detected from audio (e.g., 'de', 'fr', 'en').
    """

    # Load the Whisper model with selected configuration
    model = WhisperModel(
        model_size_or_path=model_size,
        device=device,
        compute_type=compute_type
    )

    # Run transcription; beam_size controls search complexity (higher = better accuracy, slower)
    segments, info = model.transcribe(audio_path, beam_size=1)

    # Join segments into a full transcript string
    transcript = " ".join([segment.text for segment in segments])

    # Return the transcribed text and detected language code
    return transcript, info.language
