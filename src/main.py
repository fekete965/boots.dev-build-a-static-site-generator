import os
import shutil


STATIC_FOLDER_PATH = "static"
DIST_FOLDER_PATH = "public"


def main():
    move_static_files_to_public()


def move_static_files_to_public():
    cwd = os.getcwd()

    static_folder_path = os.path.join(cwd, STATIC_FOLDER_PATH)
    if not os.path.exists(static_folder_path):
        raise Exception(f"Static folder {static_folder_path} does not exist")

    dist_folder_path = os.path.join(cwd, DIST_FOLDER_PATH)

    # Clean up the dist folder
    delete_folder(dist_folder_path)
    # Create the dist folder
    os.makedirs(dist_folder_path)
    # Copy the static folder to the dist folder
    copy_folder(static_folder_path, dist_folder_path)


def delete_folder(dist_folder_path: str):
    if not os.path.exists(dist_folder_path):
        return

    for item in os.listdir(dist_folder_path):
        item_path = os.path.join(dist_folder_path, item)

        if os.path.isdir(item_path):
            delete_folder(item_path)
        else:
            print(f"Deleting file: {item_path}")
            os.remove(item_path)

    os.rmdir(dist_folder_path)


def copy_folder(source: str, destination: str):
    if not os.path.exists(source):
        raise Exception(f"Source folder {source} does not exist")

    if not os.path.exists(destination):
        raise Exception(f"Destination folder {destination} does not exist")

    for item in os.listdir(source):
        item_source_path = os.path.join(source, item)
        item_destination_path = os.path.join(destination, item)

        if os.path.isdir(item_source_path):
            print(
                f"Copying folder: {item_source_path} to {item_destination_path}")
            os.mkdir(item_destination_path)
            copy_folder(item_source_path, item_destination_path)
        else:
            print(
                f"Copying file: {item_source_path} to {item_destination_path}")
            shutil.copyfile(item_source_path, item_destination_path)


if __name__ == "__main__":
    main()
