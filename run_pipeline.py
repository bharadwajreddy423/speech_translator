# run_pipeline.py

import os
import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed

from transcription import transcribe_audio
from translation import translate_text

SUPPORTED_FORMATS = (".wav", ".mp3", ".flac", ".m4a")


def parse_input_pairs(input_args):
    """
    Parses input in the format: "file1.wav:en file2.mp3:hi" into a dictionary.
    """
    file_map = {}
    for pair in input_args:
        try:
            path, target = pair.split(":")
            if not os.path.isfile(path):
                print(f"Skipping: {path} is not a valid file.")
                continue
            if not path.lower().endswith(SUPPORTED_FORMATS):
                print(f"Skipping: {path} is not a supported audio format.")
                continue
            file_map[path] = target.strip().lower()
        except ValueError:
            print(f"Invalid input pair format: {pair} — should be 'file_path:target_lang'")
    return file_map


def process_file(audio_path, target_lang, model_size, device, compute_type):
    """
    Transcribes and translates a single audio file to the requested target language.
    """
    try:
        transcript, source_lang = transcribe_audio(
            audio_path=audio_path,
            model_size=model_size,
            device=device,
            compute_type=compute_type
        )

        translated = translate_text(
            text=transcript,
            src_lang=source_lang,
            tgt_lang=target_lang
        )

        return {
            "audio_path": audio_path,
            "source_lang": source_lang,
            "target_lang": target_lang,
            "transcript": transcript,
            "translated_text": translated
        }

    except Exception as e:
        print(f"Error processing {audio_path}: {e}")
        return None


def main():
    parser = argparse.ArgumentParser(description="Dynamic Multi-Audio Translator with ASR + Translation")
    parser.add_argument(
        "--inputs",
        nargs="+",
        required=True,
        help="List of 'file_path:target_lang' pairs, space-separated"
    )
    parser.add_argument("--model_size", default="small", help="Whisper model size")
    parser.add_argument("--device", default="cpu", help="Device: cpu or cuda")
    parser.add_argument("--compute_type", default="int8", help="Compute type: int8 or float16")

    args = parser.parse_args()

    file_lang_map = parse_input_pairs(args.inputs)
    if not file_lang_map:
        print("No valid audio inputs found. Exiting.")
        return

    print(f"\nProcessing {len(file_lang_map)} audio files...\n")

    with ThreadPoolExecutor() as executor:
        future_to_file = {
            executor.submit(
                process_file,
                audio_path,
                target_lang,
                args.model_size,
                args.device,
                args.compute_type
            ): audio_path for audio_path, target_lang in file_lang_map.items()
        }

        for future in as_completed(future_to_file):
            result = future.result()
            if result:
                print("\n========== Result ==========")
                print(f"File: {result['audio_path']}")
                print(f"Detected Language: {result['source_lang']}")
                print(f"Transcript:\n{result['transcript']}")
                print(f"Translated to {result['target_lang']}:\n{result['translated_text']}")
                print("============================\n")


if __name__ == "__main__":
    main()
