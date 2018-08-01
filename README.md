# date_tools
##### Author: Henin Roland Karkada
--------------------------

**date_tools** provides an integrated collection of date utilities to help you guess the date format of any given date string/list

**Usage**:
> **guess_date_format()** -> Expects a single date/ List of dates

> $ from date_tools import date_guesser

> a) Single date:

> Example 1: $ date_guesser.guess_date_format("22/03/2018")
> Output: '%d/%m/%Y'
>
> Example 2: $ date_guesser.guess_date_format("14 03 18")
> Output: '%d %m %y'
>
> Example 3: $ date_guesser.guess_date_format("13-Mar-2018")
> Output: '%d-%b-%Y'
>
> Example 4: $ date_guesser.guess_date_format("31/March/18")
> Output: '%d/%B/%y'
>
> Example 5: $ date_guesser.guess_date_format("22/03/2018")
> Output: '%d/%m/%Y'
>
> Example 6: $ date_guesser.guess_date_format("31 03 2017")
> Output: '%d %m %Y'
>
> Example 7: $ date_guesser.guess_date_format("03/2018")
> Output: '%m/%Y'
>
> Example 8: $ date_guesser.guess_date_format("March/2018")
> Output: '%B/%Y'

> b) List of dates:
> Example 1: $ date_guesser.guess_date_format(["02 March 2018", "12 May 2018","10 December 2018", "22/03/1988"])
> Output: '%d %B %Y' --> Returned as '%d %B %Y' was the date format matched with majority of the items

Extra Details can be found in the example folder

### Contributing to date_tools
If you want to contribute code to **date_tools**, please take a look at  *CONTRIBUTING.md*.
