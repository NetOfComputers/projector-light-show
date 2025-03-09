import tkinter as tk
import threading
import time
from beat_detection import AudioProcessor  # Import AudioProcessor class
import screeninfo  # This will be used to get screen dimensions
from light_show_fx import LSFX
class LightShowApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Light Show")

        # Get the second screen's resolution and position
        screens = screeninfo.get_monitors()
        if len(screens) > 1:
            screen = screens[1]  # Assuming second monitor is at index 1
            screen_width = screen.width
            screen_height = screen.height
            screen_x = screen.x
            screen_y = screen.y

            # Set the window size to the screen's dimensions (fullscreen)
            self.root.geometry(f"{screen_width}x{screen_height}+{screen_x}+{screen_y}")
        else:
            print("Second screen not found. Defaulting to primary screen.")
            self.root.geometry("1920x1080+0+0")  # Default to primary screen

        # Now remove window decorations (no borders or title bar)
        self.root.overrideredirect(True)

        # Set up the canvas and other GUI elements
        self.canvas = tk.Canvas(root, width=screen_width, height=screen_height)
        self.canvas.pack(fill=tk.BOTH, expand=True)
        
        # Initial variables for BPM and color switching
        self.bpm = 0  # Initial BPM value
        self.last_update_time = time.time()  # Track when the last update occurred
        self.update_interval = 60 / self.bpm if self.bpm else 1  # Default to 1 second interval if no BPM

        # Prepare fx instance

        self.fx = LSFX()


        # # # self.color_index = 0  # Start with the first color in the list
        # # # self.colors = ['#FF5733', '#33FF57', '#3357FF', '#F1C40F', '#9B59B6', '#E74C3C']  # List of colors
        # # # self.color_switching = False  # Flag to control color switching

        # Create an instance of AudioProcessor and pass the update method as a callback
        self.audio_processor = AudioProcessor(self.update_light_show)

        # Start the audio processing in a separate thread
        audio_thread = threading.Thread(target=self.audio_processor.start_audio_stream, daemon=True)
        audio_thread.start()

        # Start the tkinter main loop
        self.update_canvas_color()

    


    '''The function to calculate bpm calls this method passing in to it the current bpm'''
    def update_light_show(self, bpm):
        print('BPM updated:', bpm)
        self.bpm = bpm
        self.update_interval = 60 / self.bpm if self.bpm else 1
        self.color_switching = True

    '''This function calls a effect function every n seconds based on interval time. That interval time
    is calculated based on the BPM value. If the BPM is 0, it defaults to 1 second interval.'''
    def update_canvas_color(self):
        if self.color_switching and self.bpm > 0:
            current_time = time.time()
            if current_time - self.last_update_time >= self.update_interval:
                self.last_update_time = current_time
                
                # call current effect
                # # Update the color index to cycle through the colors list
                # self.color_index = (self.color_index + 1) % len(self.colors)  # Cycle through colors
                # color = self.colors[self.color_index]  # Get the current color from the list
                # self.canvas.config(bg=color)
        
        # self.root.after(10, self.update_canvas_color)  # Continue checking every 10ms for faster updates

def main():
    root = tk.Tk()
    app = LightShowApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
