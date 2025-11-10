import os
import shutil

from src.utils.extract_title import extract_title
from src.utils.markdown_to_html_node import markdown_to_html_node


STATIC_FOLDER_PATH = "static"
DIST_FOLDER_PATH = "public"


def main():
    move_static_files_to_public()

    # Generate a page from content/index.md using template.html and write it to public/index.html.
    generate_page(
        from_path="content/index.md",
        template_path="template.html",
        dest_path="public/index.html",
    )


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


def generate_page(from_path: str, template_path: str, dest_path: str):
    print(
        f"Generating page from {from_path} to {dest_path} using {template_path}")

    markdown_str = ""
    with open(from_path, "r") as file:
        markdown_str = file.read()

    template_str = ""
    with open(template_path, "r") as file:
        template_str = file.read()

    title = extract_title(markdown_str)
    html_str = markdown_to_html_node(markdown_str).to_html()

    final_html_str = template_str.replace(
        "{{ Title }}", title).replace("{{ Content }}", html_str)

    with open(dest_path, 'w') as file:
        file.write(final_html_str)


if __name__ == "__main__":
    main()
