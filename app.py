from flask import Flask, render_template, request, redirect, session
import numpy as np
from PIL import Image
import os
from cryptography.fernet import Fernet
import base64
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

app = Flask(__name__)
app.secret_key = "key"

students = {
    "101": {
        "name": "Darshan N",
        "course": "BSc IT",
        "secret": "secure101"
    },
    "102": {
        "name": "Mehta",
        "course": "BCA",
        "secret": "secure102"
    }
}


def get_shuffled_indices(width, height, password):
    total_pixels = width * height
    indices = list(range(total_pixels))

    seed = sum(ord(c) for c in password)

    a = 1664525
    c = 1013904223
    m = 2**32

    curr = seed

    for i in range(total_pixels - 1, 0, -1):
        curr = (a * curr + c) % m
        j = curr % (i + 1)
        indices[i], indices[j] = indices[j], indices[i]

    return indices


def get_crypto_key(password):
    salt = b'constant_salt_2026'
    kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=100000)
    return base64.urlsafe_b64encode(kdf.derive(password.encode()))

def decode_image(image_path, password):
    img = Image.open(image_path).convert("RGB")
    pixels = np.array(img)

    h, w, _ = pixels.shape
    flat_pixels = pixels.reshape(-1, 3)

    shuffled_idx = get_shuffled_indices(w, h, password)

    all_bits = ""
    pixel_ptr = 0

    while True:
        idx_group = shuffled_idx[pixel_ptr:pixel_ptr + 3]
        pixel_ptr += 3

        rgb_block = []
        for idx in idx_group:
            rgb_block.extend(flat_pixels[idx])

        # extract 8 bits
        for i in range(8):
            all_bits += str(rgb_block[i] % 2)

        # stop bit
        if rgb_block[8] % 2 != 0:
            break

    try:
        byte_data = int(all_bits, 2).to_bytes((len(all_bits) + 7) // 8, 'big')
        key = get_crypto_key(password)
        f = Fernet(key)
        decrypted = f.decrypt(byte_data)
        return decrypted.decode().strip()
    except Exception:
        return ""



@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":

        roll = request.form["roll"]
        password = request.form["password"]
        image = request.files["image"]

        # check student exists
        if roll not in students:
            return render_template("login.html", error="Invalid Roll ❌")

        student = students[roll]

        os.makedirs("temp", exist_ok=True)
        path = "temp/upload.png"
        image.save(path)

        result = decode_image(path, password)

        if result.strip() == student["secret"]:
            session["user"] = roll
            return redirect("/dashboard")

        return render_template("login.html", error=f"Invalid Credentials ❌ (Decoded: {result})")

    return render_template("login.html")


@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect("/")

    student = students[session["user"]]
    return render_template("dashboard.html", student=student)

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)