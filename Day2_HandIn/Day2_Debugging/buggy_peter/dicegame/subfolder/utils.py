class UnnecessaryError(Exception):
    pass


def i_just_throw_an_exception():
    try:
        #value = 1
        #def some_inner_function():
        #    value += 1
        #some_value = "I don't know what you were expecting"
        print('Invalid option. Please use "y" or "n".')
    except Exception as e:
        raise UnnecessaryError("You actually called this function...")
