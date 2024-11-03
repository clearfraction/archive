#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: make
# autospec version: v12
# autospec commit: fbcebd0
#
Name     : libglibutil
Version  : 1.0.79
Release  : 5
URL      : https://github.com/sailfishos/libglibutil/archive/refs/tags/1.0.79.tar.gz
Source0  : https://github.com/sailfishos/libglibutil/archive/refs/tags/1.0.79.tar.gz
Summary  : Library of glib utilities
Group    : Development/Tools
License  : BSD-3-Clause
Requires: libglibutil-lib = %{version}-%{release}
BuildRequires : glib-dev
BuildRequires : pkgconfig(gobject-2.0)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Provides glib utility functions and macros

%package dev
Summary: dev components for the libglibutil package.
Group: Development
Requires: libglibutil-lib = %{version}-%{release}
Provides: libglibutil-devel = %{version}-%{release}
Requires: libglibutil = %{version}-%{release}

%description dev
dev components for the libglibutil package.


%package lib
Summary: lib components for the libglibutil package.
Group: Libraries

%description lib
lib components for the libglibutil package.


%prep
%setup -q -n libglibutil-1.0.79
cd %{_builddir}/libglibutil-1.0.79

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1718794772
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
make  %{?_smp_mflags}


%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1718794772
rm -rf %{buildroot}
export GOAMD64=v2
GOAMD64=v2
DESTDIR=%{buildroot} PREFIX=/usr LIBDIR=/usr/lib64 make install-dev

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/gutil/gutil_datapack.h
/usr/include/gutil/gutil_history.h
/usr/include/gutil/gutil_idlepool.h
/usr/include/gutil/gutil_idlequeue.h
/usr/include/gutil/gutil_inotify.h
/usr/include/gutil/gutil_intarray.h
/usr/include/gutil/gutil_ints.h
/usr/include/gutil/gutil_log.h
/usr/include/gutil/gutil_macros.h
/usr/include/gutil/gutil_misc.h
/usr/include/gutil/gutil_objv.h
/usr/include/gutil/gutil_ring.h
/usr/include/gutil/gutil_strv.h
/usr/include/gutil/gutil_timenotify.h
/usr/include/gutil/gutil_types.h
/usr/include/gutil/gutil_version.h
/usr/include/gutil/gutil_weakref.h
/usr/lib64/libglibutil.so
/usr/lib64/pkgconfig/libglibutil.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libglibutil.so.1
/usr/lib64/libglibutil.so.1.0
/usr/lib64/libglibutil.so.1.0.79