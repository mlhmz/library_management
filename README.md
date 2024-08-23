# Library Management 📕

## Overview 🌻
The library management is a school assignment and is meant to manage books.

## Features ✨
* Pagination
* Sorting
* Filtering
* Borrow Books
* Delete Borrowed Book Entries
* Authentication

## Stack 🐍
* Python
* Django
* Node.js and NPM
* Tailwind CSS
* DaisyUI

## Get started 🚀

Create .venv in root directory
```bash
py -m venv .venv
```

Start .venv with the command for your os and terminal
e.g. Linux with zsh  
```bash
source .venv/bin/activate
```

Install requirements
```bash
pip install -r requirements.txt
```

Apply database migrations
```bash
py ./manage.py migrate
```

Apply fixtures
```bash
py ./fixtures.py
```

Run django development server
```bash
py ./manage.py runserver
```

Create superuser
```bash
py ./manage.py createsuperuser
```

### Run CSS Preprocessor
⚠ THIS IS ONLY REQUIRED, IF YOU NEED TO UPDATE TAILWIND CLASSES. 

If you use new tailwind classes, that have been never used before, you will need the preprocessor, else, you won't see the newly added classes.

You will also need a node.js environment to execute the preprocessor

Navigate to jstoolchain
```bash
cd jstoolchain
```

Install dependencies
```bash
npm i
```

Run tailwind watch
```bash
npm run tailwind:watch
```

If you changed some styling, please build the new style file and commit it to the repo
```bash
npm run tailwind:build
```


## Screenshots
![282259618-4198531c-430d-4fd3-97c7-877657cc2e05](https://github.com/user-attachments/assets/a9830236-1f47-4d3e-b71f-4149f93b08b8)
![282259625-9e27f796-5e19-46cf-945e-ca1739d698bb](https://github.com/user-attachments/assets/1b9041b9-f344-42d0-9c87-4bae6e99764d)
![282259646-51fa702d-5437-44f4-9c00-cf3fe129d165](https://github.com/user-attachments/assets/e530c77a-be88-4269-8425-134fbc392ab7)
![282259660-47b73f24-1e34-4e60-b7e7-f9e921c2f9b3](https://github.com/user-attachments/assets/c13d034c-2622-4975-ab8d-3d929d6728e8)
![282259665-68b266c3-c842-4a61-a882-1bd0539fc033](https://github.com/user-attachments/assets/5c65d4fe-a3cd-4fdd-99bb-f5ba4130402c)
![282259687-4e7e7031-fc48-43a0-88a4-a6430da5686a](https://github.com/user-attachments/assets/baea1e8f-81ae-4763-a601-3cc546ec7ff8)

