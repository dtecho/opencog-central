
#!/usr/bin/env python3
"""
Setup script for SkinTwin: Multiscale Computational Skin Model
"""

from setuptools import setup, Extension
from Cython.Build import cythonize
import numpy
import os

# Get OpenCog paths
opencog_include = os.environ.get('OPENCOG_INCLUDE_PATH', '/usr/local/include')
opencog_lib = os.environ.get('OPENCOG_LIB_PATH', '/usr/local/lib')

# Define Cython extensions
extensions = [
    Extension(
        "skin_twin.skin_cython",
        sources=[
            "src/cython/skin_cython.pyx",
            "src/core/SkinAtomSpace.cpp",
            "src/multiscale/MultiscaleModel.cpp",
            "src/integration/BiologicalIntegration.cpp",
            "src/integration/ChemicalIntegration.cpp"
        ],
        include_dirs=[
            "src",
            opencog_include,
            numpy.get_include(),
            "agi-bio",
            "cheminformatics"
        ],
        library_dirs=[opencog_lib],
        libraries=[
            "atomspace",
            "cogutil",
            "agi-bio",
            "cheminformatics",
            "boost_system",
            "boost_filesystem"
        ],
        language="c++",
        extra_compile_args=["-std=c++17", "-O3", "-Wall"],
        extra_link_args=["-std=c++17"]
    )
]

setup(
    name="skintwin",
    version="1.0.0",
    description="Multiscale Computational Skin Model for OpenCog",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="SkinTwin Development Team",
    author_email="skintwin@opencog.org",
    url="https://github.com/opencog/agi-skintwin",
    packages=[
        "skin_twin",
        "skin_twin.core",
        "skin_twin.multiscale",
        "skin_twin.integration",
        "skin_twin.analysis",
        "skin_twin.visualization"
    ],
    ext_modules=cythonize(extensions, compiler_directives={'language_level': 3}),
    install_requires=[
        "opencog",
        "numpy>=1.20.0",
        "scipy>=1.7.0",
        "matplotlib>=3.5.0",
        "pandas>=1.3.0",
        "networkx>=2.6",
        "scikit-learn>=1.0.0",
        "flask>=2.0.0",
        "plotly>=5.0.0",
        "dash>=2.0.0",
        "cython>=0.29.0"
    ],
    extras_require={
        "dev": [
            "pytest>=6.0.0",
            "pytest-cov>=3.0.0",
            "black>=22.0.0",
            "mypy>=0.950",
            "sphinx>=4.0.0",
            "sphinx-rtd-theme>=1.0.0"
        ],
        "bio": [
            "biopython>=1.79",
            "rdkit-pypi>=2022.3.0",
            "pubchempy>=1.0.4"
        ]
    },
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: C++",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
        "Topic :: Scientific/Engineering :: Chemistry",
        "Topic :: Scientific/Engineering :: Physics"
    ],
    entry_points={
        "console_scripts": [
            "skintwin=skin_twin.main:main",
            "skintwin-demo=skin_twin.main:demo",
            "skintwin-web=skin_twin.web_interface:main"
        ]
    },
    zip_safe=False,
    include_package_data=True,
    package_data={
        "skin_twin": [
            "data/*.csv",
            "data/*.json",
            "templates/*.html",
            "static/css/*.css",
            "static/js/*.js"
        ]
    }
)
