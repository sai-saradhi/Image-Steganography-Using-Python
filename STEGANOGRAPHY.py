import customtkinter
import tkinter
from customtkinter import *
from customtkinter import CTk
import tkinter.filedialog
from PIL import ImageTk, Image
from tkinter import messagebox
from io import BytesIO
import os

class Stegno:

    output_image_size = 0

    def main(self, root):
        root.title('ImageSteganography')
        root.geometry('500x390')
        root.resizable(False, False)
        f = CTkFrame(root)

        title = CTkLabel(f, text='Image Steganography')
        title.configure(font=('courier', 44))
        title.grid(pady=10)

        b_encode = CTkButton(f, text="Encode", command=lambda: self.frame1_encode(f), height=35, corner_radius=16)
        b_encode.configure(font=('courier', 24))
        b_encode.grid(padx=14, pady=24)
        b_decode = CTkButton(f, text="Decode", command=lambda: self.frame1_decode(f), height=35, corner_radius=16)
        b_decode.configure(font=('courier', 24))
        b_decode.grid(padx=14, pady=24)
        b_info = CTkButton(f, text="Info", command=lambda: self.show_info_frame(f), height=35, corner_radius=16)
        b_info.configure(font=('courier', 24))
        b_info.grid(padx=14, pady=24)
        b_help = CTkButton(f, text="Help", command=lambda: self.show_help_frame(f), height=35, corner_radius=16)
        b_help.configure(font=('courier', 24))
        b_help.grid(row=6, column=0, padx=10, pady=(0, 10), sticky="se")

        appearance_mode_label = customtkinter.CTkLabel(f, text="Appearance Mode:", anchor="w")
        appearance_mode_label.grid(row=5, column=0, padx=10, pady=(0, 10), sticky="w")
        appearance_mode_optionemenu = customtkinter.CTkOptionMenu(f, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        appearance_mode_optionemenu.grid(row=6, column=0, padx=10, pady=(0, 10), sticky="w")

        

        root.grid_rowconfigure(1, weight=1)
        root.grid_columnconfigure(0, weight=1)

        f.grid()
        title.grid(row=1)
        b_encode.grid(row=2)
        b_decode.grid(row=3)
        b_info.grid(row=4)

    def home(self, frame):
        frame.destroy()
        self.main(root)

    def frame1_decode(self, f):
        f.destroy()
        d_f2 = CTkFrame(root)      
        l1 = CTkLabel(d_f2, text='Select Image with Hidden text:')
        l1.configure(font=('courier', 18))
        l1.grid()
        bws_button = CTkButton(d_f2, text='Select', command=lambda: self.frame2_decode(d_f2))
        bws_button.configure(font=('courier', 18))
        bws_button.grid()
        back_button = CTkButton(d_f2, text='Cancel', command=lambda: Stegno.home(self, d_f2))
        back_button.configure(font=('courier', 18))
        back_button.grid(pady=15)
        back_button.grid()
        d_f2.grid()

    def frame2_decode(self, d_f2):
        root.geometry('500x625')
        d_f3 = CTkFrame(root)
        myfile = tkinter.filedialog.askopenfilename(
            filetypes=([('png', '*.png'), ('jpeg', '*.jpeg'), ('jpg', '*.jpg'), ('All Files', '*.*')]))
        if not myfile:
            messagebox.showerror("Error", "You have selected nothing !")
        else:
            myimg = Image.open(myfile, 'r')
            myimage = myimg.resize((300, 200))
            img = ImageTk.PhotoImage(myimage)
            l4 = CTkLabel(d_f3, text='Selected Image :')
            l4.configure(font=('courier', 18))
            l4.grid()
            panel = CTkLabel(d_f3, text="", image=img)
            panel.image = img
            panel.grid()
            hidden_data = self.decode(myimg)
            l2 = CTkLabel(d_f3, text='Hidden data is :')
            l2.configure(font=('courier', 18))
            l2.grid(pady=10)
            text_area = CTkTextbox(d_f3, width=500, height=250)
            text_area.insert(INSERT, hidden_data)
            text_area.configure(state='disabled')
            text_area.grid()
            back_button = CTkButton(d_f3, text='Cancel', command=lambda: self.page3(d_f3))
            back_button.configure(font=('courier', 11))
            back_button.grid(pady=15)
            back_button.grid()
            show_info = CTkButton(d_f3, text='More Info', command=self.info)
            show_info.configure(font=('courier', 11))
            show_info.grid()
            d_f3.grid(row=1)
            d_f2.destroy()

    def decode(self, image):
        data = ''
        imgdata = iter(image.getdata())

        while (True):
            pixels = [value for value in imgdata.__next__()[:3] +
                      imgdata.__next__()[:3] +
                      imgdata.__next__()[:3]]
            binstr = ''
            for i in pixels[:8]:
                if i % 2 == 0:
                    binstr += '0'
                else:
                    binstr += '1'

            data += chr(int(binstr, 2))
            if pixels[-1] % 2 != 0:
                return data

    def frame1_encode(self, f):
        f.destroy()
        f2 = CTkFrame(root)
        l1 = CTkLabel(f2, text='Select the Image in which \nyou want to hide text :')
        l1.configure(font=('courier', 18))
        l1.grid()

        bws_button = CTkButton(f2, text='Select', command=lambda: self.frame2_encode(f2))
        bws_button.configure(font=('courier', 18))
        bws_button.grid()
        back_button = CTkButton(f2, text='Cancel', command=lambda: Stegno.home(self, f2))
        back_button.configure(font=('courier', 18))
        back_button.grid(pady=15)
        back_button.grid()
        f2.grid()


    def frame2_encode(self, f2):
        root.geometry('500x625')
        ep = CTkFrame(root)
        myfile = tkinter.filedialog.askopenfilename(
            filetypes=([('png', '*.png'), ('jpeg', '*.jpeg'), ('jpg', '*.jpg'), ('All Files', '*.*')]))
        if not myfile:
            messagebox.showerror("Error", "You have selected nothing !")
        else:
            myimg = Image.open(myfile)
            myimage = myimg.resize((300, 200))
            img = ImageTk.PhotoImage(myimage)
            l3 = CTkLabel(ep, text='Selected Image')
            l3.configure(font=('courier', 18))
            l3.grid()
            panel = CTkLabel(ep, text="", image=img)
            panel.image = img
            self.output_image_size = os.stat(myfile)
            self.o_image_w, self.o_image_h = myimg.size
            panel.grid()
            l2 = CTkLabel(ep, text='Enter the message')
            l2.configure(font=('courier', 18))
            l2.grid(pady=15)
            text_area = CTkTextbox(ep, width=500 ,height=250)
            text_area.grid()
            encode_button = CTkButton(ep, text='Cancel', command=lambda: Stegno.home(self, ep))
            encode_button.configure(font=('courier', 11))
            data = text_area.get("1.0", "end-1c")
            back_button = CTkButton(ep, text='Encode', command=lambda: [self.enc_fun(text_area, myimg),
                                                                      Stegno.home(self, ep)])
            back_button.configure(font=('courier', 11))
            back_button.grid(pady=15)
            encode_button.grid()
            ep.grid(row=1)
            f2.destroy()

    def info(self):
        try:
            str = 'original image:-\nsize of original image:{}mb\nwidth: {}\nheight: {}\n\n' \
                  'decoded image:-\nsize of decoded image: {}mb\nwidth: {}' \
                  '\nheight: {}'.format(self.output_image_size.st_size / 1000000,
                                         self.o_image_w, self.o_image_h,
                                         self.d_image_size / 1000000,
                                         self.d_image_w, self.d_image_h)
            messagebox.showinfo('info', str)
        except:
            messagebox.showinfo('Info', 'Unable to get the information')

    def genData(self, data):
        newd = []

        for i in data:
            newd.append(format(ord(i), '08b'))
        return newd

    def modPix(self, pix, data):
        datalist = self.genData(data)
        lendata = len(datalist)
        imdata = iter(pix)
        for i in range(lendata):
            pix = [value for value in imdata.__next__()[:3] +
                   imdata.__next__()[:3] +
                   imdata.__next__()[:3]]
            for j in range(0, 8):
                if (datalist[i][j] == '0') and (pix[j] % 2 != 0):
                    if (pix[j] % 2 != 0):
                        pix[j] -= 1
                elif (datalist[i][j] == '1') and (pix[j] % 2 == 0):
                    pix[j] -= 1
            if (i == lendata - 1):
                if (pix[-1] % 2 == 0):
                    pix[-1] -= 1
            else:
                if (pix[-1] % 2 != 0):
                    pix[-1] -= 1
            pix = tuple(pix)
            yield pix[0:3]
            yield pix[3:6]
            yield pix[6:9]

    def encode_enc(self, newimg, data):
        w = newimg.size[0]
        (x, y) = (0, 0)

        for pixel in self.modPix(newimg.getdata(), data):
            newimg.putpixel((x, y), pixel)
            if (x == w - 1):
                x = 0
                y += 1
            else:
                x += 1

    def enc_fun(self, text_area, myimg):
        data = text_area.get("1.0", "end-1c")
        if (len(data) == 0):
            messagebox.showinfo("Alert", "Kindly enter text in TextBox")
        else:
            newimg = myimg.copy()
            self.encode_enc(newimg, data)
            my_file = BytesIO()
            temp = os.path.splitext(os.path.basename(myimg.filename))[0]
            newimg.save(tkinter.filedialog.asksaveasfilename(initialfile=temp, filetypes=([('png', '*.png')]),
                                                              defaultextension=".png"))
            self.d_image_size = my_file.tell()
            self.d_image_w, self.d_image_h = newimg.size
            messagebox.showinfo("Success", "Encoding Successful\nFile is saved as Image_with_hiddentext.png in the same directory")

    def page3(self, frame):
        frame.destroy()
        self.main(root)

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def show_help_frame(self, f):
        f.destroy()
        root.geometry('725x315')
        help_frame = CTkFrame(root)

        # Help text
        help_text = """
        Welcome to Image Steganography Project!

        This project allows you to hide text within an image using steganography.
        To get started:
        1. Click on the "Encode" button to hide text in an image.
        2. Click on the "Decode" button to reveal hidden text from an image.
        3. Click on the "Settings" button to customize appearance and other settings.

        For more information, please visit the documentation or contact support.

        Thank you for using Image Steganography!
        """

        # Label to display help text
        help_label = CTkLabel(help_frame, text=help_text, justify="left", font=('courier', 14))
        help_label.grid(padx=20, pady=20)

        # Button to close the help frame
        close_button = CTkButton(help_frame, text="Close", command=lambda: Stegno.home(self, help_frame), height=35, corner_radius=16)
        close_button.configure(font=('courier', 14))
        close_button.grid(padx=20, pady=10)

        root.grid_rowconfigure(1, weight=1)
        root.grid_columnconfigure(0, weight=1)

        # Display the help frame
        help_frame.grid()
        help_label.grid(row=(1))
        close_button.grid(row=(2))

    def show_info_frame(self, f):
        f.destroy()
        root.geometry('725x325')
        # Create a new frame for project information
        info_frame = CTkFrame(root)

        # Project information text
        info_text = """
        Image Steganography Project

        Creators:
        - Sai Saradhi
        - [Add Other Creators Here]

        Version: 1.0
        Release Date: [Add Release Date Here]

        For more information, please visit the project repository or contact the creators.

        Thank you for using Image Steganography!
        """

        # Label to display project information
        info_label = CTkLabel(info_frame, text=info_text, justify="left", font=('courier', 14))
        info_label.grid(padx=20, pady=20)

        # Close button
        close_button = CTkButton(info_frame, text="Close", command=lambda: Stegno.home(self, info_frame), height=35, corner_radius=16)
        close_button.configure(font=('courier', 14))
        close_button.grid(padx=20, pady=10)

        root.grid_rowconfigure(1, weight=1)
        root.grid_columnconfigure(0, weight=1)

        # Display the info frame
        info_frame.grid()
        info_label.grid(row=(1))
        close_button.grid(row=(2))



root = CTk()
o = Stegno()
o.main(root)
root.mainloop()
