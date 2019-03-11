publish:
	python3 setup.py sdist bdist_wheel
	python3 -m twine upload dist/*

clean:
	rm -fr build dist *egg-info
