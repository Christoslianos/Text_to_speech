import PyPDF2
import pyttsx3
import pdfplumber
from tkinter import *
from tkinter.filedialog import askopenfilename

# create an interface for user to load pdf files
window = Tk()
window.geometry('400x200')
window.configure(background='pink')
window.title('PDF to Audio')


# open a file
def upload_pdf_file():
    file = askopenfilename()
    f = open(file, "rb")
    pdf_Reader = PyPDF2.PdfFileReader(f)
    pages = pdf_Reader.numPages

    with pdfplumber.open(file) as pdf:
        new_text = ""
        # configure the engine
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)
        # loop the pages
        for i in range(0, pages):
            page = pdf.pages[i]
            text = page.extract_text()
            new_text += text
            engine.say(new_text)
            engine.runAndWait()
        engine.stop()
        # save the file as  mp3 when i finished the audiobook
        engine.save_to_file(new_text, "audio.mp3")
        engine.runAndWait()


# create a label
label = Label(text="Choose a pdf file to convert", font=('Arial', 15))
label.pack(pady=10)

# create a button
button = Button(text="Upload a pdf", command=upload_pdf_file)
button.pack()
window.mainloop()
