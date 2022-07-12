from selene.support.shared import browser
from demoqa_tests.controls.datepicker import Date_picker
from demoqa_tests.controls.entering_tags import EnteringTags
from demoqa_tests.controls.absolute_path_file import get_abspath
from demoqa_tests.controls.dropdown import Dropdown
from selene import command



class Registration_form:

    def __init__(self):
        self.user_city = 'Panipat'
        self.user_state = 'Haryana'
        self.user_hobbi = 'Sports', 'Music'
        self.user_b_day = 18
        self.user_b_month = 9
        self.user_b_year = 1993


    def set_first_name(self, param):
        browser.element('#firstName').type('TestName')
        return self

    def set_last_name(self, param):
        browser.element('#lastName').type('TestSurname')
        return self

    def set_user_email(self, param):
        browser.element('#userEmail').type('test_email@ya.ru')
        return self

    def set_gender(self, param):
        browser.element(f'[name=gender][value=Male]').following_sibling.click()
        return self

    def set_phone_number(self, param):
        browser.element('#userNumber').type('9208887755')
        return self

    def set_birth_day(self):
        Date_picker(browser.element('#dateOfBirthInput'), self.user_b_year, self.user_b_month,
                    self.user_b_day).set_date_by_clicks()
        return self

    def set_subjects(self, *names):
        for name in names:
            EnteringTags(browser.element('#subjectsInput')).add(name)
        return self

    def set_hobbies(self):
        list_hobbi = {
            'Sports': '[for=hobbies-checkbox-1]',
            'Music': '[for=hobbies-checkbox-3]'
        }
        for value in self.user_hobbi:
            browser.element(list_hobbi[value]).click()
        return self

    def set_picture(self):
        browser.element('#uploadPicture').send_keys(get_abspath('l8xMcQXMrRqEv1GdFVdPCD6a9zP.jpg'))
        return self

    def set_address(self, param):
        browser.element('#currentAddress').type('Bolshaya Nikitskaya st., 22k2, Moscow, 121099')
        return self

    def set_state(self):
        Dropdown(browser.element('#state')).select(option='Haryana')
        return self

    def set_city(self):
        Dropdown(browser.element('#city')).autocomplete(option='Panipat')
        return self

    @staticmethod
    def submit_form():
        browser.element('#submit').perform(command.js.click)

