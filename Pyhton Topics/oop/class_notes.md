

The same dunder convention is also used for specific attributes of custom user functions and is used to store various metadata about Python objects. These attributes are as follows:

- __doc__: A writable attribute that holds the function's documentation. It is, by default, populated by the docstring function.
- __name__: A writable attribute that holds the function's name.
- __qualname__: A writable attribute that holds the function's qualified name. The qualified name is a full dotted path to the object (with class names) in the global scope of the module where the object is defined.
- __module__: A writable attribute that holds the name of the module that function belongs to.
- __defaults__: A writable attribute that holds the default argument values if the function has any.
- __code__: A writable attribute that holds the function's compile code object.
- __globals__: A read-only attribute that holds the reference to the dictionary of global variables for that function's scope. The global scope for a function is the namespace of the module where this function is defined.
- __dict__: A writable attribute that holds a dictionary of function attributes. Functions in Python are first-class objects, so they can have any arbitrary arguments defined, just like any other object.
- __closure__: A read-only attribute that holds a tuple of cells with the function's free variables. Closure cells allow you to create parametrized function decorators.
- __annotations__: A writable attribute that holds the function's argument and return annotations.
- __kwdefaults__: A writable attribute that holds the default argument values for keyword-only arguments if the function has any.
