### Country-Abbreviations

[![File Number](https://img.shields.io/github/directory-file-count/toniilic1/Country-Abbreviations "File Number")](https://github.com/toniilic1/Country-Abbreviations)
[![Size](https://img.shields.io/github/repo-size/toniilic1/Country-Abbreviations)](https://github.com/toniilic1/Country-Abbreviations)
[![Commits](https://img.shields.io/github/commit-activity/m/toniilic1/Country-Abbreviations)](https://github.com/toniilic1/Country-Abbreviations/graphs/commit-activity)
[![License](https://img.shields.io/github/license/toniilic1/Country-Abbreviations "License")](https://github.com/toniilic1/Country-Abbreviations/blob/master/LICENSE.txt "License")

## Introduction

Upon establishing communication with the ```SOAP``` server, client may request one of 4 abbreviations; "be, az, fr and de". And in return; corresponding country name is printed in the console.

The XML structure is created on the server side which contains a dictonairy of four countries and their abbreviations as keys. XML is created using ```xml.etree.ElementTree module```. Then on the client side; using ```zeep``` we connect to the server to read the XML document and generate a response; return a country name.

Point of this project is to give an example of using an ```API```, specifically ElementTree XML, and also inspect a WSDL document with zeep and to return a response.

## Installation
1. Clone the project:
- ```git clone https://github.com/toniilic1/Country-Abbreviations```

2. Create a virtual env:
- ```py -m venv .venv```
- ```.venv\scripts\activate```

3. Install the zeep and spyne:
- ```pip install zeep```
- ```pip install spyne```
or
- ```pip install -r requirements.txt```

## License

MIT
