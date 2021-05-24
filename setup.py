from setuptools import setup, find_packages

setup(
    name="please_debug_my_code",
    version="1.0",
    description="Perfect debug helper",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="ChernV (otter18)",
    author_email="vchern185@gmail.com",
    url="https://github.com/otter18/please_debug_my_code",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3',
)
