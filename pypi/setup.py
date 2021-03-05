from setuptools import setup, find_packages

setup(
    name="person_descriptor",
    version="0.1.0",
    author="Łukasz Tkaczyk",
    author_email="lukasztkaczyk@hotmail.com",
    packages=find_packages(),
    python_requires=">=3.7",
    description="Our super useful person descriptor",
    install_requires=[
        "setuptools",
        "wheel",
        "pytest",
        "pylint",
    ],
    entry_points="""
    [console_scripts]
    person_age=person.main:start_app
    """
)
