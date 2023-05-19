import os

# Directory containing the images
directory = r'D:\Pictures\database\exam pprs'

# Iterate over the files in the directory
for i, filename in enumerate(os.listdir(directory)):
    if filename.endswith('.jpg') or filename.endswith('.jpeg') or filename.endswith('.png'):
        # New filename
        new_filename = f'{i}.jpg'
        
        # Full paths of old and new filenames
        old_filepath = os.path.join(directory, filename)
        new_filepath = os.path.join(directory, new_filename)
        
        # Rename the file
        os.rename(old_filepath, new_filepath)
        print(f'Renamed "{filename}" to "{new_filename}"')