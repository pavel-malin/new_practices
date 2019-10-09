import ast
import six


class Bad(object):
    # self not used, method does not have to be bound, it must be made static
    def foo(self, a, b, c):
        return a + b - c


class OK(object):
    # everything is right here.
    @staticmethod
    def foo(a, b, c):
        return a + b - c


class StaticmethodChecker(object):
    def __init__(self, tree, filename):
        self.tree = tree

    def run(self):
        for stmt in ast.walk(self.tree):
            # No classes ignored
            if not isinstance(stmt, ast.ClassDef):
                continue
            # If is a class, then iterate over the members of the class body
            # in search of methods
            for body_item in stmt.body:
                # No method - skip
                if not isinstance(body_item, ast.FunctionDef):
                    continue
                # Check for decorator
                for decorator in body_item.decorator_list:
                    if (isinstance(decorator, ast.Name)
                       and decorator.id == 'staticmethod'):
                        # This is a static function - everything is fine
                        break
                else:
                    try:
                        first_arg = body_item.args.args[0]
                    except IndexError:

                        yield (
                            body_item.lineno,
                            body_item.col_offset,
                            "H905: method misses first argument",
                            "H905",
                        )
                        # Check the following method
                        continue
                    for func_stmt in ast.walk(body_item):
                        # Verification methods are different
                        # for python 2 and 3
                        if six.PY3:
                            if (isinstance(func_stmt, ast.Name)
                               and first_arg.arg == func_stmt.id):
                                # The first argument was used,
                                # everything is fine
                                break
                        else:
                            if (func_stmt != first_arg
                                and isinstance(func_stmt, ast.Name)
                               and func_stmt.id == first_arg.id):
                                # The first argument was used,
                                # everything is fine
                                break
                            else:
                                yield (
                                    body_item.lineno,
                                    body_item.col_offset,
                                    "H904: method should be declared static",
                                    "H904",
                                )
