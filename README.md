# FileZilla Credential Extractor

A PyQt6 GUI application to parse and view FileZilla server exports. It automatically decodes base64-encoded passwords and presents them in a clean, searchable table format.

## Features

* **Automatic Base64 Decoding**: Instantly view your saved passwords without manual decoding
* **Search Functionality**: Dynamic filtering of server entries for quick access
* **Modern UI**: Clean, dark-mode inspired interface built with PyQt6
* **XML Validation**: Ensures you are loading a valid FileZilla export file
* **Table View**: Organized display of all server credentials in an easy-to-read format
* **Cross-Platform**: Works on Windows, macOS, and Linux

## Setup & Installation

### Option 1: Using the Executable (Recommended for Windows Users)

**No Python installation required!**

1. **Download the Latest Release:**
   * Go to the [Releases](https://github.com/Deadpool2000/filezilla-credentials-extractor/releases) page
   * Download the latest `.exe` file

2. **Run the Application:**
   * Double-click the downloaded `.exe` file
   * Windows may show a security warning - click "More info" then "Run anyway"
   * The application will start immediately

### Option 2: Running from Source

### Prerequisites

* Python 3.7 or higher

### Installation Steps

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Deadpool2000/filezilla-credentials-extractor
   cd filezilla-credentials-extractor
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application:**
   ```bash
   python xml_viewer.py
   ```

## Usage

### Exporting XML from FileZilla

To get the XML file required for this tool:

1. Open **FileZilla Client**
2. Go to **File** > **Export...**
3. Check **"Export Site Manager entries"**
4. Save the file to your computer
5. Load this file using the "Load XML File" button in the application

### Viewing Credentials

1. Click the **"Load XML File"** button in the application
2. Select your exported FileZilla XML file
3. View all server entries with decoded passwords in the table
4. Use the search bar to filter specific entries

## Security Notice

⚠️ **Important**: This tool is designed for legitimate password recovery and management purposes only. Please ensure you:

* Only use this tool on XML files you own or have permission to access
* Store exported XML files securely as they contain sensitive credentials
* Delete or encrypt exported XML files after use
* Never share your credential files with unauthorized parties

## Requirements

* Python 3.7+
* PyQt6
* xml.etree.ElementTree (included in Python standard library)
* base64 (included in Python standard library)

See `requirements.txt` for specific version requirements.

## Troubleshooting

### Common Issues

**Executable Issues (Windows):**
* **Windows Defender/Antivirus blocking:** Some antivirus software may flag the .exe as suspicious. This is a false positive common with PyInstaller executables. You can add an exception or run from source
* **Application won't start:** Try running as administrator or check if your antivirus quarantined the file
* **"VCRUNTIME140.dll missing" error:** Download and install [Microsoft Visual C++ Redistributable](https://aka.ms/vs/17/release/vc_redist.x64.exe)

**Python Version Issues:**
* Ensure all dependencies are installed: `pip install -r requirements.txt`
* Verify Python version: `python --version` (should be 3.7+)
* Try using `python3` instead of `python` on some systems

**Can't load XML file:**
* Ensure the file is a valid FileZilla export
* Check that the XML file isn't corrupted
* Verify you selected "Export Site Manager entries" when exporting

**Passwords not showing:**
* Some FileZilla versions may use different encoding methods
* Ensure your FileZilla export includes password data


## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the GNU GPL 3.0 License - see the LICENSE file for details.

## Author

**Your Name**
* GitHub: [@YDeadpool2000](https://github.com/Deadpool2000)
* Email: d2kyt@protonmail.com
* LinkedIn: [Connect Me](https://linkedin.com/in/salil-mhatre-d2k)



## Disclaimer

This tool is provided for educational and legitimate password recovery purposes only. The author is not responsible for any misuse of this software. Always respect privacy and security laws in your jurisdiction.

---

⭐ If you find this project useful, please consider giving it a star on GitHub!