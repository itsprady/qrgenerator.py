import qrcode
from PIL import Image

# Get user input for the QR code data
qr_data = input("Enter the URL or text for the QR code: ")

# Create a QR code
qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H,
                   box_size=10, border=4)
qr.add_data(qr_data)
qr.make(fit=True)

# Generate the QR code image
img = qr.make_image(fill_color="black", back_color="white")

# Get user input for the output image filename
output_filename = input("Enter the output image filename (e.g., mbbchannel2.png): ")

# Save the QR code image
img.save(output_filename)
print(f"QR code saved as {output_filename}")
