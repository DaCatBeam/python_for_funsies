from setuptools import setup

setup(
    name="image_injector",
    version="0.1",
    py_modules=["image_injector"],
    include_package_data=True,
    install_requires=["click"],
    entry_points="""
        [console_scripts]
        image_injector=image_injector:cli
    """,
)
