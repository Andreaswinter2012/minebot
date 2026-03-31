from setuptools import setup, find_packages

setup(
    name="minebot",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pyautogui",
        "pydirectinput",
        "opencv-python",
        "Pillow",
    ],
    author="Andreaswinter2012",
    description="The open-souce libery for minecraft bot build library",
)
