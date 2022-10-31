# **0x00. AirBnB clone - The console**
`Group project`

`Python`

`OOP`

# **Description**

This project is the first piece of the full AirBnB web clone.
The console consist of the data model and the storage system which gives an absractioin between objects.

`In this project, each task is linked to:`
* put in place a parent class (called `BaseModel`) to take care of the initialization, serialization and deserialization of future instances.
* create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
* create all classes used for AirBnB (`User`, `State`, `City`, `Place`…) that inherit from `BaseModel`
* create the first abstracted storage engine of the project: File storage.

This project is basically based on building the command interpreter:
* create a new object
* retrieve an object from a file, a database etc...
* do operations on objects (count, compute stats, etc...)
* update attributes of an object
* destroy an object.

# **Execution**

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
