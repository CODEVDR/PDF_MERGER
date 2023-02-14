import os
import tkinter.messagebox as msg
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
from pypdf import *

root = Tk()
root.title("Pdf Merger")
root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")
root.iconbitmap("assets/icon.ico")
Label(root, text="PDF MERGER", font="impact 35 bold", relief=SOLID).pack(pady=50)

frmaddFiles = Frame(root)
# For Button Images
img = Image.open("assets/addfile_img.png")
r_img = img.resize((200, 200))
image = ImageTk.PhotoImage(r_img)
img1 = Image.open("assets/up_img.png")
r_img1 = img1.resize((200, 200))
image1 = ImageTk.PhotoImage(r_img1)


def merge_pdfs(paths):
    try:
        pdf_writer = PdfWriter()
        output = "merged.pdf"
        for path in paths:
            pdf_reader = PdfReader(path)
            for page in range(len(pdf_reader.pages)):
                # Add each page to the writer object
                pdf_writer.add_page(pdf_reader.pages[page])

        # Write out the merged PDF
        with open(output, 'wb') as out:
            pdf_writer.write(out)
        msg.showinfo("Merged", "Merged File Sucessfully")
    except:
        msg.showerror(
            "Error", "An Unexpected Error Caught We'll Solve it Soon.Please Check For Updates and Try Again Later")


i = 0
fileNames = []


def adBtn():
    filename = filedialog.askopenfilename(
        initialdir="/", title="Select a File", filetypes=(("PDF files", "*.pdf*"), ("all files", "*.*")))
    global i
    if i < 4 and filename != "":
        fileNames.append(filename)
        addBtn.pack_forget()
        tmpFrm = Frame(frmaddFiles)
        file = Label(tmpFrm, image=image1, relief=SOLID)
        file.pack()
        Label(tmpFrm, text=f"{fileNames[i]}", relief=SOLID).pack(side=BOTTOM)
        tmpFrm.pack(side=LEFT)
        addBtn.pack()
        i += 1
    elif filename == "":
        msg.showwarning("Warning", "No File Selected")
    else:
        msg.showerror("Error", "Can't Merge More Files")


# For Adding Files
addBtn = Button(frmaddFiles, image=image, relief=SOLID, command=adBtn)
addBtn.pack(side=LEFT, padx=10)


def mergePDF():
    if fileNames != []:
        merge_pdfs(fileNames)
    else:
        msg.showerror("Error", "No File Selected")


img2 = Image.open("assets/btn_img.png")
image2 = ImageTk.PhotoImage(img2)
frmaddFiles.pack(pady=100)
mergeBtn = Button(root, image=image2, relief=SOLID, command=mergePDF)
mergeBtn.pack(pady=50)
root.mainloop()
