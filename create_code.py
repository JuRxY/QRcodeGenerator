import qrcode

def make_code(content, name):
    img = qrcode.make(str(content))
    img.save(str(name)+".png")