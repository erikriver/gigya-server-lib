from distutils.core import setup
import gslib

setup(
    name='gigya-server-lib',
    version=gslib.__version__,
    author=gslib.__author__,
    author_email='miguel@miguelpilar.com',
    packages=['gslib'],
    url='http://pypi.python.org/pypi/GigyaServerLib/',
    license=open('LICENSE.txt').read(),
    description='The Gigya Server Library (gslib) is a python adaptation of the Gigya Server SDK',
    long_description=open('README.rst').read(),
    install_requires=[
        "requests>=0.13.6"
    ],
    classifiers=(
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP'
    ),
)
