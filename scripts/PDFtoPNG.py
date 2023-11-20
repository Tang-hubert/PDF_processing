import aspose.pdf as ap
import io

DIR_OUTPUT = r'C:\Users\luke1\Desktop\projects\PDF_processing'

input_pdf = r'C:\Users\luke1\Desktop\projects\PDF_processing\document-page5.pdf'
output_pdf = DIR_OUTPUT + "\convert_pdf_to_png"

# 打開 PDF 文檔
document = ap.Document(input_pdf)

# 創建分辨率對象
resolution = ap.devices.Resolution(300)
device = ap.devices.PngDevice(resolution)

for i in range(0, len(document.pages)):
    # 創建文件保存
    imageStream = io.FileIO(
        output_pdf + "_page_" + '5' + "_out.png", 'x'
    )
    
    # 轉換特定頁面並將圖像保存到流
    device.process(document.pages[i + 1], imageStream)
    imageStream.close()
