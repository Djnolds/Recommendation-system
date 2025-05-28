from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

## edit below variables as per your requirements -
REPO_NAME = "ML Based Recommendation System"
AUTHOR_USER_NAME = "OMOLUSI AYODEJI REYNOLDS"
SRC_REPO = "books_recommendation_system"
LIST_OF_REQUIREMENTS = []


setup(
    name=SRC_REPO,
    version="0.0.1",
    author="OMOLUSI AYODEJI REYNOLDS",
    description="A local packages for ML based recommendations system",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Djnolds/Recommendation-system",
    author_email="ayodejireynolds@gmail.com",
    packages=find_packages(),
    license="MIT",
    python_requires=">=3.7",
    install_requires=LIST_OF_REQUIREMENTS
)