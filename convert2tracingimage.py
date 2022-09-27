from pdf2image import convert_from_path
import os

while(True):
    dir = input("Masukkan direktori dokumen (pdf): ").strip('\"')
    paper_size = input("A3 atau A4? ")
    paper_orientation = input("landscape atau portrait (l/p)? ")
    screen_height = float(input("Masukkan tinggi layar anda (vertikal, mm): "))
    screen_height_pixels = int(input("masukkan jumlah piksel dalam tinggi layar anda: "))
    pages = convert_from_path(dir,500)

    if paper_size.lower() == "a3" and (paper_orientation.lower() == "l" or paper_orientation.lower() == "landscape"):
        paper_vertical_height = 297


    if paper_size.lower() == "a3" and (paper_orientation.lower() == "p" or paper_orientation.lower() == "portrait"):
        paper_vertical_height = 420


    if paper_size.lower() == "a4" and (paper_orientation.lower() == "l" or paper_orientation.lower() == "landscape"):
        paper_vertical_height = 210


    if paper_size.lower() == "a4" and (paper_orientation.lower() == "p" or paper_orientation.lower() == "portrait"):
        paper_vertical_height = 297


    
    i = 1
    for page in pages:
        scale_factor = paper_vertical_height*screen_height_pixels/screen_height
        print('scale factor: ' + str(scale_factor))
        width, height = page.size
        page = page.resize((int(width*scale_factor/height) ,int(scale_factor)))
        dir = dir.rstrip('.pdf')
        savedir = dir + ' tracing'
        print("akan di simpan di: " + savedir)
        try:
            os.mkdir(savedir)
        except OSError:
            print("gagal membuat folder atau folder sudah dibuat")
        else:
            print("folder berhasil dibuat")

        page.save(savedir + '\\' + 'out (' + str(i) + ')' + '.png')
        i += 1