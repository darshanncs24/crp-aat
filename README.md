# Enhancement of LSB Steganography Using Randomized Pixel Embedding

## Overview

**Enhancement of LSB Steganography Using Randomized Pixel Embedding** is a security-focused project that improves traditional Least Significant Bit (LSB) image steganography by introducing **password-based randomized pixel embedding** and **cryptographic protection**. The project combines image steganography, encryption, and authentication mechanisms to securely hide and retrieve confidential information within digital images.

The system consists of two integrated modules:

1. **Steganography Encoder/Decoder Desktop Application (Tkinter)**
2. **Secure Authentication Web Application (Flask)**

By randomizing pixel selection using a password-dependent shuffling algorithm, the hidden data becomes significantly more resistant to unauthorized extraction and steganalysis attacks compared to conventional sequential LSB embedding techniques.

---

## Objectives

* Enhance traditional LSB steganography using randomized pixel embedding.
* Improve security through password-based pixel shuffling.
* Encrypt secret messages before embedding.
* Maintain high image quality after data embedding.
* Provide a secure image-based authentication mechanism.
* Evaluate image quality using PSNR metrics.

---

## Key Features

### Randomized Pixel Embedding

* Password-based pixel shuffling.
* Non-sequential data hiding locations.
* Increased resistance against steganalysis attacks.

### Cryptographic Security

* Fernet symmetric encryption.
* PBKDF2-HMAC-SHA256 key derivation.
* Password-protected message extraction.

### Desktop Application

* Encode secret messages into images.
* Decode hidden messages from images.
* Calculate PSNR and MSE values.
* User-friendly graphical interface.

### Web Authentication System

* Student login verification.
* Secure image-based authentication.
* Session management.
* Protected dashboard access.

---

## Proposed Methodology

### Encoding Process

1. User enters a secret message and password.
2. Secret message is encrypted using Fernet encryption.
3. Encryption key is generated using PBKDF2-HMAC-SHA256.
4. Image pixels are shuffled using a password-dependent Linear Congruential Generator (LCG).
5. Encrypted binary data is embedded into the Least Significant Bits of randomized pixels.
6. Stego image is generated and stored.

### Decoding Process

1. User selects the stego image.
2. Same password is provided.
3. Pixel positions are regenerated using the password.
4. Hidden binary data is extracted.
5. Extracted data is decrypted.
6. Original message is recovered.

---

## System Architecture

```text
+----------------------+
| Secret Message Input |
+----------+-----------+
           |
           v
+----------------------+
| Fernet Encryption    |
+----------+-----------+
           |
           v
+----------------------+
| Randomized Pixel     |
| Selection using LCG  |
+----------+-----------+
           |
           v
+----------------------+
| LSB Data Embedding   |
+----------+-----------+
           |
           v
+----------------------+
| Stego Image Output   |
+----------------------+

```

---

## Technologies Used

### Programming Language

* Python 3.x

### Frameworks

* Flask
* Tkinter

### Libraries

* NumPy
* Pillow (PIL)
* OpenCV
* Cryptography

### Security Components

* Fernet Encryption
* PBKDF2-HMAC-SHA256
* Password-Based Randomized Pixel Embedding

---

## Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/enhanced-lsb-steganography.git
cd enhanced-lsb-steganography
```

### Install Dependencies

```bash
pip install flask numpy pillow cryptography opencv-python
```

Or use:

```bash
pip install -r requirements.txt
```

---

## Running the Desktop Application

```bash
python stegano_app.py
```

### Available Functions

#### Encode Message

* Enter password.
* Enter secret message.
* Select cover image.
* Save stego image.

#### Decode Message

* Enter password.
* Select stego image.
* Recover hidden message.

#### PSNR Analysis

* Select original image.
* Select stego image.
* View MSE and PSNR values.

---

## Running the Flask Authentication Module

```bash
python app.py
```

Access the application through:

```text
http://127.0.0.1:5000
```

---

## Security Mechanisms

### Password-Based Pixel Shuffling

The project uses a custom Linear Congruential Generator (LCG) to generate deterministic randomized pixel positions based on the user's password.

Benefits:

* Prevents sequential extraction attacks.
* Increases embedding unpredictability.
* Enhances data confidentiality.

### Encryption Layer

Before embedding, messages are encrypted using Fernet symmetric encryption.

### Key Generation

PBKDF2-HMAC-SHA256 is used to derive secure encryption keys from user passwords with 100,000 iterations.

---

## Image Quality Evaluation

The project evaluates visual distortion using:

### Mean Squared Error (MSE)

```text
MSE = Σ(Original - Stego)² / N
```

### Peak Signal-to-Noise Ratio (PSNR)

```text
PSNR = 10 × log10((255²) / MSE)
```

Higher PSNR values indicate better image quality and lower visual distortion.

---

## Project Structure

```text
project/
│
├── app.py
├── stegano_app.py
├── templates/
│   ├── login.html
│   └── dashboard.html
│
├── temp/
│   └── upload.png
│
├── requirements.txt
│
└── README.md
```

---

## Advantages of the Proposed System

* Enhanced security compared to traditional LSB methods.
* Randomized embedding locations.
* Password-dependent extraction process.
* Encryption before embedding.
* Minimal impact on image quality.
* Suitable for secure communication and authentication applications.

---

## Future Scope

* Dynamic salt generation.
* Multi-image embedding.
* Video steganography support.
* Cloud-based authentication system.
* Deep-learning-based steganalysis resistance.
* Database integration for large-scale deployments.
* Mobile application development.

---

## Applications

* Secure data transmission.
* Digital authentication systems.
* Confidential document sharing.
* Military and defense communications.
* Secure academic record verification.
* Cybersecurity research.

---

## Conclusion

This project presents an enhanced approach to traditional LSB steganography by incorporating randomized pixel embedding and cryptographic protection. The combination of password-based pixel shuffling, encryption, and image-quality preservation significantly improves the security and robustness of hidden data communication while maintaining high visual fidelity of the cover image.

---

## License

This project is intended for academic, educational, and research purposes.
