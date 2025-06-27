# static page generator
Static page generator powered by a Markdown to HTML converter.

## Table of Contents

* [About The Project](#about-the-project)
* [Key Features](#key-features)
* [Built With](#built-with)
* [Getting Started](#getting-started)
    * [Prerequisites](#prerequisites)
    * [Installation](#installation)
    * [How to Use](#how-to-use)
    * [Example](#example)
* [Roadmap](#roadmap)
* [Acknowledgments](#acknowledgments)

## About The Project

This project is a custom-built static site generator written in Python. It takes Markdown files as input, converts them into HTML pages, and organizes them into a static website. It also handles copying static assets like CSS files to the output directory.

## Key Features

* **Markdown to HTML Conversion:** Converts Markdown content into well-structured HTML.
* **Static Page Generation:** Generates individual HTML pages from Markdown files using a provided HTML template.
* **Recursive Directory Processing:** Recursively processes Markdown files and copies static content from source directories to the destination.
* **Template Integration:** Replaces placeholders (`{{ Title }}` and `{{ Content }}`) in the HTML template with extracted title and converted Markdown content.
* **Static File Copying:** Copies static assets (like CSS files) from a designated `static` directory to the output `docs` directory.

## Built With

* Python 3

## Getting Started

To get a local copy up and running, follow these simple steps.

### Prerequisites

* Python 3 installed on your system.

### Installation

1.  Clone this repository:
    ```bash
    git clone [https://github.com/Sanghun1Adam1Park/static-page-generator](https://github.com/Sanghun1Adam1Park/static-page-generator)
    ```
2.  Navigate to the project directory:
    ```bash
    cd static-page-generator
    ```

### How to Use

The generator can be run using the `main.sh` script or by directly executing the `main.py` script.

* Run the generator:
    ```bash
    ./main.sh
    ```
    or
    ```bash
    python3 src/main.py
    ```

* Run with a specified base path (useful for deployment to subdirectories):
    ```bash
    ./build.sh
    ```
    or
    ```bash
    python3 src/main.py "/your-base-path/"
    ```

### Example

The project includes example Markdown files in the `content/` directory and a `template.html` file. Running the generator will convert these into HTML pages in the `docs/` directory, along with the `index.css` file from the `static/` directory.

For example, the `content/blog/glorfindel/index.md` file will be converted to `docs/blog/glorfindel/index.html`.

## Roadmap

* Improve Markdown parsing to support more complex syntax.
* Add support for custom themes and styling.
* Implement a live-reload feature for development.
* Enhance error handling and logging.

## Acknowledgments

* [Boot.dev - Backend dev Tutorial](https://www.boot.dev/courses/build-static-site-generator-python)