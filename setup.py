import setuptools

with open("requirements.txt") as fp:
    requirements = fp.read().splitlines()

setuptools.setup(
    name="xrequests",
    author="h0nda",
    description="A faster alternate for the requests library",
    url="https://github.com/h0nde/xrequests",
    download_url="https://github.com/h0nde/xrequests/archive/refs/heads/main.zip",
    packages=setuptools.find_packages(),
    classifiers=[],
    install_requires=requirements
)
