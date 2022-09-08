import pytest
import pandas as pd
from urllib.error import URLError
from gazpacho import get, Soup
from mortalcalculator.mortality_calculate import Age
from mortalcalculator.mortality_calculate import country_life_span_data
from loguru import logger


@pytest.fixture()
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
        big_data = big_data.set_index("Country")
        big_data = big_data.rename(columns={"Females": "Female", "Males": "Male"})
        big_data["Female"] = big_data["Female"].astype("float64")
        big_data["Male"] = big_data["Male"].astype("float64")
    except URLError:
        logger.exception(
            "Website for calculating country average life span not responding"
        )
    return big_data


def test_fix_country_life_span_data():
    expecty = country_life_span_data(
        url="https://www.worldometers.info/demographics/life-expectancy/"
    )
    checky = [
        "Hong Kong",
        "Japan",
        "Macao",
        "Switzerland",
        "Singapore",
        "Italy",
        "Spain",
        "Australia",
        "Channel Islands",
        "Iceland",
        "South Korea",
        "Israel",
        "Sweden",
        "France",
        "Martinique",
        "Malta",
        "Canada",
        "Norway",
        "Ireland",
        "New Zealand",
        "Greece",
        "Luxembourg",
        "Netherlands",
        "Guadeloupe",
        "Portugal",
        "Finland",
        "Belgium",
        "Austria",
        "Germany",
        "Slovenia",
        "United Kingdom",
        "Réunion",
        "Cyprus",
        "Denmark",
        "U.S. Virgin Islands",
        "Taiwan",
        "Costa Rica",
        "Chile",
        "Guam",
        "Qatar",
        "Puerto Rico",
        "French Guiana",
        "Maldives",
        "Mayotte",
        "Czech Republic (Czechia)",
        "Barbados",
        "Curaçao",
        "Poland",
        "Lebanon",
        "Cuba",
        "Estonia",
        "United States",
        "Panama",
        "Croatia",
        "Albania",
        "Oman",
        "United Arab Emirates",
        "Turkey",
        "Uruguay",
        "French Polynesia",
        "New Caledonia",
        "Slovakia",
        "Bosnia and Herzegovina",
        "Colombia",
        "Thailand",
        "Bahrain",
        "Ecuador",
        "Sri Lanka",
        "Algeria",
        "Antigua and Barbuda",
        "China",
        "Peru",
        "Morocco",
        "Montenegro",
        "Tunisia",
        "Iran",
        "Hungary",
        "Argentina",
        "Aruba",
        "Saint Lucia",
        "Malaysia",
        "Brazil",
        "Romania",
        "Serbia",
        "Lithuania",
        "Brunei",
        "North Macedonia",
        "Syria",
        "Honduras",
        "Kuwait",
        "Vietnam",
        "Latvia",
        "Saudi Arabia",
        "Armenia",
        "Mauritius",
        "Bulgaria",
        "Mexico",
        "Nicaragua",
        "Belarus",
        "Belize",
        "Guatemala",
        "Jordan",
        "Jamaica",
        "Dominican Republic",
        "State of Palestine",
        "Paraguay",
        "Bahamas",
        "Georgia",
        "Micronesia",
        "El Salvador",
        "Trinidad and Tobago",
        "Kazakhstan",
        "Samoa",
        "Seychelles",
        "Cabo Verde",
        "Bangladesh",
        "Libya",
        "Solomon Islands",
        "Azerbaijan",
        "Russia",
        "St. Vincent & Grenadines",
        "North Korea",
        "Bhutan",
        "Grenada",
        "Egypt",
        "Ukraine",
        "Bolivia",
        "Venezuela",
        "Indonesia",
        "Moldova",
        "Suriname",
        "Uzbekistan",
        "Kyrgyzstan",
        "Tajikistan",
        "Nepal",
        "Philippines",
        "Tonga",
        "Western Sahara",
        "Iraq",
        "Sao Tome & Principe",
        "Vanuatu",
        "Cambodia",
        "Mongolia",
        "India",
        "Guyana",
        "Timor-Leste",
        "Rwanda",
        "Botswana",
        "Kiribati",
        "Laos",
        "Senegal",
        "Turkmenistan",
        "Micronesia",
        "Madagascar",
        "Fiji",
        "Djibouti",
        "Ethiopia",
        "Pakistan",
        "Myanmar",
        "Eritrea",
        "Kenya",
        "Gabon",
        "Yemen",
        "Tanzania",
        "Sudan",
        "Afghanistan",
        "Malawi",
        "Mauritania",
        "Papua New Guinea",
        "Congo",
        "Comoros",
        "Liberia",
        "Haiti",
        "Ghana",
        "South Africa",
        "Namibia",
        "Zambia",
        "Uganda",
        "Niger",
        "Gambia",
        "Burkina Faso",
        "Benin",
        "Burundi",
        "Guinea",
        "Angola",
        "Zimbabwe",
        "Togo",
        "Mozambique",
        "DR Congo",
        "Eswatini",
        "Mali",
        "Cameroon",
        "Equatorial Guinea",
        "Guinea-Bissau",
        "Côte d'Ivoire",
        "South Sudan",
        "Somalia",
        "Sierra Leone",
        "Nigeria",
        "Lesotho",
        "Chad",
        "Central African Republic",
    ]
    assert expecty.index.isin(checky).sum() == expecty.index.isin(checky).sum()


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
