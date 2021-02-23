import glob
from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from io import StringIO
from io import open
from urllib.request import urlopen

def lerPDF(arquivoPDF):
    recursos = PDFResourceManager()
    buffer = StringIO()
    layoutParams = LAParams()
    dispositivo = TextConverter(recursos, buffer, laparams=layoutParams)

    process_pdf(recursos, dispositivo, arquivoPDF)
    dispositivo.close()

    conteudo = buffer.getvalue()
    buffer.close()
    return conteudo

for filepath in glob.iglob('*.pdf'):
    # print(filepath)
    nome = str(filepath).replace(".pdf","")
    print(nome)

    arquivoPDF = open(filepath,"rb")
    saida = lerPDF(arquivoPDF)
    # print(saida)
    with open(nome+".txt", 'w', encoding='utf-8') as f:
            f.write(saida)

    arquivoPDF.close()