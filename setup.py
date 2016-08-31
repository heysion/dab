from setuptools import setup,find_packages
packages = find_packages("src",exclude=["*.tests.*", "tests.*", "tests"])
print(packages)
setup(
    name="deepin-auto-build",
    version="0.0.1",
    author="Heysion Yuan",
    package_dir={"dab":"src/dab/","dabdaemon":"src/dabdaemon","dabdb":"src/dabdb","dabsv":"src/dabsv/"},
    packages=["dab","dabdaemon","dabdb","dabsv"],

)
