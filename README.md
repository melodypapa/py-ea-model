# 1. py-ea-model

1. The python library for the Enterprise Architect.
2. Access Enterprise Architect with pywin 

# 2. How to create the distribution and upload to pypi

1. Run `python setup.py bdist_wheel` to generate distribution
2. Run `twine check dist/*` to check the validation of distribution
3. Run `twine upload dist/*` to upload to pypi repository
4. Check the website https://pypi.org/project/armodel/ to find out it works or not

And more details can be found at https://packaging.python.org/  

# 3. Change History

**Version 0.1.0** 

1. Initial version for the EA model

