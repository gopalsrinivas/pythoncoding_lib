import PyPDF2
import pyttsx3


def pdf_to_audio(pdf_path):
    try:
        # Open the PDF file
        with open(pdf_path, "rb") as file:
            # Create a PDF reader object
            pdf_reader = PyPDF2.PdfReader(file)

            # Initialize the text-to-speech engine
            tts_engine = pyttsx3.init()

            # Iterate through each page and extract text
            for page_number in range(len(pdf_reader.pages)):
                try:
                    page = pdf_reader.pages[page_number]
                    text = page.extract_text()

                    if text.strip():  # Check if the page contains text
                        tts_engine.say(text)
                        tts_engine.runAndWait()
                    else:
                        print(
                            f"Page {page_number + 1} is empty or contains unsupported content."
                        )

                except Exception as e:
                    print(f"Error reading page {page_number + 1}: {e}")

            # Stop the TTS engine
            tts_engine.stop()

    except FileNotFoundError:
        print(f"Error: File '{pdf_path}' not found. Please check the file path.")

    except PyPDF2.errors.PdfReadError as e:
        print(f"Error reading the PDF file: {e}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Replace 'dummy_pdf.pdf' with the path to your PDF file
pdf_path = "dummy_pdf.pdf"
pdf_to_audio(pdf_path)
