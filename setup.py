from setuptools import setup

setup(
    name="pythonanywhere_client",
    version = "0.0.1",
    packages = ["pythonanywhere_client"],
    description = "This is a backup project of the pythonanywhere server.",
    author = "Hakan Çelik",
    author_email = "hakancelik96@outlook.com",
    url = "https://github.com/hakancelik96/pythonanywhere-python-client",
    python_requires='>=3.5.0',
    py_modules=[],
    include_package_data = True,
    install_requires = ["requests"],
    keywords = ["pythonanywhere", "client"],
    license = "MIT",
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
)