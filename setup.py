from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

__version__ = "0.0.6"
REPO_NAME = "mongodb_connector"
PKG_NAME = "MongoConnect"
AUTHOR_USER_NAME = "omkars20"
AUTHOR_EMAIL = "singhomkar20.1995@gmail.com"

setup(
    name=PKG_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A python package for connecting with database.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=[
        'pymongo',
        'dnspython',
        'pandas',
        'numpy',
        'ensure',
    ],
    extras_require={
        'dev': [
            'pytest==7.1.3',
            'tox==3.25.1',
            'black==22.8.0',
            'flake8==5.0.4',
            'mypy==0.971',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)


