# Kampus Konnect

A marketing website for Kampus konnect: a platform for short movies created by college students.

## Table of Contents

[Description](#desc)

[Live Demo](#demo)

[Built With](#built)

[Authors](#authors)

[Getting Started](#started)

* [Dependencies](#depend)
* [Installation](#install)

[License](#license)

[Version History](#version)


<a name="desc"></a>

## Description

We are focused on providing a way for college students to share their creative ideas among their peers. They can start conversations around a thought or idea, create educational content, or simply fun creative content that serve as outlets for their creativity. This repository 

<a name="demo"></a>
### Live Demo

The site is presently hosted at [@Kampus Konnect](https://kampus-konnect.netlify.app)

<a name="built"></a>
### Built With

The website is built with
- HTML
- CSS
- Python - Django
- Postgres
- [Figma](https://www.figma.com/file/lylckSVblnwTfXIxcl3bNE/Video-Display?node-id=179%3A438)

A snapshot of our DB schema can be seen [here](https://app.diagrams.net/#G1wtzgJG3QADuNnowGzx___eC6y_d1ihZA) 

<a name="authors"></a>
### Authors

Contributors names and contact info

#### Designers
- [Olaosebikan Enitan](https://github.com/hennyitan)
- [Faith Ime](https://github.com/Calejay)
- [Oladele Taiwo](https://github.com/Jedstitches)
- [Chidimma Madu](https://github.com/Mara-mma)
- [Adeniji Adejoke Omolara](https://github.com/AdenijiOmolara)
- [Obiahor Jesse](https://github.com/Jessesnr)
- [Mary Eneh](https://github.com/Mary-Eneh)
- [Concillia Nwaigwe](https://github.com/Lyia-n)
- [Musa Morenikeji](https://github.com/M-Morenny-M-36)
-[Kikelomo Nicole Mariam Peter](https://github.com/kikenicole)

### Developers
- [Ukanah Dean](https://github.com/Harrylever)
- [Uthman Damilola](https://github.com/D-uth)
- [Chizoba Udechukwu](https://github.com/videlleudeh)
- [Isaac Franklin](https://github.com/orgs/Isaac-Franklin)
- [Imotola Titilope Abisola Barakat](https://github.com/iwalewa-x)
- [Ibrahim Mohammed](https://github.com/Bandastic018)
- [Adeboga Abigail](https://github.com/bogadeji)


<a name="started"></a>
## Getting Started

This is a python-django web-app.

<a name="depend"></a>
### Dependencies

Language - Python
Text editor - PyCharm, VSCode or other IDEs
Version control - Git, GitHUB account
Web browser - FireFox, Microsoft Edge, Google Chrome...

<a name="install"></a>
### Installation

To install and successfully run this web app on your device, go to your terminal, i.e. cmd, powershell or gitbash. Then you;

    CLONE REPOSITORY

    git clone https://github.com/zuri-training/kk-platform.git


This will clone the whole repository as a folder on your local machine.

CREATE VIRTUAL ENVIRONMENT

Be for yo create your virtual environment, first move into the project folder, i.e. the cloned folder.

Using the terminal,

    cd kk-platform

    In the project folder, confirm the folder contains manage.py file

    ls

To see the various files in the folder and cofirming the existence of a manage.py file.

    Now create your virtual environment.

    python -m venv env

Note: env is the name of the virtual environment (you can decide what it should be)

OR

    pip install virtualenv env

Note env is the name of the virtual environment (you can decide what it should be)

ACTIVATE VIRTUAL ENVIRONMENT

After installing virtual environment, it should be activated BEFORE anyother activity.

    For git bash;

    $source \env\Scripts\activate

    For cmd;

    env/scripts/activate


Note: env should be replaced by the name used for  the virtual environment when it was created.


Also, after activation, please confirm that the name of the virtual environment is in brackets on top or at the begining of the commandline.


INSTALL REQUIREMENTS


    Now install project requirements using:

    pip install -r requirements.txt


This will install all the requirements in the requirements.txt file which includes django.


RUN SERVER


    Now that django is installed, local server can be initiated.

    python manage.py runserver


The link below will appear in the terminal which will redirect you to the webpage. 

(http://127.0.0.1:8000/)


<a name="license"></a>
## LICENSE. 

This code is under MIT Licensing. Details of License [here](License).

<a name="version"></a>
## Version History

* 0.1
    * Initial Release
