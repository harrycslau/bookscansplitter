# bookscansplitter
When you scan a book, usually we scan both pages together.
This script helps split scanned book PDF from two-page format to individual page format, based on PyPdf3 library.

## How to Use
1. Measure the size of the book when opened. The scan area can be a bit larger.
2. Scan the book.
    - Make sure the left and top edges aligned with the scanning platform.
    - Prefer around 40-80 pages (20-40 scans) each time.
    - 10 pages (5 scans) take around 1 minute
3. Rename the file according to page number, e.g. 002-021.pdf
4. On Mac, open the scanned PDF with Preview.
5. In Preview, choose Tools -> Show Inspector -> CropBox, then and set the Unit to Points to get the cropbox values. Note that lower_left is really lower left.
    - Upper right Y is (page_height - top)
    - Lower left Y is (page_height - top + height)

## Example
- Scan area: X = 350 mm, Y = 250 mm
- Crop (lower_left) (upper_right)
    - Page 002-021: Left (65, 22) (515, 702); Right (535, 22) (985, 702)
    - Page 022-063: Left (70, 22) (520, 702); Right (535, 22) (985, 702)
    - Page 064-089: Left (70, 22) (520, 702); Right (535, 22) (985, 702)
    - Page 090-123: Left (65, 22) (515, 702); Right (535, 22) (985, 702)