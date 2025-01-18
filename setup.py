from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="mementia",
    version="0.1.0",
    author="yosefkat",
    description="A sentient memetic intelligence platform",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/memesphere/mementia",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "memesphere-train=scripts.train_model:main",
            "memesphere-deploy=scripts.deploy_agent:main",
        ],
    },
    include_package_data=True,
    package_data={
        "mementia": ["data/*", "config/*"],
    },
) 
