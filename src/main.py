import os
import shutil
import sys

from copystatic import copy_files_recursive
from gencontent import generate_pages_recursive  # Import the new function

dir_path_static = "./static"
dir_path_public = "docs"
dir_path_content = "./content"
template_path = "./template.html"


def main():
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    else:
        basepath = "/"

    print(f"Using basepath: {basepath}")

    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_public)

    print("Generating pages...")
    # Replace the single generate_page call with the recursive version
    generate_pages_recursive(
        dir_path_content,
        template_path,
        dir_path_public,
        basepath
    )


main()