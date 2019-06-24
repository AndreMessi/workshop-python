
##What are NumPy, SciPy, matplotlib, …?

#SciPy and friends can be used for a variety of tasks:

    NumPy’s array type augments the Python language with an efficient data structure useful for numerical work, e.g., manipulating matrices. NumPy also provides basic numerical routines, such as tools for finding eigenvectors.

    SciPy contains additional routines needed in scientific work: for example, routines for computing integrals numerically, solving differential equations, optimization, and sparse matrices.

    The matplotlib module produces high quality plots. With it you can turn your data or your models into figures for presentations or articles. No need to do the numerical work in one program, save the data, and plot it with another program.

    Using IPython makes interactive work easy. Data processing, exploration of numerical models, trying out operations on-the-fly allows to go quickly from an idea to a result. See the IPython site for many examples.

    There is a sizeable collection of both generic and application-specific numerical and scientific code, written using Python, NumPy and SciPy. Don’t reinvent the wheel, there may already be a pre-made solution for your problem. See Topical Software for a partial list.

    As Python is a popular general-purpose programming language, it has many advanced modules for building for example interactive applications (see e.g. wxPython and Traits) or web sites (see e.g. Django). Using SciPy with these is a quick way to build a fully-fledged scientific application.

#Installing via pip

    Most major projects upload official packages to the Python Package index. They can be installed on most operating systems using Python’s standard pip package manager.

    Note that you need to have Python and pip already installed on your system.

    You can install packages via commands such as:

    python -m pip install --user numpy scipy matplotlib ipython jupyter pandas sympy nose

    We recommend using an user install, using the --user flag to pip (note: do not use sudo pip, which can cause problems). This installs packages for your local user, and does not write to the system directories.
    Install system-wide via a Linux package manager

    Users on Linux can install packages from repositories provided by the distributions. These installations will be system-wide, and may have older package versions than those available using pip.

    Ubuntu & Debian

    sudo apt-get install python-numpy python-scipy python-matplotlib ipython ipython-notebook python-pandas python-sympy python-nose

    Users might also want to add the NeuroDebian repository for extra SciPy packages.