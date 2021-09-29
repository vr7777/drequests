import setuptools

with open("requirements.txt") as fp:
    requirements = fp.read().splitlines()

setuptools.setup(
    name="drequests",
    author="vr",
    description="Discord requests wrapper",
    url="https://github.com/downvert1/drequests",
    packages=setuptools.find_packages(),
    classifiers=[],
    install_requires=requirements
)
