import setuptools

setuptools.setup(
    name="datestamp",
    version="0.0.1",
    author="Michal Ciesielski",
    author_email="xyz@gmail.com",
    description="Michal Ciesielski Data Lake Framework",
    long_description="Custom simple library to use in databricks",
    url="",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'pyodbc',
        'jsonschema'
    ]
)