import pymupdf
doc = pymupdf.open('BEC613A.pdf')
full_text = " "
for i in doc:
  full_text += i.get_text()
  print(full_text)
