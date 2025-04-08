from os.path import join, dirname
import ast

builtin_functions = set(name for name in dir(__builtins__) if name.islower())
builtin_functions.remove('float')

def check_code():
    with open(join(dirname(__file__), 'circuit.py')) as f:
        code = f.read()

    tree = ast.parse(code)

    # Check if the code does not contain any statements except the function definition and import statements

    for node in tree.body:
        if not isinstance(node, (ast.Import, ast.ImportFrom, ast.FunctionDef)):
            raise AssertionError("Please define only the function in the code")

    # Check if the code does not import any modules other than pennylane and pennylane.numpy and util

    for node in tree.body:
        if isinstance(node, ast.Import):
            for alias in node.names:
                if alias.name not in ['pennylane', 'pennylane.numpy', 'util']:
                    raise AssertionError(f"Please do not import the module '{alias.name}'")

        if isinstance(node, ast.ImportFrom):
            if node.module not in ['pennylane', 'pennylane.numpy', 'util']:
                raise AssertionError(f"Please do not import the module '{node.module}'")

    # Check if the code contains only one function definition with the name "circuit"

    func_defs = [node for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]

    assert len(func_defs) == 1, "Please define only one function in the code"

    func_def = func_defs[0]

    assert func_def.name == "circuit", "The function defined should be named 'circuit'"

    for node in ast.walk(func_def):
        # Check if the function does not contain any import statements
        if isinstance(node, ast.Import):
            raise AssertionError("Please do not include any import statements inside the function")

        # Check if the function does not contain any built-in functions
        if isinstance(node, ast.Name) and node.id in builtin_functions:
            raise AssertionError(f"Please do not use the built-in function '{node.id}' inside the function")


if __name__ == "__main__":
    check_code()