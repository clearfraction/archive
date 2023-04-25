Name: rencode-python3
Version: 1.0.6
Release: 1
Summary: A Module similar to bencode from the BitTorrent project

License: GPLv3
URL: https://github.com/aresch/rencode
Source0: https://github.com/aresch/rencode/archive/v1.0.6.tar.gz
Patch0: ffc40a7d3fb9f7007eb93abf98949aa752a7ffae.patch
Patch1: 5c928f14567fabc9efb8bbb8ac5e0eef03c61541.patch

BuildRequires: python3-dev
BuildRequires: pip
BuildRequires: Cython

%description
pyparsing is a module that can be used to easily and directly configure syntax
The rencode module is similar to bencode from the BitTorrent project. For 
complex, heterogeneous data structures with many small elements

%prep
%setup -n rencode-1.0.6

%patch0 -p1
%patch1 -p1

%build

unset http_proxy
unset no_proxy 
unset https_proxy
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1572997294
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
unset http_proxy
unset no_proxy 
unset https_proxy

python3 -tt setup.py build  install --root=%{buildroot}

%files 
/usr/lib/python3.8/site-packages/rencode-1.0.6-py3.8.egg-info/*
/usr/lib/python3.8/site-packages/rencode/

%changelog

* Thu Jan 16 2020 David Va <davidva AT tuta DOT io> - 1.0.6-1
* Initial build
