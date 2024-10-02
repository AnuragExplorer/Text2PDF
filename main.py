from fpdf import FPDF

# Function to convert text to PDF
def text_to_pdf(text, output_filename):
    pdf = FPDF()  # Create a PDF object
    pdf.add_page()  # Add a page
    pdf.set_font("Arial", size=12)  # Set font and size

    # Add text to the PDF
    pdf.multi_cell(0, 10, text)  

    # Save the PDF to a file
    pdf.output(output_filename)
    print(f"PDF saved as {output_filename}")

# Main function
def main():
    # Ask the user for input text
    user_text = input("Enter the text you want to convert to PDF: ")
    
    # Ask the user for the output PDF filename
    filename = input("Enter the filename for the PDF (e.g., 'output.pdf'): ")

    # Convert the text to PDF
    text_to_pdf(user_text, filename)

if __name__ == "__main__":
    main()

