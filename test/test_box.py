from demoqa_tests.application_manager import app
from selene.support.shared import browser

def test_student_registration_form():
        browser.open('automation-practice-form')

        app.form.set_first_name('TestName') \
                .set_last_name('TestSurname') \
                .set_user_email('test_email@ya.ru') \
                .set_gender('[for="gender-radio-1"]') \
                .set_phone_number('9208887755') \
                .set_birth_day() \
                .set_subjects('Economics', 'English', 'Arts') \
                .set_hobbies() \
                .set_picture() \
                .set_address('Bolshaya Nikitskaya st., 22k2, Moscow, 121099') \
                .set_state() \
                .set_city() \
                .submit_form()

        app.result.cell(1, value='TestName TestSurname')
        app.result.cell(2, value='test_email@ya.ru')
        app.result.cell(3, value='Male')
        app.result.cell(4, value='9208887755')
        app.result.cell(5, value='18 September,1993')
        app.result.cell(6, value='Economics, English, Arts')
        app.result.cell(7, value='Sports, Music')
        app.result.cell(8, value='l8xMcQXMrRqEv1GdFVdPCD6a9zP.jpg')
        app.result.cell(9, value='Bolshaya Nikitskaya st., 22k2, Moscow, 121099')
        app.result.cell(10, value='Haryana Panipat')
