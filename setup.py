from setuptools import setup, find_packages

setup(
    name='django-url-shortener',
    version='1.0',
    packages=find_packages(),
    license='MIT',
    description='A professional URL shortener utility for Django projects.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/mrisis/django-url-shortener',
    author='Reza Amin',
    author_email='rezaamin8889@gmail.com',
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
    install_requires=[],
)
