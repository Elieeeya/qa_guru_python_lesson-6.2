from selene.support.shared import browser
from demoqa_tests.controls.datepicker import Date_picker
from demoqa_tests.controls.entering_tags import EnteringTags
from demoqa_tests.utils import get_abspath
from demoqa_tests.controls.dropdown import Dropdown
from demoqa_tests.controls.table import Table
from selene import command, have


class RegistrationForm:
    def __init__(self):
        self.birth_date = Date_picker(browser.element('#dateOfBirthInput'))


    def set_first_name(self, param):
        browser.element('#firstName').type(param)
        return self

    def set_last_name(self, param):
        browser.element('#lastName').type(param)
        return self

    def set_user_email(self, param):
        browser.element('#userEmail').type(param)
        return self

    def set_gender(self, param):
        browser.element('#genterWrapper').all('.custom-radio').element_by(have.exact_text(param)).click()
        return self

    def set_phone_number(self, param):
        browser.element('#userNumber').type(param)
        return self

    def set_birth_date(self, birth_date):
        self.birth_date.add(birth_date)
        return self

    def set_subjects(self, *names):
        for name in names:
            EnteringTags(browser.element('#subjectsInput')).add(name)
        return self

    def set_hobbies(self, *values):
        list_hobbi = {
            'Sports': '[for=hobbies-checkbox-1]',
            'Reading': '[for=hobbies-checkbox-2]',
            'Music': '[for=hobbies-checkbox-3]'
        }
        for value in values:
            browser.element(list_hobbi[value]).click()
        return self

    def set_picture(self, image):
        browser.element('#uploadPicture').send_keys(get_abspath(image))
        return self

    def set_address(self, param):
        browser.element('#currentAddress').type(param)
        return self

    def set_state(self, state_name):
        Dropdown(browser.element('#state')).select(option=state_name)
        return self

    def set_city(self, city_name):
        Dropdown(browser.element('#city')).autocomplete(option=city_name)
        return self

    def submit_form(self):
        browser.element('#submit').perform(command.js.click)
