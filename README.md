# Simple Keylogger (For Educational Use Only)

## Disclaimer

This project is **strictly for educational purposes only**.  
Do **not** run this keylogger on any computer that you do not own or do not have explicit permission to test on.  
Unauthorized use may violate privacy laws and local regulations.  
Always be responsible and ethical.

---

## What is a Keylogger?

A **keylogger** is a program that records the keys you press on your keyboard.  
It’s commonly used for:
- Debugging keyboard input
- Usability testing
- Parental control (with consent)
- Learning how system hooks work

---

## 🛠️ How It Works

This simple Python keylogger:
- Runs in the background
- Listens for each key press
- Saves every key to a text file (`key_log.txt`)
- Stops safely when you press `ESC`

The program uses the [`pynput`](https://pypi.org/project/pynput/) library, which allows Python to monitor keyboard events.

---

## Works On

- Windows  
- Linux (with X11; **not** fully supported on Wayland)  
- macOS (with appropriate permissions)

---

## Requirements

- Python 3.x
- `pynput` library
- (Linux only) `python3-xlib` if needed

---

## Installation

**Clone the repository**

```bash
git clone https://github.com/mz-mukhtar/PRODIGY_CS_04.git
cd PRODIGY_CS_04
```

**Install dependencies**

```bash
# Install pynput
pip install pynput

# For Linux: Xlib dependency
# (only if you get X errors)
sudo apt-get install python3-xlib
```

---

## How to use it

```bash
python3 keylogger.py
```
---

## Ethical Use

This tool is for:

- Learning how keyboard hooks work
- Practicing Python event handling
- Developing legitimate input-monitoring tools (e.g. hotkey apps)

Never use it to spy on others.
