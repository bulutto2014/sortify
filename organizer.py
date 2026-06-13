import os
import shutil
import msvcrt  # Windows'ta anlık tuş vuruşlarını yakalamak için gerekli kütüphane

def real_downloads_organizer():
    # Get the user's home directory path
    user_path = os.path.expanduser("~")
    
    # SOURCE: Directly the Downloads folder
    source_folder = os.path.join(user_path, "Downloads")
    
    # TARGETS: Main system folders
    documents_target = os.path.join(user_path, "Documents")
    pictures_target = os.path.join(user_path, "Pictures")
    videos_target = os.path.join(user_path, "Videos")

    # File extension groups
    image_extensions = [".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg", ".bmp"]
    document_extensions = [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx", ".zip", ".rar", ".7z"]
    video_extensions = [".mp4", ".mkv", ".avi", ".mov", ".wmv", ".flv", ".mpeg"]

    print("=== BULUT SMART FILE ORGANIZER ===")
    print(f"[Scanning Started] Source: {source_folder}\n")

    # Check if Downloads folder exists
    if not os.path.exists(source_folder):
        print("[Error] Downloads folder could not be found!")
        return

    # List everything inside the directory
    try:
        files = os.listdir(source_folder)
    except Exception as e:
        print(f"[Error] Could not read the folder: {e}")
        return

    moved_count = 0

    for file in files:
        file_path = os.path.join(source_folder, file)
        
        # If it is a directory, skip it. We only move files.
        if os.path.isdir(file_path):
            continue
            
        # Get the file extension and convert to lowercase
        _, extension = os.path.splitext(file)
        extension = extension.lower()
        
        target_folder = None
        target_name = ""

        # Match extensions directly with the main system folders
        if extension in image_extensions:
            target_folder = pictures_target
            target_name = "Pictures"
        elif extension in document_extensions:
            target_folder = documents_target
            target_name = "Documents"
        elif extension in video_extensions:
            target_folder = videos_target
            target_name = "Videos"
            
        # If it doesn't match any group, leave it in Downloads
        if target_folder is None:
            continue

        # Create target file path
        new_file_path = os.path.join(target_folder, file)
        
        # Check if the file already exists at the target to prevent overwriting
        if not os.path.exists(new_file_path):
            try:
                shutil.move(file_path, new_file_path)
                print(f"[Moved] {file} -> {target_name}/")
                moved_count += 1
            except Exception as e:
                print(f"[Error] Something went wrong while moving {file}: {e}")
        else:
            print(f"[Skipped] {file} already exists in {target_name} folder.")

    print(f"\n[Completed] Downloads folder is cleaned up! Total {moved_count} files moved to their destination.")

if __name__ == "__main__":
    # Security confirmation in English
    confirmation = input("Files in the Downloads folder will be moved to system folders. Do you confirm? (Y/N): ").strip().upper()
    if confirmation == "Y":
        real_downloads_organizer()
    else:
        print("Operation cancelled.")
        
    print("\n----------------------------------------")
    print("Press any key to escape...")
    
    # GERÇEK 'ANY KEY' MANTIĞI: Enter'a basmaya gerek kalmadan herhangi bir tuşu yakalar
    msvcrt.getch()