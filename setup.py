from setuptools import setup, find_packages


setup(
    name='frasco-trello',
    version='0.1',
    url='http://github.com/frascoweb/frasco-trello',
    license='MIT',
    author='Maxime Bouroumeau-Fuseau',
    author_email='maxime.bouroumeau@gmail.com',
    description="Trello integration for Frasco",
    packages=find_packages(),
    zip_safe=False,
    platforms='any',
    install_requires=[
        # 'frasco',
        # 'frasco-users',
        'py-trello==0.2.3-dev'
    ],
    dependency_links=[
        'git+https://github.com/sarumont/py-trello.git#egg=trello-0.2.3-dev'
    ]
)