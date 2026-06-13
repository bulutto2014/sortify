# Sortify 🚀

Sortify is a lightweight, standalone Windows desktop utility that instantly cleans up your messy `Downloads` folder. With a single click, it automatically categorizes and moves your files into their corresponding official system directories (Documents, Pictures, Videos) based on their file extensions.

No Python installation or setup required—just download the executable and run.

> 💡 **Built with Gemini Flash**
> This project was co-authored, optimized, and compiled using Google's Gemini Flash, ensuring clean automation logic and robust Windows integration.

---

## Features
- **Zero Configuration:** Automatically detects your active Windows user profile and dynamic `Downloads` path.
- **Direct Categorization:** Moves images to `Pictures`, videos to `Videos`, and documents/archives to `Documents` instantly without creating cluttered subfolders.
- **Smart Skip System:** Built-in protection that automatically detects if a file with the exact same name already exists in the target folder to prevent accidental overwrites.
- **Safe Execution:** Implements a quick security confirmation step (`Y/N`) before making any changes to your files.
- **True 'Any Key' Exit:** Leverages Windows-native low-level console handling to close the window instantly on any keyboard press when finished.

---

## How to Download and Run

Since Sortify is compiled as a standalone Windows executable, you don't need Python installed on your computer.

1. Go to the **Releases** section on the right side of this GitHub repository.
2. Download the latest `sortify.exe` file.
3. Move the file anywhere you like (e.g., your Desktop).
4. Double-click `sortify.exe` to launch the program, type `Y` to confirm, and let it clean your folders in milliseconds!

---

## Technical Stack & Under the Hood
For developers interested in how it's built:
- **Core Engine:** Python 3.x
- **Standard Modules Used:** `os` (Path resolution), `shutil` (High-level file operations), `msvcrt` (Native Windows console keystroke control)
- **Compiler:** PyInstaller (Bundled into a single `--onefile` executable binary)
- **AI Collaborator:** Gemini Flash

---

## License
This project is open-source and available under the **MIT License**. Feel free to fork, modify, or use it however you like!
