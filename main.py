import customtkinter
import base64
import os
import pyperclip
import threading


class MyClass:
    def __init__(self):
        self.isMenuOpen = False

        customtkinter.set_appearance_mode("System")
        customtkinter.set_default_color_theme("blue")

        self.app = customtkinter.CTk()
        self.app.geometry("720x480")
        self.app.title("Panel Utils")

        self.contentFrameKeys = customtkinter.CTkFrame(master=self.app)
        self.contentFrameTranslate = customtkinter.CTkFrame(master=self.app)

        self.frame = customtkinter.CTkFrame(master=self.app)
        self.frame.pack(side="left", fill="y")

        generateKeyMenu = customtkinter.CTkButton(self.frame, text="AES Keys", command=self.aesKeys)
        generateKeyMenu.pack(padx=10, pady=10)

        closeButton = customtkinter.CTkButton(self.frame, text="Close", command=lambda: self.closeMenu(), fg_color='red')
        closeButton.pack(padx=10, pady=50)

        exitButton = customtkinter.CTkButton(self.frame, text="Exit", command=lambda: self.exitProgram(), fg_color='red')
        exitButton.pack(side="bottom", pady=15)

        self.app.mainloop()

    def closeMenu(self):
        self.isMenuOpen = False
        if self.contentFrameKeys.winfo_exists():
            self.contentFrameKeys.destroy()
            return

        if self.contentFrameTranslate.winfo_exists():
            self.contentFrameTranslate.destroy()
            return

    def exitProgram(self):
        exit()

    def aesKeys(self):
        if self.isMenuOpen:
            return

        self.isMenuOpen = True

        self.contentFrameKeys = customtkinter.CTkFrame(master=self.app)
        self.contentFrameKeys.pack(pady=20, padx=60, fill="both")
        key256 = customtkinter.CTkButton(self.contentFrameKeys, text="256 bits", command=lambda: generateKeyMethod(32))
        key192 = customtkinter.CTkButton(self.contentFrameKeys, text="192  bits", command=lambda: generateKeyMethod(16))
        key128 = customtkinter.CTkButton(self.contentFrameKeys, text="128 bits", command=lambda: generateKeyMethod(8))

        key256.pack(padx=10, pady=10)
        key192.pack(padx=10, pady=10)
        key128.pack(padx=10, pady=10)

        def generateKeyMethod(size):
            if generateKeyMethod.isGeneratedData:
                return

            generateKeyMethod.isGeneratedData = True

            key = base64.urlsafe_b64encode(os.urandom(size))
            pyperclip.copy(key.decode("UTF-8"))

            copyButton = customtkinter.CTkButton(self.contentFrameKeys, text="Copy",
                                                 command=lambda: self.copy(key.decode("UTF-8")), fg_color='red')
            copyButton.pack(padx=40, pady=40)
            threading.Timer(7.0, lambda: copyButton.destroy()).start()
            copyKey = customtkinter.CTkLabel(self.contentFrameKeys, text="KEY: " + key.decode("UTF-8"))
            copyKey.pack(padx=10, pady=10)
            threading.Timer(7.0, lambda: copyKey.destroy()).start()
            threading.Timer(7.0, lambda: setattr(generateKeyMethod, 'isGeneratedData', False)).start()

        generateKeyMethod.isGeneratedData = False

    def copy(self, text):
        pyperclip.copy(text)

instance = MyClass()
instance.__init__()
