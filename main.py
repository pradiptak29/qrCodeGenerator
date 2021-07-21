import qrcode
qrg = input("Enter the URL:-\t")
img = qrcode.make(qrg)
img.save("myQR.jpg")
print("Your QR image is successfully generated.\nPlease check your destination folder")