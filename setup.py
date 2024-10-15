from setuptools import find_packages, setup

package_name = 'the_ferg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/' + package_name + '/launch', ['launch/run_webots.launch.py']),
        ('share/' + package_name + '/worlds', ['worlds/FirstFloorStudentCenter.wbt']), 
('share/' + package_name + '/marker', ['marker'])
   ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='anastasiaspencer',
    maintainer_email='akspencer1@crimson.ua.edu',
    description='This package is for CS 465 Project Part 1',
    license='Apache 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
