compile:
	pyinstaller --name MyApp --onefile --windowed --paths=. ui/__main__.py --hidden-import=matplotlib.backends.backend_svg