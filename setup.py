import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bengalinlp",
    version="0.1.0",
    description="Text normalizer for Bengali and English",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Your Name",
    author_email="infosulaiman@icloud.com",
    url="https://github.com/banglawiki/bengalinlp",
    packages=setuptools.find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Text Processing :: Linguistic',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    install_requires=[
        "regex",
        "emoji==1.4.2",
        "ftfy==6.0.3"
    ],
    python_requires='>=3.5',
    include_package_data=True,
    project_urls={
        'Source': 'https://github.com/banglawiki/bengalinlp',
        'Bug Reports': 'https://github.com/banglawiki/bengalinlp/issues',
    },
)
