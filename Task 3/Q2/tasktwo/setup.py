from setuptools import find_packages, setup

package_name = 'tasktwo'

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
    maintainer='hp',
    maintainer_email='hp@todo.todo',
    description='TODO: Package description',
    license='Apache-2.0',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            "node1 = tasktwo.node1_publisher:main",
            "node2 = tasktwo.node2_pubsub:main",
            "node3 = tasktwo.node3_pubsub:main",
        ],
    },
)
