import tkinter as tk
from tkhtmlview import HTMLLabel

# Create the main window
root = tk.Tk()

# Make the window borderless
root.overrideredirect(True)  # Remove the title bar and borders

# Set the window size and position
root.geometry("800x600+100+100")  # Adjust the size and position as needed

# Load HTML content from the file
html_file_path = "./fx/web/party.html"

try:
    with open(html_file_path, "r", encoding="utf-8") as html_file:
        html_content = html_file.read()
except FileNotFoundError:
    html_content = "<p>HTML file not found!</p>"

# Create an HTMLLabel widget and place it inside the window
html_label = HTMLLabel(root, html=html_content)
html_label.pack(fill="both", expand=True)

# Optionally, make the window draggable (if required)
def move_window(event):
    root.geometry(f"+{event.x_root}+{event.y_root}")

root.bind("<B1-Motion>", move_window)

# Run the Tkinter main loop
root.mainloop()
