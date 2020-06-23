# membuat GUI dengan build-in package tkinter

import tkinter

main_window = tkinter.Tk()

def event_tekan():
    label2 = tkinter.Label(main_window, text="aku di tekan")
    label2.pack()

label = tkinter.Label(main_window, text="hallo. saya adalah \n GUI sederhana dengan \n menggunakan Python")
tombol = tkinter.Button(main_window, text="tekan", command = event_tekan)

label.pack()
tombol.pack()
main_window.mainloop()