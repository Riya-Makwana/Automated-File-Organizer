import os
import shutil

# CONFIGURATION
SOURCE_FOLDER = r"C:\Users\DELL\OneDrive\Desktop"  

FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".csv", ".pptx"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Music": [".mp3", ".wav"],
    "Archives": [".zip", ".rar", ".7z"]
}

# FUNCTION TO ORGANIZE FILES
def organize_files():
    try:
        for file_name in os.listdir(SOURCE_FOLDER):
            file_path = os.path.join(SOURCE_FOLDER, file_name)

            # Skip folders
            if os.path.isdir(file_path):
                continue

            file_extension = os.path.splitext(file_name)[1].lower()
            moved = False

            for folder_name, extensions in FILE_CATEGORIES.items():
                if file_extension in extensions:
                    folder_path = os.path.join(SOURCE_FOLDER, folder_name)

                    # Create folder if not exists
                    if not os.path.exists(folder_path):
                        os.makedirs(folder_path)

                    shutil.move(file_path, os.path.join(folder_path, file_name))
                    print(f"Moved: {file_name} → {folder_name}")
                    moved = True
                    break

            # Move unknown files
            if not moved:
                other_folder = os.path.join(SOURCE_FOLDER, "Others")
                if not os.path.exists(other_folder):
                    os.makedirs(other_folder)

                shutil.move(file_path, os.path.join(other_folder, file_name))
                print(f"Moved: {file_name} → Others")

        print("\n File organization completed successfully!")

    except Exception as e:
        print(f" Error occurred: {e}")


# RUN SCRIPT
if __name__ == "__main__":
    organize_files()
