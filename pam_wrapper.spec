#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v18
# autospec commit: 356da62
#
# Source0 file verified with key 0x7EE0FC4DCC014E3D (asn@samba.org)
#
Name     : pam_wrapper
Version  : 1.1.7
Release  : 6
URL      : https://ftp.samba.org/pub/cwrap/pam_wrapper-1.1.7.tar.gz
Source0  : https://ftp.samba.org/pub/cwrap/pam_wrapper-1.1.7.tar.gz
Source1  : https://ftp.samba.org/pub/cwrap/pam_wrapper-1.1.7.tar.gz.asc
Source2  : 7EE0FC4DCC014E3D.pkey
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause GPL-3.0
Requires: pam_wrapper-lib = %{version}-%{release}
Requires: pam_wrapper-license = %{version}-%{release}
Requires: pam_wrapper-man = %{version}-%{release}
Requires: pam_wrapper-python = %{version}-%{release}
Requires: pam_wrapper-python3 = %{version}-%{release}
BuildRequires : Linux-PAM-dev
BuildRequires : buildreq-cmake
BuildRequires : doxygen
BuildRequires : glibc-dev
BuildRequires : gnupg
BuildRequires : python3
BuildRequires : python3-dev
BuildRequires : texlive
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
The manpage is written with asciidoc. To generate the manpage use:
a2x --doctype manpage --format manpage doc/pam_wrapper.1.txt

%package dev
Summary: dev components for the pam_wrapper package.
Group: Development
Requires: pam_wrapper-lib = %{version}-%{release}
Provides: pam_wrapper-devel = %{version}-%{release}
Requires: pam_wrapper = %{version}-%{release}

%description dev
dev components for the pam_wrapper package.


%package lib
Summary: lib components for the pam_wrapper package.
Group: Libraries
Requires: pam_wrapper-license = %{version}-%{release}

%description lib
lib components for the pam_wrapper package.


%package license
Summary: license components for the pam_wrapper package.
Group: Default

%description license
license components for the pam_wrapper package.


%package man
Summary: man components for the pam_wrapper package.
Group: Default

%description man
man components for the pam_wrapper package.


%package python
Summary: python components for the pam_wrapper package.
Group: Default
Requires: pam_wrapper-python3 = %{version}-%{release}

%description python
python components for the pam_wrapper package.


%package python3
Summary: python3 components for the pam_wrapper package.
Group: Default
Requires: python3-core

%description python3
python3 components for the pam_wrapper package.


%prep
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) 7EE0FC4DCC014E3D' gpg.status
%setup -q -n pam_wrapper-1.1.7
cd %{_builddir}/pam_wrapper-1.1.7
pushd ..
cp -a pam_wrapper-1.1.7 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1722353795
mkdir -p clr-build
pushd clr-build
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
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
pushd ../buildavx2/
mkdir -p clr-build-avx2
pushd clr-build-avx2
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
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
popd

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
export SOURCE_DATE_EPOCH=1722353795
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pam_wrapper
cp %{_builddir}/pam_wrapper-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pam_wrapper/8624bcdae55baeef00cd11d5dfcfa60f68710a02 || :
cp %{_builddir}/pam_wrapper-%{version}/cmake/Modules/COPYING-CMAKE-SCRIPTS %{buildroot}/usr/share/package-licenses/pam_wrapper/ff3ed70db4739b3c6747c7f624fe2bad70802987 || :
export GOAMD64=v2
pushd ../buildavx2/
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
## Remove excluded files
rm -f %{buildroot}*/usr/lib64/pkgconfig/libpamtest.pc
rm -f %{buildroot}*/usr/lib64/pkgconfig/pam_wrapper.pc
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/libpamtest.h
/usr/lib64/cmake/pam_wrapper/pam_wrapper-config-version.cmake
/usr/lib64/cmake/pam_wrapper/pam_wrapper-config.cmake
/usr/lib64/cmake/pamtest/pamtest-config-relwithdebinfo.cmake
/usr/lib64/cmake/pamtest/pamtest-config-version.cmake
/usr/lib64/cmake/pamtest/pamtest-config.cmake
/usr/lib64/libpam_wrapper.so
/usr/lib64/libpamtest.so

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libpam_wrapper.so.0.0.10
/V3/usr/lib64/libpamtest.so.0.0.10
/V3/usr/lib64/pam_wrapper/pam_chatty.so
/V3/usr/lib64/pam_wrapper/pam_get_items.so
/V3/usr/lib64/pam_wrapper/pam_matrix.so
/V3/usr/lib64/pam_wrapper/pam_set_items.so
/usr/lib64/libpam_wrapper.so.0
/usr/lib64/libpam_wrapper.so.0.0.10
/usr/lib64/libpamtest.so.0
/usr/lib64/libpamtest.so.0.0.10
/usr/lib64/pam_wrapper/pam_chatty.so
/usr/lib64/pam_wrapper/pam_get_items.so
/usr/lib64/pam_wrapper/pam_matrix.so
/usr/lib64/pam_wrapper/pam_set_items.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pam_wrapper/8624bcdae55baeef00cd11d5dfcfa60f68710a02
/usr/share/package-licenses/pam_wrapper/ff3ed70db4739b3c6747c7f624fe2bad70802987

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/pam_wrapper.1
/usr/share/man/man8/pam_chatty.8
/usr/share/man/man8/pam_get_items.8
/usr/share/man/man8/pam_matrix.8
/usr/share/man/man8/pam_set_items.8

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/V3/usr/lib/python3*/*
/usr/lib/python3*/*
