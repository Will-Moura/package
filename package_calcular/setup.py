from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="packagecp",
    version="0.0.1",
    author="WilliamMoura",
    author_email="william_2207.moura@hotmail.com",
    description="The package is used for to calculate the porcentage in your code.",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Will-Moura",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)