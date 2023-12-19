class NonPositiveArgumentException(Exception):
    "Raised when an argument is required to be positive but it is not"
    pass

class NotANumberException(Exception):
    "Raised when an argument is required to be an int or a float but it is not"
    pass

def check_args(*args):
    '''
    Проверяет все данные аргументы на предмет соблюдения требований касательно
    типов данных и положительности всех числовых значений.

    Может выбрасывать NotANumberException либо NonPositiveArgumentException.
    '''

    if not all([type(arg) in [int, float] for arg in args]):
        raise NotANumberException

    if not all([arg > 0 for arg in args]):
        raise NonPositiveArgumentException