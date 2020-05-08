rpc_info = {}


def xmlrpc(in_=(), out=(type(None),)):

    def _xmlrpc(function):
        # registering the signature
        func_name = function.__name__

        rpc_info[func_name] = (in_, out)

        def _check_types(elements, types):
            """Subfunction that checks the types."""
            if len(elements) != len(types):

                raise TypeError('argument count is wrong')
            typed = enumerate(zip(elements, types))

            for index, couple in typed:
                arg, of_the_right_type = couple

                if isinstance(arg, of_the_right_type):

                    continue
                raise TypeError(
                    'arg #%d should be %s' % (index,
                                              of_the_right_type))

        # wrapped function
        def __xmlrpc(*args):  # no keywords allowed
            # checking what goes in
            checkable_args = args[1:]  # removing self
            _check_types(checkable_args, in_)
            # running the function
            res = function(*args)
            # checking what goes out
            if not type(res) in (tuple, list):
                checkable_res = (res,)
            else:
                checkable_res = res
            _check_types(checkable_res, out)

            # the function and the type
            # checking succeeded
            return res
        return __xmlrpc
    return _xmlrpc
