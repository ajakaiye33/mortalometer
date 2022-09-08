"""
Created on Wed Sep 07 16:20:01 2022
@author: Hedgar Ajakaiye
"""
from loguru import logger
import time
import fire
from pyfiglet import Figlet
from termcolor import colored
from mortalcalculator.mortality_calculate import Age


fyi = Figlet(font="standard")
print(colored(fyi.renderText("Welcome to Mortalometer"), "blue"))
time.sleep(2)


def main(name="Spencer", age=45, terminal_age=98, country="Jamaica", sex="Male"):

    """
    Description
    ----
    Engine room of the app. Calculate spent and remaining days on earth!
    Input
    ----
    parameter:
    name:str Your name
    age:(int) Your age
    terminal_age:int If you can choose, the age you wish could live up to
    country:str Your country e.g list of countries:['Hong Kong', 'Japan', 'Macao', 'Switzerland', 'Singapore', 'Italy', 'Spain', 'Australia', 'Channel Islands', 'Iceland', 'South Korea', 'Israel', 'Sweden', 'France', 'Martinique', 'Malta', 'Canada', 'Norway', 'Ireland', 'New Zealand', 'Greece', 'Luxembourg', 'Netherlands', 'Guadeloupe', 'Portugal', 'Finland', 'Belgium', 'Austria', 'Germany', 'Slovenia', 'United Kingdom', 'Réunion', 'Cyprus', 'Denmark', 'U.S. Virgin Islands', 'Taiwan', 'Costa Rica', 'Chile', 'Guam', 'Qatar', 'Puerto Rico', 'French Guiana', 'Maldives', 'Mayotte', 'Czech Republic (Czechia)', 'Barbados', 'Curaçao', 'Poland', 'Lebanon', 'Cuba', 'Estonia', 'United States', 'Panama', 'Croatia', 'Albania', 'Oman', 'United Arab Emirates', 'Turkey', 'Uruguay', 'French Polynesia', 'New Caledonia', 'Slovakia', 'Bosnia and Herzegovina', 'Colombia', 'Thailand', 'Bahrain', 'Ecuador', 'Sri Lanka', 'Algeria', 'Antigua and Barbuda', 'China', 'Peru', 'Morocco', 'Montenegro', 'Tunisia', 'Iran', 'Hungary', 'Argentina', 'Aruba', 'Saint Lucia', 'Malaysia', 'Brazil', 'Romania', 'Serbia', 'Lithuania', 'Brunei', 'North Macedonia', 'Syria', 'Honduras', 'Kuwait', 'Vietnam', 'Latvia', 'Saudi Arabia', 'Armenia', 'Mauritius', 'Bulgaria', 'Mexico', 'Nicaragua', 'Belarus', 'Belize', 'Guatemala', 'Jordan', 'Jamaica', 'Dominican Republic', 'State of Palestine', 'Paraguay', 'Bahamas', 'Georgia', 'Micronesia', 'El Salvador', 'Trinidad and Tobago', 'Kazakhstan', 'Samoa', 'Seychelles', 'Cabo Verde', 'Bangladesh', 'Libya', 'Solomon Islands', 'Azerbaijan', 'Russia', 'St. Vincent & Grenadines', 'North Korea', 'Bhutan', 'Grenada', 'Egypt', 'Ukraine', 'Bolivia', 'Venezuela', 'Indonesia', 'Moldova', 'Suriname', 'Uzbekistan', 'Kyrgyzstan', 'Tajikistan', 'Nepal', 'Philippines', 'Tonga', 'Western Sahara', 'Iraq', 'Sao Tome & Principe', 'Vanuatu', 'Cambodia', 'Mongolia', 'India', 'Guyana', 'Timor-Leste', 'Rwanda', 'Botswana', 'Kiribati', 'Laos', 'Senegal', 'Turkmenistan', 'Micronesia', 'Madagascar', 'Fiji', 'Djibouti', 'Ethiopia', 'Pakistan', 'Myanmar', 'Eritrea', 'Kenya', 'Gabon', 'Yemen', 'Tanzania', 'Sudan', 'Afghanistan', 'Malawi', 'Mauritania', 'Papua New Guinea', 'Congo', 'Comoros', 'Liberia', 'Haiti', 'Ghana', 'South Africa', 'Namibia', 'Zambia', 'Uganda', 'Niger', 'Gambia', 'Burkina Faso', 'Benin', 'Burundi', 'Guinea', 'Angola', 'Zimbabwe', 'Togo', 'Mozambique', 'DR Congo', 'Eswatini', 'Mali', 'Cameroon', 'Equatorial Guinea', 'Guinea-Bissau', "Côte d'Ivoire", 'South Sudan', 'Somalia', 'Sierra Leone', 'Nigeria', 'Lesotho', 'Chad', 'Central African Republic']
    sex:str Your sex/gender
    Output
    ----
    str
        Returns a statements depending on your input.
    """
    try:
        person = Age(
            name=name, age=age, terminal_age=terminal_age, country=country, sex=sex
        )
        if isinstance(name, str):
            name = name.upper()
        if isinstance(country, str):
            country = country.title()
        person.remaining_days_on_earth()
    except KeyError:
        logger.exception(
            "Thats an invalid input, try 'python mortalometer.py --help' for help"
        )


if __name__ == "__main__":
    fire.Fire(main)
