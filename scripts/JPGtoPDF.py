from PIL import Image

image_1 = Image.open(r'C:\Users\luke1\Desktop\projects\JPGTOPDF\data\役男徵兵檢查.jpg')
im_1 = image_1.convert('RGB')
im_1.save(r'C:\Users\luke1\Desktop\projects\JPGTOPDF\data\役男徵兵檢查.pdf')