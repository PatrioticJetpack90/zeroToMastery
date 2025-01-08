from io import BytesIO
from pathlib import Path
from typing import List, Union
from PIL import Image
from pypdf import PageRange, PdfReader, PdfWriter, Transformation


def image_to_pdf(stamp_img: Union[Path, str]) -> PdfReader:
    img = Image.open(stamp_img)
    # Resize the image to 100x100 pixels
    img_resized = img.resize((100, 100))

    # Save the image as a PDF to an in-memory buffer
    img_as_pdf = BytesIO()
    img_resized.save(img_as_pdf, format="PDF")
    img_as_pdf.seek(0)  # Reset buffer position for reading

    # Read the in-memory PDF as a PdfReader object
    return PdfReader(img_as_pdf)


def stamp_img(
    content_pdf: Union[Path, str],
    stamp_img: Union[Path, str],
    pdf_result: Union[Path, str],
    page_indices: Union[PageRange, List[int], None] = None,
):
    # Convert the image to a PDF
    stamp_pdf = image_to_pdf(stamp_img)

    # Use the first page of the stamp PDF as the stamp
    stamp_page = stamp_pdf.pages[0]

    # Create a PDF writer
    writer = PdfWriter()

    # Read the content PDF
    reader = PdfReader(content_pdf)

    # Append pages to the writer, optionally limiting to page_indices
    writer.append(reader, pages=page_indices)

    # Add the stamp to the specified pages
    for content_page in writer.pages:
        content_page.merge_transformed_page(
            stamp_page,
            Transformation().translate(50, 50),  # Adjust position of the stamp
        )

    # Write the result to the specified output PDF
    with open(pdf_result, "wb") as fp:
        writer.write(fp)


# Example usage
stamp_img("super.pdf", "top-secret-stamp.jpg", "output.pdf")
