from demoqa_tests.controls.pages.page import Registration_form
from demoqa_tests.controls.table import Table



class Application_manager:
    result = Table
    form = Registration_form()

app = Application_manager
