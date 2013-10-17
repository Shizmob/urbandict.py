# set the thing up.
from setuptools import setup

setup(
    name='urbandict',
    author='Shizmob',
    author_email='mark@xn--hwg34fba.ws',
    version='0.1',
    license='WTFPL',
    py_modules=['urbandict'],
    install_requires=['requests >= 2.0'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: Do What the Fuck You Want to Public License (WTFPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Sociology'
    ],
)
