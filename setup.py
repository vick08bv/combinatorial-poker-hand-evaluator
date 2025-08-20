from setuptools import setup, find_packages

setup(
    name="combinatorial-poker-hand-evaluator",
    version="0.1.0",
    description="A combinatorial, general, and efficient poker hand evaluator with scoring.",
    author="Victor Mendez",
    author_email="vick08bv@gmail.com",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.9",
    install_requires=[

    ],
    extras_require={
        "dev": ["pytest", "numpy", "matplotlib"]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
