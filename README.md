# Long Weekend Planner

This Python script helps you plan for long weekends. It checks for the major U.S. holidays and indicates which ones will fall on a Monday or Friday (giving you a three-day weekend) or on a Tuesday or Thursday (where you can optionally take an extra day off for a four-day weekend).

## Setup and Usage

To use this script, you need to have Python installed. If you don't have Python installed, you can download it from [here](https://www.python.org/downloads/).

Once you have Python installed:

1. Clone this repository or download the `holiday.py` script to your local machine.
2. Navigate to the directory containing the `holiday.py` script in your terminal.
3. Install the required Python packages by typing `pip install -r requirements.txt` in the terminal.
4. Run the script by typing `python3 holiday.py` in the terminal.

The script will print out the list of holidays from 2023 to 2033, indicating which ones will give you a long weekend.

## Customizing the Script

By default, the script only checks for the major U.S. holidays. If you want to include additional holidays, you can add them to the `fixed_holidays` or `floating_holidays` lists in the script.

If you want the script to check for a different range of years, you can change the arguments to the `check_holiday_weekends` function call at the end of the script.

## Contributing

Contributions to improve this script are welcome. If you find a bug or have a suggestion for a new feature, please open an issue or submit a pull request.

