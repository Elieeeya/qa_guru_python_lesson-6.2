import demoqa_tests
import os
from pathlib import Path



# Abs Путь к файлу
def get_abspath(path):
    file_path = str(Path(demoqa_tests.__file__).parent.parent.joinpath(f'resources/{path}'))
    return os.path.abspath(file_path)