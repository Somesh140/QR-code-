import qrcode
from PIL import Image

qr = qrcode.QRCode(
    version=10,
    box_size=5,
    border=5,
)
data = 'https://web.whatsapp.com/' # Type the text for which you want to create QR code you can also generate QR for any website as well example

qr.add_data(data)
qr.make(fit=True)
imag = qr.make_image(fill='black', back_color='white')
imag.get_image()
