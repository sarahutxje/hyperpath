# HyperPath

HyperPath is a simple and efficient file compression and decompression tool with a graphical user interface (GUI) built using Python's Tkinter library. It supports various file formats, making it easy to compress and decompress files on Windows.

## Features

- **Compress Files**: Quickly compress files into ZIP format.
- **Decompress Files**: Supports decompression of ZIP and TAR (including `.tar.gz` and `.tgz`) formats.
- **User-Friendly Interface**: Simple GUI to select files and perform operations.

## Requirements

- Python 3.x
- Tkinter (should be available with Python installation)
- `zipfile` and `tarfile` modules (part of Python standard library)

## Installation

1. Clone the repository or download the `hyperpath.py` file.

   ```bash
   git clone https://github.com/yourusername/HyperPath.git
   ```

2. Navigate to the directory containing `hyperpath.py`.

   ```bash
   cd HyperPath
   ```

3. Run the program using Python.

   ```bash
   python hyperpath.py
   ```

## Usage

1. Launch the application.
2. Click on "Browse" to select a file you wish to compress or decompress.
3. Click "Compress" to create a ZIP file of the selected file.
4. Click "Decompress" to extract files from a supported compressed file.

## Supported Formats

- **Compression**: ZIP
- **Decompression**: ZIP, TAR, TAR.GZ, TGZ

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.