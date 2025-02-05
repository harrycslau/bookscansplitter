from pypdf import PdfWriter, PdfReader

inFile  = "inputs/090-123.pdf"
outFile = "outputs/090-123.pdf"

with open(inFile, "rb") as in_f:
    input1 = PdfReader(in_f)
    output = PdfWriter()

    numPages = len(input1.pages)
    print("document has %s pages." % numPages)


    # on Mac, use Preview -> Tools -> Show Inspector -> CropBox,
    # and set the Unit to Points to get the cropbox values.
    # lower_left is really lower left, so Y is (page_height - top)
    for i in range(numPages):
        page = input1.pages[i]
        page.cropbox.lower_left = (65, 22)
        page.cropbox.upper_right = (520, 702)
        output.add_page(page)
        page.cropbox.lower_left = (515, 22)
        page.cropbox.upper_right = (985, 702)
        output.add_page(page)


    with open(outFile, "wb") as out_f:
        output.write(out_f)