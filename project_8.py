# QR code encoder / decoder

import qrcode

def create_qr_code(data, filename="qr_code.png"):
    # Create a QR code from the input data
    qr = qrcode.QRCode(
        version=1,  # size of the QR code (1 = smallest)
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,  # size of each box in pixels
        border=4      # border around the QR code
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)
    print(f"✅ QR Code successfully saved as '{filename}'.")

def main():
    text = input("Enter text or URL to encode as QR code: ")
    filename = input("Enter filename to save (default: qr_code.png): ").strip()
    if not filename:
        filename = "qr_code.png"
    create_qr_code(text, filename)

if __name__ == "__main__":
    main()
