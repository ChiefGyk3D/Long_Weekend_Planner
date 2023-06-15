import argparse
import datetime
from dateutil.relativedelta import relativedelta, MO, TH, FR

# Define standard fixed and floating date holidays
standard_fixed_holidays = [("New Year's Day", 1, 1),  # New Year's Day
                           ("Independence Day", 7, 4),  # Independence Day
                           ("Veterans Day", 11, 11),  # Veterans Day
                           ("Christmas Day", 12, 25)]  # Christmas Day

standard_floating_holidays = [("Martin Luther King Jr. Day", 1, MO(3)),
                              ("Presidents' Day", 2, MO(3)),
                              ("Memorial Day", 5, MO(-1)),
                              ("Labor Day", 9, MO(1)),
                              ("Thanksgiving", 11, TH(4))]

# Define non-standard fixed and floating date holidays
nonstandard_fixed_holidays = [("New Year's Day", 1, 1),  # New Year's Day
                              ("Independence Day", 7, 4),  # Independence Day
                              ("Christmas Day", 12, 25)]  # Christmas Day

nonstandard_floating_holidays = [("Memorial Day", 5, MO(-1)),
                                 ("Labor Day", 9, MO(1)),
                                 ("Thanksgiving", 11, TH(4)),
                                 ("Day After Thanksgiving", 11, FR(4))]

def check_holiday_weekends(year_start, year_end, nonstandard):
    holiday_data = {}

    fixed_holidays = nonstandard_fixed_holidays if nonstandard else standard_fixed_holidays
    floating_holidays = nonstandard_floating_holidays if nonstandard else standard_floating_holidays

    for year in range(year_start, year_end+1):
        holiday_data[year] = []

        for holiday_name, month, day in fixed_holidays:
            date = datetime.date(year, month, day)
            weekday = date.weekday()

            if weekday in [0, 4]:  # If the holiday is on a Monday or Friday
                holiday_data[year].append((holiday_name, date.strftime("%B %d"), 'You have a three-day weekend.'))
            elif weekday == 1:  # If the holiday is on a Tuesday
                off_day = date - datetime.timedelta(days=1)
                holiday_data[year].append((holiday_name, date.strftime("%B %d"), 'You can take off Monday, ' + off_day.strftime("%B %d") + ', for a four-day weekend.'))
            elif weekday == 3:  # If the holiday is on a Thursday
                off_day = date + datetime.timedelta(days=1)
                holiday_data[year].append((holiday_name, date.strftime("%B %d"), 'You can take off Friday, ' + off_day.strftime("%B %d") + ', for a four-day weekend.'))

        for holiday_name, month, rule in floating_holidays:
            date = datetime.date(year, month, 1) + relativedelta(weekday=rule)
            holiday_data[year].append((holiday_name, date.strftime("%B %d"), 'You have a three-day weekend.'))

    # Print holiday data
    for year, data in holiday_data.items():
        print(f"\nIn {year}:")
        for holiday_info in data:
            print(f"    {holiday_info[0]} on {holiday_info[1]}: {holiday_info[2]}")

# Add command line arguments
parser = argparse.ArgumentParser()
parser.add_argument('--nonstandard', action='store_true', help='Calculate for non-standard holidays')
args = parser.parse_args()

check_holiday_weekends(2023, 2025, args.nonstandard)
