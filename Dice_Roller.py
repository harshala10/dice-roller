import tkinter as tk
import random
from PIL import Image, ImageTk  # Ensure Pillow is installed

# Function to load and resize dice images
def load_dice_images():
    images = {}
    image_directory = r'C:\Users\harshala\Desktop\Dice_Roller\\'  # Corrected path
    for i in range(1, 7):
        # Load image
        img = Image.open(f'{image_directory}dice{i}.png')
        # Resize image to 100x100 pixels using LANCZOS
        img = img.resize((100, 100), Image.LANCZOS)  
        images[i] = ImageTk.PhotoImage(img)
    return images

# Function to roll the dice and display results
def roll_dice():
    try:
        num_dice = int(entry_num_dice.get())
        if num_dice <= 0:
            raise ValueError("Number of dice must be positive.")
        
        results = [random.randint(1, 6) for _ in range(num_dice)]
        label_result.config(text=f"Results: {', '.join(map(str, results))}")

        # Update the images based on the roll results
        for i in range(num_dice):
            if i < 6:  # Display up to 6 dice images
                dice_labels[i].config(image=dice_images[results[i]])
                dice_labels[i].image = dice_images[results[i]]
            else:
                break
    except ValueError as e:
        label_result.config(text="Error: " + str(e))
        
 # Clear the image
def clear():
    entry_num_dice.delete(0, tk.END)
    label_result.config(text="Results: ")
    for label in dice_labels:
        label.config(image='') 

# Create the main window
root = tk.Tk()
root.title("Dice Roller")

# Load dice images
dice_images = load_dice_images()

# Create and place widgets
label_instruction = tk.Label(root, text="Enter the number of dice to roll:")
label_instruction.pack()

entry_num_dice = tk.Entry(root)
entry_num_dice.pack()

button_roll = tk.Button(root, text="Roll Dice", command=roll_dice)
button_roll.pack()

button_clear = tk.Button(root, text="Clear", command=clear)
button_clear.pack()

label_result = tk.Label(root, text="Results: ")
label_result.pack()

# Create labels for dice images
dice_labels = []
for _ in range(6):  # Maximum of 6 dice
    label = tk.Label(root)
    label.pack(side=tk.LEFT, padx=5, pady=5)  # Add padding to the sides
    dice_labels.append(label)

# Run the application
root.mainloop()
