# AirBnB_clone

### Contents

- [Description](#description)
- [Files](#files)
- [Usage](#usage)
- [Installation](#installation)
- [Examples](#examples)
- [Resources](resources)
- [Authors](#authors)
---

### Description

In this module we created a command interpreter or better known as console, as a first step for the AriBnB clone.
This will serve as the back-end for the entire project, as our base. It will be written in Python. In this stage we will concentrate on the file storage system.
The repository will contain models tha will be used as objects, and various tests using the unittest module of Python.

### Files and Directories

- `AUTHORS` - Authors of the repository
- `console.py` - The entry point of the command interpreter
- `README.md` - Repository README.md
#### /models/
- `amenity.py` - Class amenity inherits from BaseModel
- `base_model.py` - Base class for other models
- `city.py` - Class city inherits from BaseModel
- `file_storage.py` - Class FileStorage to manage serialization and deserialization of instances, to JSON file and from JSON file to intances
- `__init__.py` - Inittialization module
- `place.py` - Class Place inherits from BaseModel
- `review.py` - Class Review inherits from BaseModel
- `state.py` - Class State inherits from BaseModel
- `user.py` - Class User inherits from BaseModel
#### /tests/
- `__init.py` - Initialization for the console tests
- `test_cosole.py` - Test cases for the console
#### /tests/test_models/
- `__init__.py` - Initialization module for tests
- `test_amenity.py` - Test cases for the Amenity class
- `test_base_model.py` - Test cases for the BaseModel class
- `test_city.py` - Test cases for the City class
- `test_place.py` - Test cases for the Place class
- `test_review.py` - Test cases for the Review class
- `test_state.py` - Test cases for the State class
- `test_user.py` - Test cases for the User class
#### /test_models/test_engine
- `__init__.py` - Initialization module for engine tests
- `test_file_storage.py` - Test cases for the FileStorage class
---

### Usage

#### Console Commands

- `help` - displays a list of commands
- `create` - creastes a new instance of a class
- `show` - shows a specific instance
- `destroy` - deletes a specific instance
- `all` - shows all intances or a class
- `update` - updates and attribute of an instance
- `count` - counts the number of instances
- `quit` - quits the console

### Installation

To install this project, you can follow these steps:

1. Clone the repository:
```
git clone git@github.com:emmanuelmaldonadomaldonado/holbertonschool-AirBnB_clone.git
``` 
2. Done

### Examples

Interactive mode:
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```

Non-interactive mode:
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```

### Resources

- *[Python packages](https://intranet.hbtn.io/concepts/66)*
- *[AirBnB clone](https://intranet.hbtn.io/concepts/74)*

### Authors

- *[Osvaldo Antompietri](https://github.com/ojvl1)*
- *[Juan C Lopez](https://github.com/juancalpz23)*
- *[Emmanuel Maldonado](https://github.com/emmanuelmaldonadomaldonado)*
