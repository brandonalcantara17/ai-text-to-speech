# ai-text-to-speech (Python)

Simple text-to-speech app using ai.

---

## 🚀 Quick Start

```bash
cd ai-text-to-speech
python -m venv venv
# or
python3 -m venv venv
```

### Activate environment

**Windows (CMD)**

```bash
venv\Scripts\activate.bat
```

**macOS / Linux**

```bash
source venv/bin/activate
```

---

## 📦 Install

```bash
python -m pip install -r requirements.txt
```

---

## ⚙️ Setup Config

**macOS / Linux**

```bash
cp config.example.json config.json
```

**Windows**

```bash
copy config.example.json config.json
```

Edit `config.json`:

```json
{
  "text": "Hello! Good Morning.",
  "language": "en-us",
  "voice": "af_heart",
  "speed": 1.0,
  "output_mode": "file",
  "output_file": "output.wav"
}
```

---

## ▶️ Run

```bash
python main.py
```

---

## 🛠️ Linux / WSL Troubleshooting

If you get this error:

```text
OSError: PortAudio library not found
```

Install PortAudio system packages:

```bash
sudo apt-get update
sudo apt-get install -y libportaudio2 portaudio19-dev
```

If you are running in WSL or another headless environment, you may see:

```text
sounddevice.PortAudioError: Error querying device -1
```

This usually means there is no default audio output device. Use file output instead of live playback in `config.json`:

```json
"output_mode": "file"
```

---

## ⚠️ macOS SSL Fix

If you see an error like:

```
CERTIFICATE_VERIFY_FAILED
```

Run this command:

```bash
/Applications/Python\ 3.x/Install\ Certificates.command
```

Replace `3.x` with your Python version (e.g. `3.11`).

Then run the app again.

## 🔊 Output Modes

- `"file"` → saves audio
- `"play"` → plays audio and deletes file

---

## 🌍 Supported Languages

- English (US) → `en-us`
- English (UK) → `en-gb`
- 日本語 → `ja`
- 中文 (普通话) → `zh`
- Castellano → `es`
- Français → `fr-fr`
- हिन्दी → `hi`
- Italiano → `it`
- Português (Brasil) → `pt-br`

---

## License / Attribution

This project uses the Kokoro TTS model licensed under the Apache License 2.0.
