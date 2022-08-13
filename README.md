# Kampus Konnect

A marketing website for Kampus konnect: a platform for short movies created by college students.

##### Table of Contents

[Description](#desc)

[Live Demo](#demo)

[Built With](#built)

Authors

[Getting Started](#started)

    - [Dependencies](#depend)
    - [Installation](#install)

[License](#license)

[Version History](#version)


<a name="desc" />
## Description

We are focused on providing a way for college students to share their creative ideas among their peers. They can start conversations around a thought or idea, create educational content, or simply fun creative content that serve as outlets for their creativity. This repository 

### Live Demo

The site is presently hosted at [@Kampus Konnect](https://kampus-konnect.netlify.app)

### Built With

The website is built with
- HTML
- CSS
- Netlify
- [Figma](https://www.figma.com/file/lylckSVblnwTfXIxcl3bNE/Video-Display?node-id=179%3A438)
- [DataBase Schema](https://app.diagrams.net/#G1wtzgJG3QADuNnowGzx___eC6y_d1ihZA) 

### Authors

Contributors names and contact info

#### Designers
- [Olaosebikan Enitan](https://github.com/orgs/zuri-training/people/hennyitan)
- [Chidimma Madu](https://github.com/orgs/zuri-training/people/Mara-mma)
- [Adeniji Adejoke Omolara](https://github.com/orgs/zuri-training/people/AdenijiOmolara)
- [Obiahor Jesse](https://github.com/orgs/zuri-training/people/Jessesnr)
- [Mary Eneh](https://github.com/orgs/zuri-training/people/Mary-Eneh)
- [Concillia Nwaigwe](https://github.com/orgs/zuri-training/people/Lyia-n)
- [Musa Morenikeji](https://github.com/orgs/zuri-training/people/M-Morenny-M-36)

#### Developer 

- [Ukanah Dean](https://github.com/orgs/zuri-training/people/Harrylever)
- [Uthman Damilola](https://github.com/orgs/zuri-training/people/D-uth)
- [Chizoba Udechukwu](https://github.com/orgs/zuri-training/people/videlleudeh)


## Getting Started


This is a python-django web-app.

### Dependencies

Language - Python
Text editor - PyCharm, VSCode or other IDEs
Version control - Git, GitHUB account
Web browser - FireFox, Microsoft Edge, Google Chrome...


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



## LICENSE. 

This code is under MIT Licensing. Details of License [here](License).




## Version History

* 0.1
    * Initial Release
