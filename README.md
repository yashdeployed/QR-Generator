# QR-Generator
# QR-Generator

A simple Python script that generates QR codes from text or URLs.

## Features

- Generate a QR code from any text input or URL
- Save the generated QR code as an image file
- Lightweight, single-script implementation

## Requirements

- Python 3.x
- `qrcode` library (and `Pillow` if not already installed)

Install dependencies:

```bash
pip install qrcode[pil]
```

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/yashdeployed/QR-Generator.git
   cd QR-Generator
   ```

2. Run the script:

   ```bash
   python QR.py
   ```

3. Enter the text or URL you want to encode when prompted.

4. The generated QR code will be saved as an image in the project folder.

## Example

```bash
$ python QR.py
Enter text or URL: https://github.com/yashdeployed
QR code saved as qr_code.png
```
