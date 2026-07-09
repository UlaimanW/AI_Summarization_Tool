import re
import os
import arabic_reshaper
from bidi.algorithm import get_display
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from datetime import datetime


FONT_PATH = os.path.join(
    "fonts",
    "a-arslan-wessam-a-a-arslan-wessam-a",
    "(A) Arslan Wessam A (A) Arslan Wessam A",
    "(A) Arslan Wessam A (A) Arslan Wessam A.ttf"
)
FONT_NAME = "ArabicFont"


def clean_file_name(file_name):
    file_name = file_name.strip()
    file_name = file_name.replace(" ", "_")
    file_name = re.sub(r'[\\/:*?"<>|]', '', file_name)

    if not file_name:
        current_time = datetime.now().strftime("%Y-%m-%d_%H-%M")
        file_name = f"summary_{current_time}"

    return file_name


def create_txt(summary, file_name):
    with open(f"{file_name}.txt", "w", encoding="utf-8") as file:
        file.write(summary)


def contains_arabic(text):
    return any("\u0600" <= char <= "\u06FF" for char in text)


def prepare_text_for_pdf(text):
    if contains_arabic(text):
        reshaped_text = arabic_reshaper.reshape(text)
        return get_display(reshaped_text)

    return text


def create_pdf(summary, file_name):
    if not os.path.exists(FONT_PATH):
        raise FileNotFoundError(
            "Arabic font not found. Please add NotoNaskhArabic-Regular.ttf inside the fonts folder."
        )

    pdfmetrics.registerFont(TTFont(FONT_NAME, FONT_PATH))

    pdf = canvas.Canvas(f"{file_name}.pdf", pagesize=A4)
    width, height = A4

    x = 50
    y = height - 50
    max_width = width - 100
    font_size = 12

    pdf.setFont(FONT_NAME, font_size)

    for paragraph in summary.split("\n"):
        words = paragraph.split()
        line = ""

        for word in words:
            test_line = line + word + " "

            if pdf.stringWidth(prepare_text_for_pdf(test_line), FONT_NAME, font_size) <= max_width:
                line = test_line
            else:
                prepared_line = prepare_text_for_pdf(line.strip())

                if contains_arabic(line):
                    pdf.drawRightString(width - 50, y, prepared_line)
                else:
                    pdf.drawString(x, y, prepared_line)

                y -= 20
                line = word + " "

                if y < 50:
                    pdf.showPage()
                    pdf.setFont(FONT_NAME, font_size)
                    y = height - 50

        if line:
            prepared_line = prepare_text_for_pdf(line.strip())

            if contains_arabic(line):
                pdf.drawRightString(width - 50, y, prepared_line)
            else:
                pdf.drawString(x, y, prepared_line)

            y -= 20

            if y < 50:
                pdf.showPage()
                pdf.setFont(FONT_NAME, font_size)
                y = height - 50

    pdf.save()