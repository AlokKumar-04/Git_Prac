from setuptools import setup, find_packages

setup(
    name='Censos_income',
    version='0.0.0.1',
    author='Alok Kumar',
    packages=find_packages(),
    install_requires=[
        'pandas', 
        'numpy', 
        'flask', 
        'beautifulsoup4', 
        'scipy', 
        'matplotlib'
    ]
)
