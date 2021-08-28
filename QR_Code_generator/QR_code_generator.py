import pyqrcode
from pyqrcode import QRCode

url = 'https://github.com/'

qr_code = pyqrcode.create(url)

qr_code.svg('github_qr.svg' , scale = 10)