LaTeX DIN Letter Template (DIN 5008)
====================================

Template generator for LaTeX Letters according to DIN 5008.

Requirements
------------
Install `cookiecutter` command line: `pip install cookiecutter`

Usage
-----
Generate a new Cookiecutter template layout: `cookiecutter gh:ethylomat/letter`    

Example
-------
```console
# Create a project directory
foo@bar:~$ cookiecutter gh:ethylomat/letter
title []: Testbrief
From_name [Maximilian Mustermann]: 
From_addr [Musterstraße 1\\11010 Musterstadt]: 
From_addr_short [Musterstraße 1\\10000 Musterstadt]: 
From_phone [+49 111 - 222 333 44]: 
From_email [mustermann@example.com]: 
To_name [Max Mustermann]: 
To_addr [Max Mustermann\\Musterstraße 42\\11010 Musterstadt]: 
Date [today]: 
Place [Musterstadt]: 
Subject []: Gute Nachrichten
Enclosings []: 
Signature [y]: 
foo@bar:~$ ls Brief-Testbrief
head.tex      main.tex      signature.png
```

Compile LaTeX document via `lualatex main.tex`  

Configuration
-------------
To configure the letter template settings edit the file `cookiecutter.json`.

To edit the template files navigate to the directory: `Brief-{{cookiecutter.title}}`


License
-------
This project is licensed under the terms of the [MIT License](/LICENSE)
