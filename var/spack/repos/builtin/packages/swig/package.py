# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os


from spack import *


class Swig(AutotoolsPackage):
    """SWIG is an interface compiler that connects programs written in
       C and C++ with scripting languages such as Perl, Python, Ruby,
       and Tcl. It works by taking the declarations found in C/C++
       header files and using them to generate the wrapper code that
       scripting languages need to access the underlying C/C++
       code. In addition, SWIG provides a variety of customization
       features that let you tailor the wrapping process to suit your
       application."""

    homepage = "http://www.swig.org"
    url      = "http://prdownloads.sourceforge.net/swig/swig-3.0.12.tar.gz"

    version('master', git='https://github.com/swig/swig.git')
    version('4.0.0', sha256='e8a39cd6437e342cdcbd5af27a9bf11b62dc9efec9248065debcb8276fcbb925')
    version('3.0.12', sha256='7cf9f447ae7ed1c51722efc45e7f14418d15d7a1e143ac9f09a668999f4fc94d')
    version('3.0.11', sha256='d9031d531d7418829a54d0d51c4ed9007016b213657ec70be44031951810566e')
    version('3.0.10', sha256='2939aae39dec06095462f1b95ce1c958ac80d07b926e48871046d17c0094f44c')
    version('3.0.8',  sha256='58a475dbbd4a4d7075e5fe86d4e54c9edde39847cdb96a3053d87cb64a23a453')
    version('3.0.2',  sha256='a2669657cabcedc371f63c0457407a183e0b6b2ef4e7e303c1ec9a3964cc7813')
    version('2.0.12', sha256='65e13f22a60cecd7279c59882ff8ebe1ffe34078e85c602821a541817a4317f7')
    version('2.0.2',  sha256='6e6b5e8db2bbf2761ff789a3109e4f12ca664ec178d3a164ed0dc273d346c11f')
    version('1.3.40', sha256='1945b3693bcda6777bd05fef1015a0ad1a4604cde4a4a0a368b61ccfd143ac09')
    version('fortran', branch='master',
            git='https://github.com/swig-fortran/swig.git')

    depends_on('pcre')

    # Git repository does *not* include configure script
    for _version in ['@fortran', '@master']:
        depends_on('autoconf', type='build', when=_version)
        depends_on('automake', type='build', when=_version)
        depends_on('libtool', type='build', when=_version)
    depends_on('pkgconfig', type='build')

    build_directory = 'spack-build'

    @run_after('install')
    def create_symlink(self):
        # CMake compatibility: see https://github.com/spack/spack/pull/6240
        with working_dir(self.prefix.bin):
            os.symlink('swig', 'swig{0}'.format(self.spec.version.up_to(2)))

    for _version in ['@fortran', '@master']:
        @when(_version)
        def autoreconf(self, spec, prefix):
            which('sh')('./autogen.sh')
