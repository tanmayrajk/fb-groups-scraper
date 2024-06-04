# FACEBOOK GROUPS SCRAPER

## Setup & Installation

First of all, download the chromedriver from [here](https://googlechromelabs.github.io/chrome-for-testing/) and [add it to your path](https://www.architectryan.com/2018/03/17/add-to-the-path-on-windows-10/).

Assuming that you have Python 3 >= installed, cd into this directory and use the following command to create and activate the virtual environment:

```
python -m venv .
.\Scripts\activate
```

Next install the required packages by using:

```
pip install -r requirements.txt
```

## Usage

**First, fill in the variables in the [.env](/.env) file.**

After that, you can run the main file:

```
python main.py
```

Once the program completely runs, an output.xlsx will be created in the working directory. Also, you can delete the ".json" files once the output.xlsx file is generated.
