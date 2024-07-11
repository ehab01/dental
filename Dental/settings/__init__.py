
try:
    from .local import *
except ImportError:
    try:
        from .staging import *
    except ImportError:
        try:
            from .staging import *
        except ImportError as e:
            e.args = tuple(
                ['%s (Did you create a copy settings/production.py)' % e.args[0]]
            )
            raise e