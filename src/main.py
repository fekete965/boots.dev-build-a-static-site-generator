import os
import shutil
import sys

from src.utils.extract_title import extract_title
from src.utils.markdown_to_html_node import markdown_to_html_node


STATIC_FOLDER_NAME = "static"
DIST_FOLDER_NAME = "docs"
CONTENT_FOLDER_NAME = "content"
TEMPLATE_FILE_NAME = "template.html"


def main():
    # Get the base path from the command line arguments
    base_path = sys.argv[1]

    # If the base path is not provided, default to "/"
    if not base_path:
        base_path = "/"

    # Move the static files to the dist folder
    move_static_files_to_dist()

    # Define the paths for the content folder, template file, and dist folder
    cwd = os.getcwd()
    content_folder_path = os.path.join(cwd, CONTENT_FOLDER_NAME)
    template_file_path = os.path.join(cwd, TEMPLATE_FILE_NAME)
    dist_folder_path = os.path.join(cwd, DIST_FOLDER_NAME)

    # Generate a page from content/index.md using template.html and write it to public/index.html.
    generate_content(
        folder_path=content_folder_path,
        template_file_path=template_file_path,
        dist_folder_path=dist_folder_path,
    )


def generate_content(folder_path: str, template_file_path: str, dist_folder_path: str) -> list[str]:
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)

        # If the item is a directory, generate the content for the directory
        if os.path.isdir(item_path):
            # Get the new dist folder path
            new_dist_folder_path = os.path.join(dist_folder_path, item)
            # Create the new dist folder if it doesn't exist
            if not os.path.exists(new_dist_folder_path):
                os.makedirs(new_dist_folder_path)

            # Continue the recursive call
            generate_content(
                folder_path=item_path,
                template_file_path=template_file_path,
                dist_folder_path=new_dist_folder_path,
            )
        # If the item is an index.md file, generate the page for the item
        elif item == "index.md":
            # Get the new dist folder path
            new_dist_folder_path = os.path.join(
                dist_folder_path, item.replace(".md", ".html"))

            # Generate the page for the item
            generate_page(
                from_path=item_path,
                template_path=template_file_path,
                dest_path=new_dist_folder_path,
            )


def move_static_files_to_dist():
    cwd = os.getcwd()

    static_folder_path = os.path.join(cwd, STATIC_FOLDER_NAME)
    if not os.path.exists(static_folder_path):
        raise Exception(f"Static folder {static_folder_path} does not exist")

    dist_folder_path = os.path.join(cwd, DIST_FOLDER_NAME)

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
        f"\nGenerating page from {from_path} to {dest_path} using {template_path}")

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
