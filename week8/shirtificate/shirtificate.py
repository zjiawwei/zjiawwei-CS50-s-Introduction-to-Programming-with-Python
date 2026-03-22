from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font("Helvetica",style="B",size=36)
        self.set_text_color(0,0,0)
        self.cell(
        0,
        40,
        text="CS50 Shirtificate",
        ln=True,
        align="C"
        )

def main():
    name = input("What's your name?").strip()

    pdf = PDF(orientation='P', unit='mm', format='A4')
    pdf.add_page()
    
    image_width = 180
    image_x = (210 - image_width) / 2
    pdf.image("shirtificate.png",x = image_x, y = 50, w = image_width)

    pdf.set_font("Helvetica","B",28)
    pdf.set_text_color(255,255,255)
    pdf.set_y(140)
    pdf.cell(
        0,
        10,
        name,
        ln=True,
        align="C"
    )

    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()
