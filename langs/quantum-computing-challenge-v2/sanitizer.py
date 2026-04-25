from os.path import join, dirname
import ast

builtin_functions = set(name for name in dir(__builtins__) if name.islower())
builtin_functions.remove('float')
builtin_functions.remove('range')
builtin_functions.remove('int')
builtin_functions.remove('list')

def check_code():
    with open(join(dirname(__file__), 'solve.py')) as f:
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
                if alias.name not in ['qiskit', 'numpy', 'qiskit.circuit.gate']:
                    raise AssertionError(f"Please do not import the module '{alias.name}'")

        if isinstance(node, ast.ImportFrom):
            if node.module not in ['qiskit', 'numpy', 'qiskit.circuit.gate']:
                raise AssertionError(f"Please do not import the module '{node.module}'")

    # Check if the code contains only one function definition with the name "solve"

    func_defs = [node for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]

    assert len(func_defs) <= 2, "Do not define more than two functions in the code"

    for func_def in func_defs:
        assert func_def.name == "solve" or func_def.name == "oracle", "The function defined should be named 'solve' or 'oracle'"

        for node in ast.walk(func_def):
            # Check if the function does not contain any import statements
            if isinstance(node, ast.Import):
                raise AssertionError("Please do not include any import statements inside the function")

            # Check if the function does not contain any built-in functions
            if isinstance(node, ast.Name) and node.id in builtin_functions:
                raise AssertionError(f"Please do not use the built-in function '{node.id}' inside the function")

            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id in builtin_functions:
                raise AssertionError(f"Please do not call the built-in function '{node.func.id}' inside the function")

if __name__ == "__main__":
    check_code()