from PyPDF2 import PdfFileWriter, PdfFileReader

ofn = '/mnt/d/High Performance Python_ Practical Perform - Micha Gorelick.pdf'

mp = PdfFileReader(open(ofn, 'rb'))

pages = []
for i in range(mp.getNumPages()):
    if not '/Annots' in mp.getPage(i):
        continue
    annots = [ann.getObject() for ann in mp.getPage(i)['/Annots'] if ann.getObject()['/Subtype'] != '/Link']
    if len(annots) > 0:
        print(f'Page {i}: {[ann["/Subtype"] for ann in annots]}')
        pages.append({i: annots})

