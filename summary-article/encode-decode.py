import base64

string = 'string'
# print(base64.b64encode(string)) 에러
bString = string.encode('utf-8')
print(bString)
encoding = base64.b64encode(bString)
print(encoding)
decoding = base64.b64decode(encoding)
print(decoding)
decoding_str = decoding.decode('utf-8')
print(decoding_str)

from PIL import Image

path = 'img.png'
# img = Image.open(path)
with open(path, 'rb') as img:
    image = img.read()

print(image)

from bitstring import BitArray

input_str = '0xff'
c = BitArray(hex=input_str)
print(c.bin)

with open(path, 'rb') as img1:
    data = img1.read()
    encoded = base64.b64encode(data)
    print(encoded)

decoded = base64.decodebytes(encoded)
print(decoded)

file = "img1.png"

with open(file, 'wb') as file:
    file.write(decoded)
