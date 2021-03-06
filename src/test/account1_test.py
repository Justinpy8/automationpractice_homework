from src.utilities import load_yaml, create_logger
from src.all_imports import *

# from src.steps.account_creation_steps import *

data = utils.load_yaml("C:/Dev/automationpractice_homework/data/parameter.yml")
logs = utils.create_logger()

# Parameters:

url = data["dataset1"]["url"]
email = data["dataset1"]["email"]
title = data["dataset1"]["title"]
firstname = data["dataset1"]["firstname"]
lastname = data["dataset1"]["lastname"]
password = data["dataset1"]["password"]
date = data["dataset1"]["date"]
month = data["dataset1"]["month"]
year = data["dataset1"]["year"]
companyname = data["dataset1"]["companyname"]
address_line1 = data["dataset1"]["address_line1"]
address_line2 = data["dataset1"]["address_line2"]
city = data["dataset1"]["city"]
state = data["dataset1"]["state"]
zipcode = data["dataset1"]["zipcode"]
country = data["dataset1"]["country"]
additionalinfo = data["dataset1"]["additionalinfo"]
homephone = data["dataset1"]["homephone"]
mobilephone = data["dataset1"]["mobilephone"]
aliasaddress = data["dataset1"]["aliasaddress"]


@pytest.mark.positive
@pytest.mark.account_creation
@pytest.mark.account_creation_positive
def test_account_creation_case1(driver):
    logs.info("Starting account creation positive case #1 test!")
    account_creation = AccountCreationPage(driver)
    account_creation.launching_website(url)
    account_creation.email_address_check(email)
    account_creation.title_info(title)
    account_creation.name_info(firstname, lastname)
    account_creation.password_info(password)
    account_creation.date_of_birth(date, month, year)
    account_creation.special_offers()
    account_creation.news_letter()
    account_creation.company_name(companyname)
    account_creation.address(address_line1, address_line2, city, state, zipcode, country)
    account_creation.additional_info(additionalinfo)
    account_creation.home_phone(homephone)
    account_creation.mobile_phone(mobilephone)
    account_creation.address_alias(aliasaddress)
    account_creation.register_button()
    account_creation.account_confirmation()
    account_creation.signout()
