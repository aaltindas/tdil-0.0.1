import setuptools

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name='tdil',
    author='Alper Altındaş',
    version="0.0.1",
    author_email='aaltindas.help@gmail.com',
    description='Turkish word checker',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/aaltindas/tdil-0.0.1',
    project_urls={
        'Documentation': 'https://github.com/aaltindas/tdil-0.0.1',
        'Source Code': 'https://github.com/aaltindas/tdil-0.0.1',
    },
    package_dir={'': 'src'},
    packages=setuptools.find_packages(where='src'),
    classifiers=[
        # see https://pypi.org/classifiers/
        'Development Status :: 5 - Production/Stable',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
    ],
    python_requires='>=3.10',
    install_requires=['turkishnlp'],
)