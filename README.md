# pyPicDeMo
pyPicDeMo is a simple GUI tool designed to help you manage your image files by allowing you to easily move or delete photos within a specified folder. This tool was created as a side project and is provided "as-is" without any warranty or guarantees of support.

## Features

- **Browse Folders:** Easily select a folder containing images to review.
- **Move Images:** Move selected images to a predefined folder specified in the configuration file.
- **Delete Images:** Send unwanted images to the trash with a single click.
- **Filename Display:** View the filename of the currently displayed image.

## System and Software Requirements
-Python 3.6 or higher
-Pip
-Pillow (installed via pip)
-send2trash (installed via pip)

## Getting Started

** pyPicDeMo has only been tested in Windows! **

1. **Clone the Repository:**
   ```
   git clone https://github.com/n-damien/pyPicDeMo.git
   cd pyPicDeMo

   Install Required Libraries:
        Make sure you have Python 3.x installed.
        Install the required libraries with:
          pip install Pillow send2trash
   ```

Configure the Application:

   ```
    Edit the config.json file to set the path of the folder where you want to move images:

    {
        "move_to_folder": "C:/path/to/your/destination/folder"
    }
   ```

Run the Application:

   ```
    Run the script:

          python pyPicDeMo.py

   ```

## Usage

1. **Browse Folder:**
   - Click "Browse Folder" to select the directory containing your images.

2. **Move Image:**
   - Click "MOVE" to move the current image to the predefined folder.

3. **Delete Image:**
   - Click "DELETE" to send the current image to the trash.

## Disclaimer

No Warranty: This software is provided "as is," without any express or implied warranty. In no event will the authors be held liable for any damages arising from the use of this software.

Use at Your Own Risk: The user assumes all responsibility for the use and installation of this software. The authors make no guarantees about the suitability of this software for any particular purpose.

No Maintenance: This project was created as a side project and there are no plans for maintaining or updating it in the future.

License

## License

pyPicDeMo is licensed under the GNU General Public License v3.0. You are free to redistribute and modify this software under the terms of the GPL.

This project is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this project. If not, see [https://www.gnu.org/licenses/](https://www.gnu.org/licenses/).

## Source Code

The complete source code for pyPicDeMo is available in this repository. You may modify and redistribute it under the terms of the GNU General Public License.

## Contributions

By contributing to this project, you agree that your contributions will be licensed under the GNU General Public License.

Acknowledgments

This project was collaboratively developed by Damien and ChatGPT.
