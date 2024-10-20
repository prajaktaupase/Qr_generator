import qrcode

qr_img = qrcode.make("welcome to @thecodecompiler")

qr_img.save ("qr-img.jpg")
