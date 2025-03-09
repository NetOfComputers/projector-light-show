import tkinter as tk
import threading
import time
from beat_detection import AudioProcessor  # Import AudioProcessor class

class LightShowApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Light Show")
        self.root.geometry("1920x1080+1920+0")  # Set window size and position
        # self.root.attributes('-fullscreen', True)
        # self.root.geometry("400x400+1911+0")  # Set window size and position
        # self.root.overrideredirect(True)  # Remove window decorations
        self.canvas = tk.Canvas(root, width=400, height=400)
        self.canvas.pack()
        self.bpm = 0  # Initial BPM value
        self.last_update_time = time.time()  # Track when the last update occurred
        self.update_interval = 60 / self.bpm if self.bpm else 1  # Default to 1 second interval if no BPM
        self.color_index = 0  # Start with the first color in the list
        self.colors = ['#FF5733', '#33FF57', '#3357FF', '#F1C40F', '#9B59B6', '#E74C3C']  # List of colors
        self.color_switching = False  # Flag to control color switching

        # Create an instance of AudioProcessor and pass the update method as a callback
        self.audio_processor = AudioProcessor(self.update_light_show)

        # Start the audio processing in a separate thread
        audio_thread = threading.Thread(target=self.audio_processor.start_audio_stream, daemon=True)
        audio_thread.start()

        # Start the tkinter main loop
        self.update_canvas_color()

    def update_light_show(self, bpm):
        print('BPM updated:', bpm)
        self.bpm = bpm  # Update the BPM value
        self.update_interval = 60 / self.bpm if self.bpm else 1  # Calculate the new update interval
        self.color_switching = True  # Start switching the color once we get the first BPM

    def update_canvas_color(self):
        if self.color_switching and self.bpm > 0:
            current_time = time.time()
            if current_time - self.last_update_time >= self.update_interval:
                self.last_update_time = current_time  # Update the last update time
                
                # Update the color index to cycle through the colors list
                self.color_index = (self.color_index + 1) % len(self.colors)  # Cycle through colors
                color = self.colors[self.color_index]  # Get the current color from the list
                self.canvas.config(bg=color)
        
        self.root.after(10, self.update_canvas_color)  # Continue checking every 10ms for faster updates

def main():
    root = tk.Tk()
    app = LightShowApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
