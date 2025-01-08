from PyPDF2 import PdfWriter

# merger variable that holds our input
merger = PdfWriter()


# input each file the order we want to merge them
input1 = open("dummy.pdf", "rb")
input2 = open("wtr.pdf", "rb")
input3 = open("twopage.pdf", "rb")




# append entire input at the end of previous file
merger.append(input1)
merger.append(input2)
merger.append(input3)


output = open("merged-output.pdf", "wb")

merger.write(output)

# Close File Descriptors
merger.close()
output.close()
