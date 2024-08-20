import setuptools

# Read the content of the README file
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

# Project metadata
__version__ = "0.0.0"
REPO_NAME = "Chicken-Disease-Classification--Project"
AUTHOR_USER_NAME = "syedowais57"
SRC_REPO = "cnnClassifier"
AUTHOR_EMAIL = "owaisquadri8575@gmail.com"

# Setup configuration
setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A brief description of the project",  # Add a description
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"
    },
    package_dir={"": "src"},  # Corrected option
    packages=setuptools.find_packages(where="src"),
)
