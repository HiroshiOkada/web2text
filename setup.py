from setuptools import setup, find_packages

setup(
    name="web2text",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "playwright",
    ],
    entry_points={
        "console_scripts": [
            "web2text=web2text.core:main",
        ],
    },
    author="Your Name",
    author_email="your.email@example.com",
    description="Render JavaScript-heavy websites as text using Playwright and w3m",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/web2text",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
    ],
    python_requires=">=3.6",
)
