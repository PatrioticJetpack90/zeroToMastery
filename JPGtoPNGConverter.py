'''
Converts image from your directory to another folder called new folder.

jpg to png
'''

import os
from PIL import Image

directory = r"Your directory" #this should be the only line you likely new to change.
new_folder_path = os.path.join(directory, "new")

# Create a new folder if it doesn't exist
if not os.path.exists(new_folder_path):
    os.makedirs(new_folder_path)

# Process each file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".jpg"):
        prefix = filename.split(".jpg")[0]
        input_path = os.path.join(directory, filename)  # Full path to the .jpg file
        output_path = os.path.join(new_folder_path, prefix + '.png')  # Path for the .png file

        # Open the .jpg and save as .png in the 'new' folder
        with Image.open(input_path) as im:
            im.save(output_path)
    else:
        continue


print("All .jpg files have been converted and saved as .png in the 'new' folder.")

