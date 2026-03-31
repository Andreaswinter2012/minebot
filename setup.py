from setuptools import setup, find_packages

setup(
    name="minelib",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pyautogui",
        "pydirectinput",
        "opencv-python",
        "Pillow",
    ],
    author="Andreaswinter2012",
    description="Библиотека для автоматизации действий в Minecraft",
)
