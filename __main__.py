# coding: utf-8
"""
Export a \"My Clippings.txt\" Kindle file to HTML5.
"""

import sys
import re
import os
import argparse
from Klipps import (read_file,
                    clipps_str_to_html_str,
                    style_html_str,
                    save_str_as_file,
                    open_file)

__version__ = "0.5"
__author__ = "Rafał Karoń <rafalkaron@gmail.com.com>"

def main():
    parser = argparse.ArgumentParser(description="Convert your Kindle clippings to HTML.")
    parser.add_argument('clipps_path', help=r'A file path to the "My Clippings.txt" file on your Kindle device that you want to convert to HTML. For example: "D:\Kindle\Documents\My Clippings.txt" (Windows) or "/Volumes/Kindle/documents/My Clippings.txt" (macOS). Remember to encapsulate the path in inverted commas!')
    parser.add_argument("-nopr", "--no_preview", action="store_true", help="Prevents the converted files from opening.")
    parser.add_argument("-ns", "--no_style", action = "store_true",help="Does not style the HTML file by embedding CSS syntax.")
    try:
        args = parser.parse_args()
    except:
        parser.print_help()
        sys.exit(0)
    
    html_str = clipps_str_to_html_str(read_file(args.clipps_path))
    if not args.no_style:
        html_str = style_html_str(html_str)
    publish_html5 = save_str_as_file(html_str, args.clipps_path.replace(".txt", ".html"))
    if not args.no_preview:
        open_file(publish_html5)

if __name__ == "__main__":
    main()