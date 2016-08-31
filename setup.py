from setuptools import setup,find_packages
packages = find_packages("src",exclude=["*.tests.*", "tests.*", "tests"])
print(packages)
setup(
    name="deepin-auto-build",
    version="0.0.1",
    author="Heysion Yuan",
    package_dir={"dabutil":"src/dab/util","dabdaemon":"src/dabdaemon","dabdb":"src/dabdb","dabsv":"src/dabsv"},
    packages=["dabutil","dabdaemon","dabdb","dabsv"],

)
