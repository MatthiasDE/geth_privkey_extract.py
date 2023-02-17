# Name of the project
> Retrieves your private key from your Ethereum geth keystore file. Enabling to use your Ethereum wallet on any computer or device just with authorizing it with the private key that you can get for your personal view with this small offline-program running on your computer.

This program allows to extract your private key form the Ethereum geth keystore file. For this you just need your geth password and the location of the file. There will be no transfer of this details or file from and to the internet because it is all running on your windows computer.


## Installing / Getting started
A quick introduction of the minimal setup you need to get the program up &
running.

Prerequisites:
* Python >3.11
* Windows 11

```shell
git clone https://github.com/MatthiasDE/geth_privkey_extract.py.git
cd geth_privkey_extract.py
python -m venv .\\venv
.\\venv\Scripts\activate.bat
pip install -r requirements.txt
python geth_privkey_extract.py #and now follow the GUI :)
```

This code clones the repo. Creates a virtual environment for Python that your base python installation does not get overloaded with additional libraries. Then you activate the virtual python environment, installing the requirements (libraries) and at least starts the program.


## Features
What's all the bells and whistles this project can perform?
* It's running locally
* You can select the keystore file with dialog
* Your password is hidden and not saved (so just used at your computers end)
* Private Key is only shown locally and temporary and therefore you should write it down and store it in a safe place
* Uninstall is quite easy with deleting the cloned folder (in above example "geth_privkey_extract.py)


## Contributing
When you publish something open source, one of the greatest motivations is that
anyone can just jump in and start contributing to your project.

If you'd like to contribute, please fork the repository and use a feature
branch. Pull requests are warmly welcome.

PEP8 code style appreciated.


## Licensing
The code in this project is licensed under GPLv3 license.