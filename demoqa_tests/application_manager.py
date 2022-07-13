from demoqa_tests.page import RegistrationForm
from demoqa_tests.controls.table import Table


class Application_manager:
    result_registered_user_dialog = Table
    registration_form = RegistrationForm()


app = Application_manager
