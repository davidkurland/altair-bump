from setuptools import setup, find_packages

setup(
    name="altair-bump",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "altair>=5.0.0",
        "pandas>=1.0.0",
        "numpy>=1.20.0",
    ],
    extras_require={
        'dev': [
            'pytest>=6.0',
            'pytest-cov>=2.0',
            'black>=21.0',
            'flake8>=3.9',
        ],
    },
    author="Your Name",
    author_email="your.email@example.com",
    description="A Python library for creating bump charts using Altair",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/altair-bump",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
) 