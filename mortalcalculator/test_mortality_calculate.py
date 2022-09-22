import pytest
import pandas as pd
from urllib.error import URLError
from gazpacho import get, Soup
from mortalcalculator.mortality_calculate import Age
from loguru import logger


@pytest.fixture
def fix_country_life_span_data(
    url="https://www.worldometers.info/demographics/life-expectancy/",
):
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
            # print(f"extracting country details from row {_}")
            dey = [j.text for j in num.find("td")]
            fishy.append(dey)
        big_data = pd.DataFrame(data=fishy, columns=head_data)
        big_data = big_data.drop(["#"], axis=1)
        big_data['Country'] = big_data['Country'].str.upper()
        big_data = big_data.set_index("Country")
        big_data = big_data.rename(columns={"Females": "Female", "Males": "Male"})
        big_data["Female"] = big_data["Female"].astype("float64")
        big_data["Male"] = big_data["Male"].astype("float64")
    except URLError:
        logger.exception(
            "Website for calculating country average life span not responding"
        )
    return big_data


def test_dataframe_type(fix_country_life_span_data):
    """
    Test fix_country_life_span_data
    :param fix_country_life_span_data:
    :return:
    """
    assert isinstance(fix_country_life_span_data, pd.DataFrame)


def test_list_of_countries(fix_country_life_span_data):
    country_list = len(fix_country_life_span_data.index.to_list())
    assert country_list == 202


def test_male_female_col_data_type(fix_country_life_span_data):
    female_col = fix_country_life_span_data["Female"][0]
    assert isinstance(female_col, float)
    male_col = fix_country_life_span_data["Male"][0]
    assert isinstance(male_col, float)

def test_country_upper_case(fix_country_life_span_data):
    index_case = fix_country_life_span_data.index.to_list()
    assert "singapore" not in index_case

#@pytest.fixture
def test_call_main_code(name ="Spencer", age =45, terminal_age =98, country ='unitedstates', sex="Male"):
    zyu = country.split(' ')
    gyu = country.upper()
    assert isinstance(zyu,list)
    assert  len(zyu) != 2
    assert gyu == 'UNITEDSTATES'
    assert isinstance(gyu,str)
    assert isinstance(name,str)
    assert not isinstance(age,str)
    assert isinstance(sex,str)
    assert isinstance(terminal_age,int)

    



def test_age():
    # given
    gey = Age(name="Spenser", age=45, terminal_age=98, country="Jamaica", sex="Male")
    # when
    assert gey.age == 45
    # then
    assert gey.terminal_age == 98
    assert gey.country == "Jamaica"
    assert gey.sex == "Male"

    # when
    gey.remaining_days_on_earth()
    # then
    outputz = None
    assert outputz == gey.remaining_days_on_earth()
