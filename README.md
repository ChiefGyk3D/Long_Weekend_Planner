# Holiday Long Weekend Calculator

This script calculates the potential long weekends given the standard or non-standard holidays in a year.

## Usage

Run the script in the terminal as follows:

```
python3 holiday.py [--nonstandard]
```

## Arguments

- `--nonstandard`: Calculate for non-standard holidays. By default, calculations are based on the standard holidays.

## Dependencies

To install dependencies, use the following command:

```
pip install -r requirements.txt
```

## Standard Holidays

- New Year's Day (January 1)
- Martin Luther King Jr. Day (Third Monday in January)
- Presidents' Day (Third Monday in February)
- Memorial Day (Last Monday in May)
- Independence Day (July 4)
- Labor Day (First Monday in September)
- Veterans Day (November 11)
- Thanksgiving (Fourth Thursday in November)
- Christmas Day (December 25)

## Non-standard Holidays

- New Year's Day (January 1)
- Memorial Day (Last Monday in May)
- Independence Day (July 4)
- Labor Day (First Monday in September)
- Thanksgiving (Fourth Thursday in November)
- Day After Thanksgiving (Fourth Friday in November)
- Christmas Day (December 25)

## Customizing the Script

By default, the script only checks for the major U.S. holidays. If you want to include additional holidays, you can add them to the `fixed_holidays` or `floating_holidays` lists in the script.

If you want the script to check for a different range of years, you can change the arguments to the `check_holiday_weekends` function call at the end of the script.

## Contributing

Contributions to improve this script are welcome. If you find a bug or have a suggestion for a new feature, please open an issue or submit a pull request.

