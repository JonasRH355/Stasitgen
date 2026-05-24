from textnode import TextNode, TextType
from os import path, listdir, mkdir
from shutil import copy, rmtree 

from copystatic import *

dir_static = "./static"
dir_public = "./public"

def main():
    if path.exists(dir_public):
        rmtree("./public")
    copy_files_recursive(dir_static, dir_public)

    pass

main()