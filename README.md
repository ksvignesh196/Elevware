# Elevware

## Overview

Elevware is an educational ransomware simulation developed in Python as part of a cybersecurity academic project. The project demonstrates how ransomware can encrypt files, display a ransom notification, and restore files using a valid decryption key within a controlled environment.

The purpose of this project is to help students, researchers, and cybersecurity enthusiasts understand ransomware behavior, malware analysis concepts, encryption workflows, and defensive security strategies.

---

## Features

* File encryption simulation
* File decryption using a valid key
* Ransom notification display
* Executable generation using PyInstaller
* Educational demonstration of ransomware behavior
* Controlled-environment testing

---

## Technologies Used

* Python 3
* Cryptography Libraries
* PyInstaller
* Tkinter

---

## Project Workflow

1. Develop the ransomware simulation in Python.
2. Convert the Python script into a Windows executable using PyInstaller.
3. Execute the program in a controlled environment.
4. Encrypt selected files using cryptographic techniques.
5. Display a ransom notification.
6. Restore encrypted files through the decryption process.
7. Analyze ransomware behavior and security implications.

---

## Repository Contents

```text
Elevware/
├── elevware.py      # Educational ransomware simulation source code
├── elevware.exe     # Windows executable build generated using PyInstaller
├── img.jpg          # Sample image used during delivery technique research
├── img.ico          # Executable icon resource
└── README.md
```

---

## Executable Packaging Research

The Elevware Python script was converted into a Windows executable using PyInstaller to study how malware can be packaged and distributed in executable form.

As part of the research, an image-based delivery technique was explored in which the generated executable was intended to be bundled with an image file. This experiment was conducted solely for educational purposes to understand malware concealment and delivery methods commonly discussed in cybersecurity research and malware analysis.

During testing, Microsoft Defender and other security mechanisms automatically detected and removed the generated executable and packaged files. Due to these security protections, the final packaged image artifact could not be preserved and therefore is not included in this repository.

For this reason, only the source code, executable, image resource, and project documentation are provided.

---

## Educational Objectives

This project was created to study:

* Ransomware behavior
* File encryption mechanisms
* Malware packaging concepts
* Malware delivery techniques
* Incident response fundamentals
* Defensive cybersecurity strategies
* Antivirus detection capabilities

---

## Important Notice

⚠️ **Default Decryption Password:** `asdfasdf`

⚠️ **Run Only in a Controlled Environment**

This project is capable of encrypting files. Although it was developed for educational and research purposes, running it on a personal system may result in unintended file encryption or modification.

It is strongly recommended to execute Elevware only inside a virtual machine, isolated laboratory environment, or other controlled testing setup.

Before running the program, ensure that:

* Important files are backed up.
* The test environment is isolated from production systems.
* You understand the encryption and decryption process.

The default password required for decryption is:

```text
asdfasdf
```

Failure to use the correct password may prevent access to encrypted files until the proper decryption key is provided.


## Disclaimer

⚠️ This project was developed strictly for educational, research, and cybersecurity awareness purposes. It was created and tested only in controlled environments.

The author does not endorse, support, or encourage the use of ransomware or similar software on unauthorized systems. Any misuse of this project is solely the responsibility of the user.

---

## Reference

The image-based executable packaging concept explored during this project was inspired by publicly available cybersecurity demonstrations and educational resources.

YouTube Reference:
https://www.youtube.com/watch?v=cXEkSQl9wmw

Note: The final packaged image file is not included in this repository because modern antivirus solutions, including Microsoft Defender, automatically detected and removed the generated artifacts during testing.
