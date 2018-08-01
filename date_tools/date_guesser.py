# =============================================================================
# Filename: date_tools.py
# Description: Date utlities to guess the type of date format
# Author: Henin Karkada <henin.roland@gmail.com>
# Python Environment - Python3
# Usage: from date_tools import date_guesser
# Creation Date: 31-July-2018
# ==============================================================================

# Standard Modules
import logging

# Standard Packages
from datetime import datetime
from collections import Counter

# Logging Basic Configuration
logging.basicConfig(format='%(levelname)s: %(asctime)s.%(msecs)03d:: %(filename)s:: %(funcName)s():: %(lineno)s ::  %(message)s', level=logging.DEBUG, datefmt='%d-%m-%Y %H:%M:%S')

def guess_date_format(dates_list):
    """
    Guess the date format for a list of dates, first guess the date
    separator, then loop through different formats
    :param dates_list: Input list of dates/ A single date
    :return date_format: Guessed date format by separator
    Usage: 1. guess_date_format(["12-03-2018", "21-03-2018", "24-03-2018"])
           2. guess_date_format("29-03-2018")
    """

    # Check if the date to be guessed is a list of dates or single date string
    if isinstance(dates_list, str):
        dates_list = [dates_list]

    date_separator_res = []
    default_date_format = "%d-%m-%Y"

    # Loop through the dates and find the common separator in all dates
    for index, date_string in enumerate(dates_list):
        try:
            # Strip spaces in beginning and end of string
            dates_list[index] = date_string.strip()
            date_separator_temp_res = set('[_ -+/\']').intersection(
                date_string)
            if not date_separator_temp_res:
                continue
            else:
                date_separator_res.append(list(date_separator_temp_res)[0])
        except:
            continue

    # Find the top most common separator based on occurences
    try:
        date_separator = Counter(date_separator_res).most_common(1)
        if date_separator:
            date_separator = date_separator[0][0]
        else:
            date_separator = "no_space"
    except Exception as error:
        error_msg = "Error : {} occurred when trying to guess the date " \
                    "format. returning `{}` as default date format".format(
            error, default_date_format)
        logging.error(error_msg)
        return default_date_format

    if '/' == date_separator:
        date_formats = ["%d/%m/%Y", "%m/%d/%Y", "%Y/%m/%d",
                        "%Y/%d/%m", "%m/%Y/%d",
                        "%d/%m/%y", "%m/%d/%y", "%y/%m/%d",
                        "%y/%d/%m", "%m/%y/%d",
                        "%d/%b/%Y", "%b/%d/%Y", "%Y/%b/%d",
                        "%Y/%d/%b", "%b/%Y/%d",
                        "%d/%b/%y", "%b/%d/%y", "%y/%b/%d",
                        "%y/%d/%b", "%b/%y/%d",
                        "%d/%B/%Y", "%B/%d/%Y", "%Y/%B/%d",
                        "%Y/%d/%B", "%B/%Y/%d",
                        "%d/%B/%y", "%B/%d/%y", "%y/%B/%d",
                        "%y/%d/%B", "%B/%y/%d",
                        "%m/%Y", "%m/%Y", "%Y/%m",
                        "%Y/%m", "%m/%Y",
                        "%m/%y", "%m/%y", "%y/%m",
                        "%y/%m", "%m/%y",
                        "%b/%Y", "%b/%Y", "%Y/%b",
                        "%Y/%b", "%b/%Y",
                        "%b/%y", "%b/%y", "%y/%b",
                        "%y/%b", "%b/%y",
                        "%B/%Y", "%B/%Y", "%Y/%B",
                        "%Y/%B", "%B/%Y",
                        "%B/%y", "%B/%y", "%y/%B",
                        "%y/%B", "%B/%y"]

    elif '-' == date_separator:
        date_formats = ["%d-%m-%Y", "%m-%d-%Y", "%Y-%m-%d",
                        "%Y-%d-%m", "%m-%Y-%d",
                        "%d-%m-%y", "%m-%d-%y", "%y-%m-%d",
                        "%y-%d-%m", "%m-%y-%d",
                        "%d-%b-%Y", "%b-%d-%Y", "%Y-%b-%d",
                        "%Y-%d-%b", "%b-%Y-%d",
                        "%d-%b-%y", "%b-%d-%y", "%y-%b-%d",
                        "%y-%d-%b", "%b-%y-%d",
                        "%d-%B-%Y", "%B-%d-%Y", "%Y-%B-%d",
                        "%Y-%d-%B", "%B/%Y/%d",
                        "%d-%B-%y", "%B-%d-%y", "%y-%B-%d",
                        "%y-%d-%B", "%B-%y-%d",
                        "%m-%Y", "%m-%Y", "%Y-%m",
                        "%Y-%m", "%m-%Y",
                        "%m-%y", "%m-%y", "%y-%m",
                        "%y-%m", "%m-%y",
                        "%b-%Y", "%b-%Y", "%Y-%b",
                        "%Y-%b", "%b-%Y",
                        "%b-%y", "%b-%y", "%y-%b",
                        "%y-%b", "%b-%y",
                        "%B-%Y", "%B-%Y", "%Y-%B",
                        "%Y-%B", "%B/%Y",
                        "%B-%y", "%B-%y", "%y-%B",
                        "%y-%B", "%B-%y"]

    elif ' ' == date_separator:
        date_formats = ["%d %m %Y", "%m %d %Y", "%Y %m %d",
                        "%Y %d %m", "%m %Y %d",
                        "%d %m %y", "%m %d %y", "%y %m %d",
                        "%y %d %m", "%m %y %d",
                        "%d %b %Y", "%b %d %Y", "%Y %b %d",
                        "%Y %d %b", "%b %Y %d",
                        "%d %b %y", "%b %d %y", "%y %b %d",
                        "%y %d %b", "%b %y %d",
                        "%d %B %Y", "%B %d %Y", "%Y %B %d",
                        "%Y %d %B", "%B %Y %d",
                        "%d %B %y", "%B %d %y", "%y %B %d",
                        "%y %d %B", "%d %y %B",
                        "%m %Y", "%m %Y", "%Y %m",
                        "%Y %m", "%m %Y",
                        "%m %y", "%m %y", "%y %m",
                        "%y %m", "%m %y",
                        "%b %Y", "%b %Y", "%Y %b",
                        "%Y %b", "%b %Y",
                        "%b %y", "%b %y", "%y %b",
                        "%y %b", "%b %y",
                        "%B %Y", "%B %Y", "%Y %B",
                        "%Y %B", "%B %Y",
                        "%B %y", "%B %y", "%y %B",
                        "%y %B", "%y %B"]

    elif 'no_space' == date_separator:
        date_formats = ["%d%m%Y", "%m%d%Y", "%Y%m%d",
                        "%Y%d%m", "%m%Y%d",
                        "%d%m%y", "%m%d%y", "%y%m%d",
                        "%y%d%m", "%m%y%d",
                        "%d%b%Y", "%b%d%Y", "%Y%b%d",
                        "%Y%d%b", "%b%Y%d",
                        "%d%b%y", "%b%d%y", "%y%b%d",
                        "%y%d%b", "%b%y%d",
                        "%d%B%Y", "%B%d%Y", "%Y%B%d",
                        "%Y%d%B", "%b%Y%d",
                        "%d%B%y", "%B%d%y", "%y%B%d",
                        "%y%d%B", "%B%y%d",
                        "%m/%Y", "%m/%Y", "%Y/%m",
                        "%Y/%m", "%m/%Y",
                        "%m/%y", "%m/%y", "%y/%m",
                        "%y/%m", "%m/%y",
                        "%b/%Y", "%b/%Y", "%Y/%b",
                        "%Y/%b", "%b/%Y",
                        "%b/%y", "%b/%y", "%y/%b",
                        "%y/%b", "%b/%y",
                        "%B/%Y", "%B/%Y", "%Y/%B",
                        "%Y/%B", "%B/%Y",
                        "%B/%y", "%B/%y", "%y/%B",
                        "%y/%B", "%B/%y"]

    date_format_res = []
    now = datetime.now()
    # Loop through different formats and find which format matches the
    # maximum for all dates
    for date_string in dates_list:
        for date_format in date_formats:
            try:
                date_obj = datetime.strptime(date_string.strip(), date_format)
                if date_obj and (date_obj <= now):
                    date_format_res.append(date_format)
            except ValueError:
                continue

    # Take the top most matched format and return it
    try:
        if date_format_res:
            date_format_common = Counter(date_format_res).most_common(1)
            if date_format_common:
                date_format = date_format_common[0][0]
                logging.info("Date format detected: `{}`".format(date_format))
                return date_format
            else:
                logging.warning("Unable to determine the date format, default date format returned: `{}`".format(default_date_format))
                return default_date_format
        else:
            logging.warning("Unable to determine the date format, default date format returned: `{}`".format(default_date_format))
            return default_date_format
    except Exception as error:
        error_msg = "Error : {} occurred when trying to guess the date " \
                    "format. returning `{}` as default date format".format(error, default_date_format)
        logging.error(error_msg)
        return default_date_format
