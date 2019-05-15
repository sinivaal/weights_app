# Raspberry Pi weight scale application

This is software for a scale made with  Raspberry Pi, hx711 and FZ1878.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

You will need

```
*Raspberry Pi with Raspian installed
*Working database with PostgreSQL installed.
*HX711 and FZ1878 connected correctly
```

### Installing

A step by step series of examples that tell you how to get a development env running.
As Raspian has already Python 3 installed you will need to:

Start with making a virtual enviroment in your desired directory:
[Good guide](https://realpython.com/python-virtual-environments-a-primer/) for staring with venv tool.

```
python3 -m venv env
```
Then activate your virtual enviroment:
```
source [your virtual enviroment name]/bin/activate
```
and clone the repository to your project folder:

```
git clone https://github.com/sinivaal/weights_app.git
```

Then install the dependencies using python:

```
python -m pip install -r requirements.txt
```

Finally run your new app:
```
python run.py
```

## Running the tests

Tests are written useing Python unitest module. To run tests move to the tests folder and 

```
python test.py
```

### Break down into end to end tests

Right now there is only 1 test and it tests database connection.

```
Example will come here
```

## Deployment

Once again you will need PostgreSLQ database for this application to work.

## Built With

* [Psycopg2](http://initd.org/psycopg/) - PostgreSQL database adapter


## Authors

* **Sinivaal** - *Initial work* - [sinivaal](https://github.com/sinivaal)


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone who will use the code

