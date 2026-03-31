from setuptools import setup, find_packages

setup(
    name="minelib",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "pyautogui",
        "pydirectinput",
        "opencv-python",
        "Pillow",
    ],
    author="Andreas7313",
    description="The open-souce libery for minecraft bot build library",
)
