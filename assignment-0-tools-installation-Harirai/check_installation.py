import importlib

modules = ["numpy", "pandas", "nltk", "matplotlib", "sklearn", "hmmlearn", "sympy", "scipy", "jupyter"]


for module in modules:
	try:
		importlib.import_module(module)
	except:
		print(module + " not installed!")


