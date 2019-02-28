from setuptools import setup

setup(
    name='flaskr',
    packages=['flaskr'],
    include_package_data=True,
    install_requires=[
        'flask',
    ],
    setup_requeres=[
        'pytest-runner',
    ],
    tests_requires=[
        'pytest',
    ],
)