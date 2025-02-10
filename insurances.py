from pypdf import PdfReader, PdfWriter
import os

vehicles = ("BH87MT", "BH11LI", "BH11LL", "BH25LL", "BJ92JU", "BJ95JU", "BJ93JU", "BJ97JU", "BJ98JU", "BG03RV", "BG16RV", "BG33RV", "BH06LE", "BH56LE", "03UG18", "85ZQ59", "AI82BH")

newpath = "/Users/leonardoabreu/Downloads/insurances"
if not os.path.exists(newpath):
    os.makedirs(newpath)

reader = PdfReader("/Users/leonardoabreu/Downloads/insurances.pdf")
writer = PdfWriter()
for i in range(len(vehicles)):
    writer.add_page(reader.pages[i*2])
    with open(f"/Users/leonardoabreu/Downloads/insurances/{vehicles[i]}.pdf", "wb") as fp:
        writer.write(fp)
    writer.remove_page(0)
