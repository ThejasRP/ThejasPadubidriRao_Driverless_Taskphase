from setuptools import find_packages, setup

package_name = 'taskone'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Thejas',
    maintainer_email='xxxxxxxxx@gmail.com',
    description='Package Task 1 of for FM DV TP',
    license='Apache-2.0',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            "pub = taskone.taskone_publisher:main",
            "sub = taskone.taskone_subscriber:main"
        ],
    },
)
