# 🖼️ Image Steganography
This project is a desktop-based application that allows users to hide secret messages within images (Encoding) and extract hidden messages from images (Decoding). It uses the CustomTkinter library to create a user-friendly GUI and implements LSB (Least Significant Bit) Steganography for hiding data within images.

# 🎯 Features
- Encode Text into Images: Hide secret messages inside .png, .jpg, or .jpeg images.
- Decode Messages: Extract hidden messages from encoded images.
- Modern GUI: Developed using CustomTkinter for a sleek appearance.
- Appearance Modes: Switch between light, dark, or system modes.
- Image Preview: Displays the selected image for both encoding and decoding.
- Info & Help: Easy access to application information and assistance.

# 🛠️ Technologies Used
- Python: Backend logic and GUI.
- CustomTkinter: Modern-looking widgets and GUI components.
- Pillow (PIL): For handling image files and operations.
- Tkinter: Basic GUI functionality and file dialogs.

# 📁 Installation and Setup
Clone the repository:

```bash
git clone <repository-url>
cd Image-Steganography
```

Install the dependencies: Make sure you have Python 3.x installed, then run:

```bash
pip install -r requirements.txt
```
Run the application:

```bash
python stegno_app.py
```

# 🧑‍💻 How to Use
Encoding a Message:

- Open the app and click Encode.
- Select the image where you want to hide the message.
- Enter your secret message in the text area.
- Click Encode to save the new image with the hidden text.

Decoding a Message:

- Click Decode from the main menu.
- Select the image containing the hidden message.
- The hidden message will appear in the text box.
- Changing Appearance Mode:

Use the dropdown menu at the bottom of the main screen to toggle between Light, Dark, or System appearance modes.

# 📝 Code Overview
Key Functions

Encoding Process:

- genData(data): Converts the text message into binary format.
- modPix(pix, data): Modifies the image pixels based on the message.
- encode_enc(newimg, data): Places the encoded pixels into the new image.
- enc_fun(text_area, myimg): Encodes the message and saves the new image.

Decoding Process:

- decode(image): Extracts hidden data from the image pixels.

# 💡 Appearance Modes
- Light Mode: Clean white theme for better visibility in bright environments.
- Dark Mode: Eye-friendly dark theme.
- System Mode: Follows the default system theme.

# 📦 Folder Structure
```bash
Image-Steganography/
│
├── stegno_app.py         # Main application file
├── README.md             # Project documentation
└── requirements.txt      # Dependencies (optional)
```

# ⚠️ Error Handling
- If no image or message is selected, the app shows an error message.
- If the encoding or decoding process fails, a popup alert is triggered.

# 🤖 Future Improvements
- Drag and Drop support for selecting files.
- Password Protection for encoding and decoding.
- Support for Audio or Video Steganography.


# 📧 Contact

For any issues or improvements, please feel free to reach out.