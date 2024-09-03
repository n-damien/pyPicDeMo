# pyPicDeMo
pyPicDeMo is a simple GUI tool designed to help you manage your image files by allowing you to easily move or delete photos within a specified folder. This tool was created as a side project and is provided "as-is" without any warranty or guarantees of support.

## Features

- **Browse Folders:** Easily select a folder containing images to review.
- **Move Images:** Move selected images to a predefined folder specified in the configuration file.
- **Delete Images:** Send unwanted images to the trash with a single click.
- **Filename Display:** View the filename of the currently displayed image.

## Getting Started

** pyPicDeMo has only been tested in Windows! **

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/n-damien/pyPicDeMo.git
   cd pyPicDeMo

    Install Required Libraries:
        Make sure you have Python 3.x installed.
        Install the required libraries with:

    pip install Pillow send2trash

Configure the Application:

    Edit the config.json file to set the path of the folder where you want to move images:

    json

    {
        "move_to_folder": "C:/path/to/your/destination/folder"
    }

Run the Application:

    Run the script:

          python pyPicDeMo.py

Disclaimer

No Warranty: This software is provided "as is," without any express or implied warranty. In no event will the authors be held liable for any damages arising from the use of this software.

Use at Your Own Risk: The user assumes all responsibility for the use and installation of this software. The authors make no guarantees about the suitability of this software for any particular purpose.

No Maintenance: This project was created as a side project and there are no plans for maintaining or updating it in the future.

License

This project is licensed under the GNU License. See the LICENSE file for more details.
Acknowledgments

This project was collaboratively developed by Damien and ChatGPT.
