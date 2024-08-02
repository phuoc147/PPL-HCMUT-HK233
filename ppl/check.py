import inspect
import antlr4

# Get the file path of the antlr4 module
antlr4_path = inspect.getfile(antlr4)
print(f"The antlr4 module is located at: {antlr4_path}")
# antlr4 -v 4.13.0 -Dlanguage=Python3 Expr.g4
#python Driver.py input.txt