from setuptools import setup, find_packages


def readme():
    with open('README.rst') as f:
        return f.read()

setup(  name='bnGetGitRepos',
        version='0.1.0b0',
        description=' Download git repositories from a cloud Git service',
        packages=find_packages('src'),
        package_dir={'': 'src'},
        long_description=readme(),
        classifiers=[
            'Development Status :: 3 - Alpha',
	     'Programming Language :: Python :: 3',
            'Intended Audience :: Developers',
        ],
        keywords='git gitlab github amazon repositories',
        url='https://github.com/ahestevenz/ll',
        author='Ariel Hernandez <ariel.h.estevenz@ieee.org>',
        author_email='ariel.h.estevenz@ieee.org',
        license='Proprietary',
        install_requires=[
            'numpy', 'pexpect'
        ],
        test_suite='nose.collector',
        tests_require=['nose'],
        entry_points = {
            'console_scripts': ['bn-get-repositories=bnGetGitRepos.scripts.get_repos:main',
            ],
        },
        include_package_data=True,
        zip_safe=True
    )
