import tkinter as tk
from tkinter import scrolledtext
import pyperclip  
import webbrowser 
import os 

def format_text():
    input_text = text_input.get("1.0", tk.END).strip()
    output_text = ""
    
    for word in input_text.split():
        half_index = len(word) // 2
        formatted_word = f"<b>{word[:half_index]}</b>{word[half_index:]} "
        output_text += formatted_word

    text_output.config(state=tk.NORMAL)  # Enable editing
    text_output.delete("1.0", tk.END)    # Clear previous output
    text_output.insert(tk.END, output_text)  # Insert new formatted text
    text_output.config(state=tk.DISABLED)  # Disable editing

def copy_to_clipboard():
    # Get the content from the output area
    output_text = text_output.get("1.0", tk.END).strip()
    # Copy the content to the clipboard
    pyperclip.copy(output_text)

def export_to_html():
    output_text = text_output.get("1.0", tk.END).strip()
    
    # Create HTML content
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Formatted Text</title>
    </head>
    <body>
        <p>{output_text}</p>
    </body>
    </html>
    """
    
    # Define the file name and path
    file_path = os.path.expanduser("./formatted_text.html")
    
    # Write the HTML content to a file
    with open(file_path, 'w') as html_file:
        html_file.write(html_content)

    # Open the HTML file in the default web browser
    webbrowser.open(file_path)

root = tk.Tk()
root.title("Bionic Text Editor - h3x0r-offical")

text_input = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=10)
text_input.pack(padx=10, pady=10)

format_button = tk.Button(root, text="Format Text", command=format_text)
format_button.pack(pady=5)

export_button = tk.Button(root, text="Open in Browser", command=export_to_html)
export_button.pack(pady=5)

copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.pack(pady=5)

text_output = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=10, state=tk.DISABLED)
text_output.pack(padx=10, pady=10)

# Application loop
root.mainloop()
