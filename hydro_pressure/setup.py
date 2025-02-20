from setuptools import setup

setup(
    name='hydro_pressure',  # Replace with your package name
    version='0.0.0',
    packages=['hydro_pressure'],  # This should match your Python module's directory
    install_requires=[
        'rospy',
        'pyqt5',
        'pyqtgraph',
        'std_msgs',
        'serial'
    ],
)


