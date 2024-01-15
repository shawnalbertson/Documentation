- configuration file used by 
	- packaging tools
	- linters
		- sort of quality check on code, displaying warnings and erros
	- type checkers
- Three possible TOML  (just a specific file format for config files)
	- [build-system]
		- declare which build backend you use, and which other dependencies are needed
	- [project]
		- project's basic metadata, dependencies, my name
	- [tool]
		- tool-specific subtables


### Build backend
"Tools like [pip](https://packaging.python.org/en/latest/key_projects/#pip) and [build](https://packaging.python.org/en/latest/key_projects/#build) do not actually convert your sources into a [distribution package](https://packaging.python.org/en/latest/glossary/#term-Distribution-Package) (like a wheel); that job is performed by a [build backend](https://packaging.python.org/en/latest/glossary/#term-Build-Backend)."
- Poetry
	- setuptools 