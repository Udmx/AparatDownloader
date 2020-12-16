import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="AparatDownloader",
    version="1.0.0",
    author="Pouria Shafiee",
    author_email="pouriashafieeit@gmail.com",
    description="Download aparat videos",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Udmx/AparatDownloader",
    packages=setuptools.find_packages(),
    install_requires=[
        'requests', 'beautifulsoap4'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
