<div>
  <img src="https://user-images.githubusercontent.com/69850751/175876062-f252cc1b-bd44-46b3-9ddb-a7692b2eede4.png"     alt="">
</div>

## Project Description
Airbnb clone is a complete web application that intergrates a database storage, 
a back-end API, and front-end interface in a clone of AirBnB.As an online marketplace, AirBnB connects people who want to rent out their homes with people who are looking for accommodations in specific locales.
The project currently only implements the back-end console.

## Project Classes

AirBnB makes use of the following classes:

|     | BaseModel | FileStorage | User | State | City | Amenity | Place | Review |
| --- | --------- | ----------- | -----| ----- | -----| ------- | ----- | ------ |
| **PUBLIC INSTANCE ATTRIBUTES** | `id`<br>`created_at`<br>`updated_at` | | Inherits from `BaseModel` | Inherits from `BaseModel` | Inherits from `BaseModel` | Inherits from `BaseModel` | Inherits from `BaseModel` | Inherits from `BaseModel` |
| **PUBLIC INSTANCE METHODS** | `save`<br>`to_dict` | `all`<br>`new`<br>`save`<br>`reload` | "" | "" | "" | "" | "" | "" |
| **PUBLIC CLASS ATTRIBUTES** | | | `email`<br>`password`<br>`first_name`<br>`last_name`| `name` | `state_id`<br>`name` | `name` | `city_id`<br>`user_id`<br>`name`<br>`description`<br>`number_rooms`<br>`number_bathrooms`<br>`max_guest`<br>`price_by_night`<br>`latitude`<br>`longitude`<br>`amenity_ids` | `place_id`<br>`user_id`<br>`text` | 
| **PRIVATE CLASS ATTRIBUTES** | | `file_path`<br>`objects` | | | | | | |

## Files and Directories
- ```models``` directory contains all classes used for the entire project. A class, called “model” in a OOP project is the representation of an object/instance.
- ```tests``` directory contains all unit tests.
- ```console.py``` file is the entry point of our command interpreter.
- ```models/base_model.py``` file is the base class of all our models. It contains common elements:
    - attributes: ```id```, ```created_at``` and ```updated_at```
    - methods: ```save()``` and ```to_json()```
- ```models/engine``` directory contains all storage classes (using the same prototype). For the moment I will have only one: ```file_storage.py```.

The project's implementation will happen in the following phases:
## Phase One
The first phase is to manipulate a powerful storage system to give an abstraction between objects and how they are stored and persisted. To achieve this, we will:
- put in place a parent class (called ```BaseModel```) to take care of the initialization, serialization and deserialization of my future instances
- create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
- create all classes used for AirBnB (```User, State, City, Place…```) that inherit from ```BaseModel```
- create the first abstracted storage engine of the project: File storage.
- create all unittests to validate all our classes and storage engine
- Create a data model
- Manage (create, update, destroy, etc) objects via a console/command interpreter
- Store and persist objects to files (JSON files)

## Storage

The classes are handled by the abstracted storage engine defined in the [FileStorage](./models/engine/file_storage.py) class.

Every time the backend is initialized, AirBnB starts an instance of `FileStorage` called `storage`. The `storage` object is loaded/re-loaded from any class instances stored in the JSON file `file.json`. As class instances are 
created, updated, or deleted, the `storage` object is used to register corresponding changes in the `file.json`.

## Console Description

The console is a command line interpreter that permits management of the backend of AirBnB. It can be used to handle and manipulate all classes utilized by the application (achieved by calls on the `storage` object defined above).

### Using the Console

The AirBnB console can be run both interactively and non-interactively. 
To run the console in non-interactive mode, pipe any command(s) into an execution of the file `console.py` at the command line.

```
$ echo "help" | ./console.py
(hbnb) 

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb) 
$
```
Alternatively, to use the AirBnB console in interactive mode, run the 
file `console.py` by itself:
```
$ ./console.py
```
While running in interactive mode, the console displays a prompt for input:
```
$ ./console.py
(hbnb) 
```
To quit the console, enter the command `quit`, or input an EOF signal 
(`ctrl-D`).
```
$ ./console.py
(hbnb) quit
$
```

```
$ ./console.py
(hbnb) EOF
$
```

### Console Commands

The AirBnB console supports the following commands:

* **create**
  * Usage: `create <class>`

Creates a new instance of a given class. The class' ID is printed and 
the instance is saved to the file `file.json`.

* **show**
  * Usage: `show <class> <id>` or `<class>.show(<id>)`

Prints the string representation of a class instance based on a given id.

```
$ ./console.py
(hbnb) create User
(hbnb)
(hbnb) show User uid		
(hbnb) 
(hbnb) User.show(uid)
(hbnb) 
```
* **destroy**
  * Usage: `destroy <class> <id>` or `<class>.destroy(<id>)`

Deletes a class instance based on a given id. The storage file `file.json` 
is updated accordingly.

```
$ ./console.py
(hbnb) create State
(hbnb) create Place
(hbnb)
(hbnb) destroy State uid
(hbnb) Place.destroy(uid)
(hbnb) quit
$ cat file.json ; echo ""
{}
```

* **all**
  * Usage: `all` or `all <class>` or `<class>.all()`

Prints the string representations of all instances of a given class. If no 
class name is provided, the command prints all instances of every class.

```
$ ./console.py
(hbnb) create BaseModel
(hbnb) create BaseModel
(hbnb) create User
(hbnb) create User
(hbnb)
(hbnb) all BaseModel
(hbnb)
(hbnb) User.all()
(hbnb) 
(hbnb) all
```

* **count**
  * Usage: `count <class>` or `<class>.count()`

Retrieves the number of instances of a given class.

```
$ ./console.py
(hbnb) create Place
(hbnb) create Place
(hbnb) create City
(hbnb) 
(hbnb) count Place
2
(hbnb) city.count()
1
(hbnb) 
```

* **update**
  * Usage: `update <class> <id> <attribute name> "<attribute value>"` or
`<class>.update(<id>, <attribute name>, <attribute value>)` or `<class>.update(
<id>, <attribute dictionary>)`.

Updates a class instance based on a given id with a given key/value attribute 
pair or dictionary of attribute pairs. If `update` is called with a single 
key/value attribute pair, only "simple" attributes can be updated (ie. not 
`id`, `created_at`, and `updated_at`). However, any attribute can be updated by 
providing a dictionary.

```
$ ./console.py
(hbnb) create User
(hbnb)
(hbnb) update User id first_name "name"
(hbnb) show User uid
(hbnb)
(hbnb) User.update(uid), address, "address")
(hbnb) User.show(uid)
(hbnb)
(hbnb) User.update(uid, {'email': 'email', 'last_name': 'last_name'})
(hbnb) 
```

## Testing

Unittests for the Airbnb_clone project are defined in the [tests](./tests) 
folder. To run the entire test suite simultaneously, execute the following command:

```
$ python3 unittest -m discover tests
```
Alternatively, you can specify a single test file to run at a time:
```
$ python3 unittest -m tests/test_console.py
```

## Authors :pen:
* **JULIEY NJOROGE** <[Rationew](https://github.com/rationew)>
* **DOUGLAS KEN** <[dshikuta](https://github.com/dshikuta)>
