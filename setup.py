from setuptools import setup,find_packages
packages = find_packages("src",exclude=["*.tests.*", "tests.*", "tests"])
print(packages)
setup(
    name="deepin-auto-build",
    version="0.0.1",
    author="Heysion Yuan",
    packages = packages,
    package_dir = {"":"src"},
)
