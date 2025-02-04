import os
import zipfile
import tarfile
import tkinter as tk
from tkinter import filedialog, messagebox

class HyperPath:
    def __init__(self, root):
        self.root = root
        self.root.title("HyperPath - File Compressor and Decompressor")
        self.root.geometry("400x250")

        self.file_path = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Select a file to compress/decompress:").pack(pady=10)

        tk.Entry(self.root, textvariable=self.file_path, width=50).pack(pady=5)
        tk.Button(self.root, text="Browse", command=self.browse_file).pack(pady=5)

        tk.Button(self.root, text="Compress", command=self.compress_file).pack(pady=10)
        tk.Button(self.root, text="Decompress", command=self.decompress_file).pack(pady=5)

    def browse_file(self):
        file_path = filedialog.askopenfilename()
        self.file_path.set(file_path)

    def compress_file(self):
        file_path = self.file_path.get()

        if not file_path:
            messagebox.showwarning("Warning", "Please select a file to compress.")
            return

        compressed_file_path = file_path + '.zip'
        with zipfile.ZipFile(compressed_file_path, 'w') as zipf:
            zipf.write(file_path, os.path.basename(file_path))
        
        messagebox.showinfo("Success", f"File compressed successfully to {compressed_file_path}")

    def decompress_file(self):
        file_path = self.file_path.get()

        if not file_path:
            messagebox.showwarning("Warning", "Please select a file to decompress.")
            return

        if file_path.endswith('.zip'):
            with zipfile.ZipFile(file_path, 'r') as zipf:
                zipf.extractall(os.path.dirname(file_path))
            messagebox.showinfo("Success", f"File decompressed successfully in {os.path.dirname(file_path)}")
        elif file_path.endswith(('.tar.gz', '.tgz', '.tar')):
            with tarfile.open(file_path, 'r:*') as tarf:
                tarf.extractall(os.path.dirname(file_path))
            messagebox.showinfo("Success", f"File decompressed successfully in {os.path.dirname(file_path)}")
        else:
            messagebox.showwarning("Warning", "Unsupported file format for decompression.")

if __name__ == "__main__":
    root = tk.Tk()
    app = HyperPath(root)
    root.mainloop()