from util import cp, generate_page, generate_page_recursively
import sys 
import os

if __name__ == "__main__":
    basepath = sys.argv[1] if len(sys.argv) > 1 else "/"

    os.makedirs("docs", exist_ok=True)
    cp("static", "docs")
    generate_page_recursively(basepath, "template.html", "docs")
