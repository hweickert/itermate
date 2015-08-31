========
itermate
========

Iterator-tools for functional programming.

## Usage

### iapply()
Applies function similar to itertools.imap but returns another item iterator instead
of the called function's results.

    import sys
    import itermate

    >>> strings = ["foo", "bar"]
    >>> strings = itermate.iapply( sys.stdout.write, strings )
    >>> list(strings)
    foobar
    ["foo", "bar"]


### operator.attrsetter()
Sets attribute and returns new item iterator.

    import itertools
    import itermate.operator

    >>> class Foo(object):
    >>>     bar = 0
    >>>     def __repr__(self):
    >>>         return unicode(self.bar)

    >>> gen_foos = itertools.imap( attrsetter("bar", "spam"), (Foo() for i in range(3)) )
    >>> list(gen_foos)
    [spam, spam, spam]

    >>> gen_foos = itertools.imap( attrsetter("bar"),         (Foo() for i in range(3)), ["bacon", "egg", "sausage"] )
    >>> list(gen_foos)
    [bacon, egg, sausage]
