import itertools



def imapchain(*a, **kwa):
    """ Like itertools.imap but also chains the results. """
    return itertools.chain( *itertools.imap( *a, **kwa ) )


def iapply(function, *iterables):
    """ Like itertools.imap, but returns the iterable's item/iterables' items instead. """

    iterables = map(iter, iterables)
    while True:
        args = [next(it) for it in iterables]
        if function is None:
            yield tuple(args)
        else:
            function(*args)
            yield args[0]
