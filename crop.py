from pypdf import PdfWriter, PdfReader

inFile  = "inputs/002-043.pdf"
outFile = "outputs/out.pdf"

with open(inFile, "rb") as in_f:
    input1 = PdfReader(in_f)
    output = PdfWriter()

    numPages = len(input1.pages)
    print("document has %s pages." % numPages)

    for i in range(numPages):
        page = input1.pages[i]
        page.cropbox.lower_left = (30, 10)
        page.cropbox.upper_right = (550, 730)
        output.add_page(page)
        page.cropbox.lower_left = (580, 10)
        page.cropbox.upper_right = (1100, 730)
        output.add_page(page)


    with open(outFile, "wb") as out_f:
        output.write(out_f)