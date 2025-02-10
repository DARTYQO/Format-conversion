@staticmethod
def convert_docx_to_pdf(input_file, output_file):
    # רישום הפונט העברי
    pdfmetrics.registerFont(TTFont('David', 'C:\\Windows\\Fonts\\david.ttf'))
    
    doc = Document(input_file)
    c = canvas.Canvas(output_file, pagesize=letter)
    c.setFont("David", 12)  # שימוש בפונט דוד
    
    y_position = 800
    for para in doc.paragraphs:
        text = para.text
        c.drawString(72, y_position, text)
        y_position -= 20
        if y_position < 50:
            c.showPage()
            c.setFont("David", 12)  # חשוב להגדיר מחדש את הפונט בכל עמוד
            y_position = 800
    c.save()

    @staticmethod
    def merge_pdfs(input_files, output_file):
        merger = PdfMerger(strict=False)  # הוספת strict=False לטיפול בקבצים בעייתיים
        for pdf in input_files:
            merger.append(pdf)
        merger.write(output_file)
        merger.close()

    @staticmethod
    def split_pdf(input_file, output_dir):
        reader = PdfReader(input_file, strict=False)  # הוספת strict=False לטיפול בקבצים בעייתיים
        for i, page in enumerate(reader.pages):
            writer = PdfWriter()
            writer.add_page(page)
            output_path = os.path.join(output_dir, f'page_{i+1}.pdf')
            with open(output_path, 'wb') as output_file:
                writer.write(output_file)
