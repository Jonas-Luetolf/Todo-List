try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name="Todo-List",
    version=2.0,
    description='a todo-list cli',
 
    author='Jonas Lütolf',
    license='MIT',
    url='http://github.com/Jonas-Luetolf/Todo-List',

    python_requires='>=3.6',
    install_requires=[
        'PyYAML (>= 3.12)',
    ],
    package_dir={'': './'},
    packages=['table',"todo_list"],
    scripts=['todo-list'],
)
