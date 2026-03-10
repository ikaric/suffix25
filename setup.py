"""Build script for Cython extension."""

from setuptools import setup, Extension

try:
    from Cython.Build import cythonize

    extensions = cythonize(
        [
            Extension(
                "zlfi._core",
                sources=["src/zlfi/_core.pyx"],
                extra_compile_args=["-O3", "-march=native", "-ffast-math", "-fopenmp"],
                extra_link_args=["-fopenmp"],
            )
        ],
        compiler_directives={
            "boundscheck": False,
            "wraparound": False,
            "cdivision": True,
            "language_level": 3,
        },
    )
except ImportError:
    extensions = [
        Extension(
            "zlfi._core",
            sources=["src/zlfi/_core.c"],
            extra_compile_args=["-O3", "-march=native", "-ffast-math", "-fopenmp"],
            extra_link_args=["-fopenmp"],
        )
    ]

setup(
    ext_modules=extensions,
)
