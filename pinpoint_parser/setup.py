from setuptools import setup
from setuptools_rust import Binding, RustExtension

setup(
    name="pinpoint_parser",
    version="1.0",
    rust_extensions=[RustExtension("pinpoint_parser.pinpoint_parser", binding=Binding.PyO3)],
    packages=["pinpoint_parser"],
    # rust extensions are not zip safe, just like C-extensions.
    zip_safe=False,
)
