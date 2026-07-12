import qrcode

url = input("Enter the URL: ").strip()
if not url:
    print("Error: No URL entered!")
    exit()
file_path= r"D:\ALL-CODES\Python Codes\Mini-Projects\QR\Qr.png"


qr= qrcode.QRCode()
qr.add_data(url)
qr.make(fit=True)

Img=qr.make_image()
Img.save(file_path)
print("QR Generated Successfully!!") 
print(f"Saved at: {file_path}")




