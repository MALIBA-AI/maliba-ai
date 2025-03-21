from setuptools import setup, find_packages

setup(
    name="maliba_ai",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[
        "torch>=2.0.0",
        "librosa",
        "transformers @ git+https://github.com/huggingface/transformers.git@main",
        "peft @ git+https://github.com/huggingface/peft.git@main",
    ],
    author="MALIBA-AI",
    author_email="sudoping01@gmail.com",
    description="A Whisper-based Automatic Speech Recognition package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/MALIBA-/maliba-ai",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)