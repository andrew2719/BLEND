import tkinter as tk
from tkinter import filedialog
import os
import asyncio
import aiofiles

async def read_file(file_path):
    async with aiofiles.open(file_path, 'rb') as file:
        data = await file.read()
    return data

async def main():
    # Create the Tkinter root window
    root = tk.Tk()
    root.withdraw()

    # Open the file explorer dialog
    file_path = filedialog.askopenfilename()

    # Get the file details
    filename = os.path.basename(file_path)
    size = os.path.getsize(file_path)
    extension = os.path.splitext(file_path)[1]

    # Read the file as binary data
    data = await read_file(file_path)

    # Print the file details
    # print("File Details:")
    # print("Filename:", filename)
    # print("Size:", size, "bytes")
    # print("Extension:", extension)
    # print("Data (binary):", data)

    file_details = {
        'filename': filename,
        'size': size,
        'extension': extension,
        'data': data
    }

    return file_details


# Run the asyncio event loop
# select_file_from_system = asyncio.run(main())
# print(select_file_from_system)
