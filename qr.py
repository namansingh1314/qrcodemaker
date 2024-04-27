import pyqrcode
import png
from pyqrcode import QRCode
  
  
# replace the link with your desired link 
s = "https://drive.google.com/drive/folders/1--"
  
# for Generating QR code
url = pyqrcode.create(s)
  
# Create and save the svg file naming "myqr.svg"
url.svg("myqr.svg", scale = 8)
  
# Create and save the png file naming "myqr.png"
url.png('myqr.png', scale = 6)
