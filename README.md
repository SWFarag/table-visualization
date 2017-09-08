# Table Visualization
Provide a simple way of visualizing your data tables. Tables are searchable using individual column searching functionality that is provided by DataTables for quickly search through the information in the table. Moreover, tables are elegantly paginated and they are also sortable.
## Installation
This script uses Python 2.7.x If you don't have Python, I would recommend downloading it from Anaconda.

Copy or clone this package from Github.

Open the Terminal/Command Line and navigate to where you copied the package:

```
$ cd path/to/copied/directory
```

## Linux and MacOS
Install the dependencies by entering:
```
$ pip install -r requirements.txt
```

## Usage
To run from the command-line, just do:
```
$ python wsgi.py
```

## Docker
A Docker container is available for this project.  For a detailed description of docker, please refer to this [overview.](https://www.docker.com/what-docker)

## Install Docker
Follow [instructions](https://www.docker.com/docker-mac) to install Docker for your environment.

## Get a pre-built image from DockerHub and run the server
```
docker pull stevetsa/table-visualization
docker run -itp 8000:8000 stevetsa/table-visualization
```
You can browse:
    http://127.0.0.1:8000

Ctrl-C to stop the server.

## Questions and Comments
Feel free to direct any questions or comments to the Issues page of the repository.
