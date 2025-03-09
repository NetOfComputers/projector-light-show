import tkinter as tk
import screeninfo

# Function to open fullscreen window on a specific screen
def open_fullscreen_on_screen(screen_index=0):
    # Get all connected screens
    screens = screeninfo.get_monitors()

    if screen_index >= len(screens):
        print("Invalid screen index")
        return

    # Create a root window
    root = tk.Tk()

    # Get the specified screen dimensions (e.g., screen_index 0 for the first screen)
    screen = screens[screen_index]

    # Set window size to the screen size and move it to the correct position
    root.geometry(f"{screen.width}x{screen.height}+{screen.x}+{screen.y}")

    # Print the initial position and size of the window
    print(f"Initial window geometry: Width={screen.width}, Height={screen.height}, X={screen.x}, Y={screen.y}")

    # You can add a label or any widgets here for testing
    label = tk.Label(root, text="Fullscreen Window", font=("Arial", 30))
    label.pack(expand=True)

    # Function to print window size and position when it's moved or resized
    def print_position():
        width = root.winfo_width()
        height = root.winfo_height()
        x = root.winfo_x()
        y = root.winfo_y()
        print(f"Window geometry - Width: {width}, Height: {height}, X: {x}, Y: {y}")

    # Bind to <Configure> event to monitor changes in size/position
    root.bind("<Configure>", lambda event: print_position())

    # Start the Tkinter mainloop
    root.mainloop()

# Open the window on the first screen (index 0)
open_fullscreen_on_screen(screen_index=0)
