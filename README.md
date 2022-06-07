# Application for accounting measuring instruments(MI)
##### _Console application in Python_
_________________________
The application provides:

- Registration
- Authentication
- Delete user

## Requirements

- Python version >3
- Pandas
- Tabulate
- Cassandra

Copy/Past this into your requirements.txt:

```sh
pandas
tabulate
cassandra-driver
```

Before run the APP, just write it into your terminal:

```sh
python -m venv env
cd env
source bin/activate
pip install -r path/to/requirements.txt
```

## Usage

Run the APP:

```sh
python APP.py
```

- You will be offered 6 actions to choose from:
you should write just a number of ation
> Add Mi to reestr;

> See all Mi in reestr;

> Remove Mi from reestr;

> Remove all Mi from reestr;

> See N last added Mi in reestr;

> See statistics;

> Import Mi from csv;

> Exit


## Add Mi to reestr
You fill in the fields one by one
| Field | Type | Description |
| ------ | ------ | ------ |
| name | string | Name of MI |
| type | string | Type of MI |
| field_area | string | Field Area where is MI |
| manufacturer | string | Manufacturer of MI |
| last_date | string | Last date of MI's verification |
| units | string | Units of MI |
| field | int | Field where is MI |
| life_time | int | Life time of MI |
| release_date | int | Release date of MI |
| interval | int | Interval of MI's verification |
| range1 | int | Range1 of MI |
| range2 | int | Range2 of MI |
| pre_result | int | Result of the last MI's verification |
| relative_error | float | Relative error of MI |

## Remove Mi from reestr
You will see the table with current (not deleted) MI fnd then you will be asked:
> _Enter indexes of records to be deleted separated by a space_

Then you will see:
> _Mi deleted successfully!_

## See statistics
If you choose this point you will see the next table:
| | Value |
| ------ | ------ |
| Total Mi | ... |
| Total types of Mi | ... |
| Total manufacturers | ... |
| Total serviceable Mi | ... |
| Maximum life time of Mi | ... |
| Total Mi added today | ... |

## Import Mi from csv
To add Mi to registry from csv file you should use "  ,  " as delimiter and your file should contain **ALL** headers from database (**ALL** required fields above in "Add Mi to reestr" table)

To path you should take an absolute _**path/to/your/file.csv**_