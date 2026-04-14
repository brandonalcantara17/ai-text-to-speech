import os
import sys
import json
import urllib.request
import sounddevice as sd
import soundfile as sf
from kokoro_onnx import Kokoro

CONFIG_FILE = "config.json"

MODEL_URL = "https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/kokoro-v1.0.onnx"
VOICES_URL = "https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/voices-v1.0.bin"

MODEL_FILE = "kokoro-v1.0.onnx"
VOICES_FILE = "voices-v1.0.bin"

def ensure_file(file_path, url, description):
    if not os.path.exists(file_path):
        print(f"{description} not found: {file_path}")
        choice = input("Download it? (y/n): ").strip().lower()
        if choice != "y":
            print("Missing required files. Exiting.")
            sys.exit(1)
        try:
            urllib.request.urlretrieve(url, file_path)
            print(f"{description} downloaded.")
        except Exception as e:
            print(f"Download failed: {e}")
            sys.exit(1)

if not os.path.exists(CONFIG_FILE):
    print(f"{CONFIG_FILE} not found.")
    sys.exit(1)

with open(CONFIG_FILE, "r", encoding="utf-8") as f:
    config = json.load(f)

text = config.get("text", "").strip()
if not text:
    print("Text is empty in config.json")
    sys.exit(1)

lang_code = config.get("language", "en-us")
voice = config.get("voice", "af_heart")
speed = float(config.get("speed", 1.0))
output_mode = config.get("output_mode", "file")
output_file = config.get("output_file", "output.wav")

if not output_file.endswith(".wav"):
    output_file += ".wav"

ensure_file(MODEL_FILE, MODEL_URL, "Model file (.onnx)")
ensure_file(VOICES_FILE, VOICES_URL, "Voices file (.bin)")

kokoro = Kokoro(MODEL_FILE, VOICES_FILE)

print("Generating...")
samples, sample_rate = kokoro.create(
    text,
    voice=voice,
    speed=speed,
    lang=lang_code
)

sf.write(output_file, samples, sample_rate)

if output_mode == "play":
    print("Playing audio...")
    sd.play(samples, sample_rate)
    sd.wait()
    os.remove(output_file)
    print("Done.")
else:
    print(f"Saved to {output_file}")