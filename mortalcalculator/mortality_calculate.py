"""
Created on Wed Sep 07 16:20:01 2022
@author: Hedgar Ajakaiye
"""
from urllib.error import URLError
import pandas as pd
from gazpacho import get, Soup
from loguru import logger
from dataclasses import dataclass
from rich.console import Console


console = Console()

WORLDOMETERS = "https://www.worldometers.info/demographics/life-expectancy/"


def country_life_span_data(url: str) -> pd.DataFrame:
    """
    Description
    ----
    Helper function for class instance variable;Obtain life expectancy data from the worldometers website.
    Input
    ----
    parameter :str The worldometers url page
    Output
    ----
    df (pd.DataFrame)
        Returns a DataFrame with average life expectancy of males and female from different countries.
    """
    try:
        # logger.info('Extracting country average life expectance age')
        url = str(url)
        html = get(url)
        soup = Soup(html)
        grant_table = soup.find("table", {"id": "example2"})
        head_col = grant_table.find("thead").find("th")

        head_data = [t.text for t in head_col]
        body_data = grant_table.find("tbody").find("tr")
        fishy = []
        for _, num in enumerate(body_data):
            # logger.info(f"extracting country details from row {_}")
            dey = [j.text for j in num.find("td")]
            fishy.append(dey)
        big_data = pd.DataFrame(data=fishy, columns=head_data)
        big_data = big_data.drop(["#"], axis=1)
        big_data = big_data.set_index("Country")
        big_data = big_data.rename(columns={"Females": "Female", "Males": "Male"})
        big_data["Female"] = big_data["Female"].astype("float64")
        big_data["Male"] = big_data["Male"].astype("float64")
    except URLError:
        logger.exception(
            "Website for calculating country average life span not responding"
        )
    return big_data


life_span = country_life_span_data(WORLDOMETERS)


@dataclass
class Age:
    age: int
    name: str
    terminal_age: int
    sex: str
    country: str

    def remaining_days_on_earth(self):
        """
        Description
        -----------
        functio/method of the age class which essentially carry out the heavy lifting of the app
        Input
        -----
        None of it own
        Output
        -----
        (Str) string of staement
        """
        # logger.info('Calculating remaing and spent days')
        age_in_days = self.age * 365
        avg_life_span = life_span.loc[self.country.title(), self.sex.capitalize()]
        remaining_days = self.terminal_age - self.age
        remaining_days = remaining_days * 365
        console.print(
            f"{self.age} years old {self.name.capitalize()} from {self.country.capitalize()}, welcome! Though your desired terminal age is {self.terminal_age}; {self.country.capitalize()}'s average life expectancy age for {self.sex}s is {avg_life_span}.",
            style="bold white",
        )
        console.print(
            f"Phew,{self.name.capitalize()}, you have spent {age_in_days} days of your time already!",
            style="bold white",
        )
        console.print(
            f"{self.name.capitalize()}, based on your desired terminal age of {self.terminal_age}, you have {remaining_days} days to mortality! Make each day count! Tick! Tock! Tick! Tock!",
            style="bold white",
        )
        if avg_life_span > self.age:
            # logger.info("Calculating remaining and spent day for those within country's life expectance age")
            remaining_by_life_span = avg_life_span - self.age
            days_by_life = remaining_by_life_span * 365
            console.print(
                f"Meanwhile, based on {self.country.capitalize()}'s average life expectancy age, you have {round(days_by_life)} days to mortality! Make each day count! Tick! Tock! Tick! Tock!",
                style="bold white",
            )
        elif avg_life_span < self.age:
            # logger.info("Calculating remaining and spent day for those above country's life expectance age")
            console.print(
                f"Wow! {self.name.capitalize()},you are one of the fortunates!",
                style="bold green",
            )
            grace_age = avg_life_span - self.age
            total_grace = grace_age * 365
            console.print(
                f"However, base on the average life expectancy of {self.country.capitalize()}'s citizens,you have spent[underline red] {round(total_grace)}[/] lucky days of your Graceful and lucky life. Cherish this gift...!",
                style="bold white",
            )
