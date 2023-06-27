#  Decoratori:

# @property
# @abstractmethod

def new_decorator(original_func):
    # original_func = referinta catre functia care urmeaza a fi decorata.

    def wrapper_func():
        original_func()
        print('Niste cod inaintea apelului original_func')
    return wrapper_func()


@new_decorator
def func_needs_decoration():
    print('Vreau sa fiu decorata')


func_needs_decoration()
