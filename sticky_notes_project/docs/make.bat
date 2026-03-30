\
    @ECHO OFF
    pushd %~dp0
    sphinx-build -b html source build\html
    popd
