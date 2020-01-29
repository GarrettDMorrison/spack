# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import spack
from spack.main import SpackCommand

python = SpackCommand('python')

test_string = "Ran the spack python module"


def test_python():
    out = python('-c', 'import spack; print(spack.spack_version)')
    assert out.strip() == spack.spack_version


def test_python_with_module():
    out = python('-m', 'site')
    assert 'sys.path' in out.strip()


def test_python_raises():
    out = python('--foobar', fail_on_error=False)
    assert "Error: Unknown arguments" in out
