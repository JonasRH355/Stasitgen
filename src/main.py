from textnode import TextNode, TextType
from os import path, listdir, mkdir
from shutil import copy, rmtree 
import sys

from copystatic import *
from gencontent import *

dir_static = "./static"
dir_public = "./docs"
dir_content = "./content"
template_path = "./template.html"
default_basepath = "/"

def main():
    basepath = default_basepath
    if len(sys.argv) > 1:
        basepath = sys.argv[1]

    if path.exists(dir_public):
        rmtree(dir_public)
    copy_files_recursive(dir_static, dir_public)

    generate_pages_recursive(
        dir_content,
        template_path,
        dir_public,
        basepath
    )


main()