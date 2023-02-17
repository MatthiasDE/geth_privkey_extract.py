#Credits to https://web3py.readthedocs.io/en/latest/index.html. Thanks for the hints that made this code finally runable.

import os
sUserPath = os.environ['userprofile']

from eth_account import Account

from tkinter import *
from tkinter import ttk
from tkinter import filedialog 

def openFileDialog():
    inputFile.delete(0,END)
    inputFile.insert(0, filedialog.askopenfilename(initialdir=sUserPath))

def printPrivateKey():
    import binascii

    textField.delete(1.0,END)
    
    try:
        with open(inputFile.get()) as keyfile:
            encrypted_key = keyfile.read()
            private_key = Account.decrypt(encrypted_key, inputPassword.get())
        textField.insert(END, binascii.hexlify(private_key))
    except FileNotFoundError:
        textField.insert(END, 'ERROR: File couldn\'t be found')
    except ValueError:
        textField.insert(END, 'ERROR: Password is not correct or not a keystore file')
    except OSError:
        textField.insert(END, 'ERROR: Something wrong with path & filename')
    except Exception as e:
         textField.insert(END, 'ERROR:', str(e))
    

## GUI Generation

root = Tk()
root.title('Geth Private Key Extractor')
root.geometry('750x250')

frame = Frame(root, borderwidth=2, relief=GROOVE, padx=5, pady=5)

buttonOpenFile = ttk.Button(frame, text="Open Geth Keystore", command = openFileDialog)
buttonOpenFile.grid(row=0, column=0, sticky=W)
inputFile = ttk.Entry(frame, width = 100)
inputFile.grid(row=0, column=1)

lInputPassword = ttk.Label(frame)
lInputPassword.configure(text='Keystore Password: ')
lInputPassword.grid(row=1, column=0, sticky=W)
inputPassword = ttk.Entry(frame,  show="*", width = 50)
inputPassword.grid(row=1, column=1, sticky=W)

buttonExtract = ttk.Button (frame, text="Extract Private Key", command = printPrivateKey)
buttonExtract.grid(pady=10, columnspan=2)


resultFrame = Frame(root)

lTextField = ttk.Label(resultFrame)
lTextField.configure(text='Private Key (!!KEEP SECRET!!): ')
lTextField.grid(sticky=W, columnspan=2)
textField = Text(resultFrame, width=90, height=5)
textField.grid(sticky=W, columnspan=2)

buttonQuit = ttk.Button(resultFrame, text="Quit", command=root.destroy)
buttonQuit.grid(pady=10, columnspan=2, sticky=E)

frame.pack(expand=True)
resultFrame.pack(expand=True)

root.mainloop()