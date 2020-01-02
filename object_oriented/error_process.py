import class_exception as ce
import logging

def fo():
    raise ce.CustError('Test message.')

def foo():
    fo()

def error_stack_test():
    try:
        foo()
    except Exception as e:
        logging.error(e)
    finally:
        print('This block will be excuted.')


def manual_debug():
    n = 10
    i = 0

    # Use 'assert' to replace print in debug.
    while i <= n:
        i += 1
        assert i < 10, 'error'

if __name__ == '__main__':
    error_stack_test()
