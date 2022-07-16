from demoqa_tests.application_manager import app
from demoqa_tests.page import RegistrationForm
from selene.support.shared import browser


def test_student_registration_form():
    browser.open('automation-practice-form')

    (app.registration_form
     .set_first_name('TestName')
     .set_last_name('TestSurname')
     .set_user_email('test_email@ya.ru')
     .set_gender('Male')
     .set_phone_number('9208887755')
     .set_birth_date('18.09.1993')
     .set_subjects('Economics', 'English', 'Arts')
     .set_hobbies('Sports', 'Music')
     .set_picture('l8xMcQXMrRqEv1GdFVdPCD6a9zP.jpg')
     .set_address('Bolshaya Nikitskaya st., 22k2, Moscow, 121099')
     .set_state('Haryana')
     .set_city('Panipat')
     .submit_form()
     )

    # Table result
    app.result_registered_user_dialog.table_row(1, value='TestName TestSurname')
    app.result_registered_user_dialog.table_row(2, value='test_email@ya.ru')
    app.result_registered_user_dialog.table_row(3, value='Male')
    app.result_registered_user_dialog.table_row(4, value='9208887755')
    app.result_registered_user_dialog.table_row(5, value='18 September,1993')
    app.result_registered_user_dialog.table_row(6, value='Economics, English, Arts')
    app.result_registered_user_dialog.table_row(7, value='Sports, Music')
    app.result_registered_user_dialog.table_row(8, value='l8xMcQXMrRqEv1GdFVdPCD6a9zP.jpg')
    app.result_registered_user_dialog.table_row(9, value='Bolshaya Nikitskaya st., 22k2, Moscow, 121099')
    app.result_registered_user_dialog.table_row(10, value='Haryana Panipat')
