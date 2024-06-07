# import PyPDF2


# def pdf_to_text(file_path):
#     text = ""
#     with open(file_path, "rb") as f:
#         reader = PyPDF2.PdfFileReader(f)
#         for page_num in range(reader.numPages):
#             text += reader.getPage(page_num).extractText()
#     return text
