#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xAB4655A126D292E4 (coreteam@netfilter.org)
#
Name     : ebtables
Version  : 2.0.11
Release  : 50
URL      : https://www.netfilter.org/pub/ebtables/ebtables-2.0.11.tar.gz
Source0  : https://www.netfilter.org/pub/ebtables/ebtables-2.0.11.tar.gz
Source1  : https://www.netfilter.org/pub/ebtables/ebtables-2.0.11.tar.gz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: ebtables-bin = %{version}-%{release}
Requires: ebtables-data = %{version}-%{release}
Requires: ebtables-lib = %{version}-%{release}
Requires: ebtables-license = %{version}-%{release}
Requires: ebtables-man = %{version}-%{release}
Requires: iptables
BuildRequires : iptables

%description
No detailed description available

%package bin
Summary: bin components for the ebtables package.
Group: Binaries
Requires: ebtables-data = %{version}-%{release}
Requires: ebtables-license = %{version}-%{release}

%description bin
bin components for the ebtables package.


%package data
Summary: data components for the ebtables package.
Group: Data

%description data
data components for the ebtables package.


%package dev
Summary: dev components for the ebtables package.
Group: Development
Requires: ebtables-lib = %{version}-%{release}
Requires: ebtables-bin = %{version}-%{release}
Requires: ebtables-data = %{version}-%{release}
Provides: ebtables-devel = %{version}-%{release}
Requires: ebtables = %{version}-%{release}

%description dev
dev components for the ebtables package.


%package lib
Summary: lib components for the ebtables package.
Group: Libraries
Requires: ebtables-data = %{version}-%{release}
Requires: ebtables-license = %{version}-%{release}

%description lib
lib components for the ebtables package.


%package license
Summary: license components for the ebtables package.
Group: Default

%description license
license components for the ebtables package.


%package man
Summary: man components for the ebtables package.
Group: Default

%description man
man components for the ebtables package.


%prep
%setup -q -n ebtables-2.0.11
cd %{_builddir}/ebtables-2.0.11

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1594869781
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%configure --disable-static --sysconfdir=/usr/share/defaults/ebtables
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1594869781
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/ebtables
cp %{_builddir}/ebtables-2.0.11/COPYING %{buildroot}/usr/share/package-licenses/ebtables/f65e47501f802ee8bdca3650b3b80b9cf933bf8f
%make_install BINDIR=%{_sbindir} ETHERTYPESPATH=/usr/share/defaults/ebtables MANDIR=%{_mandir} LIBDIR=%{_libdir}
## Remove excluded files
rm -f %{buildroot}/usr/bin/ebtables
rm -f %{buildroot}/usr/bin/ebtables-restore
rm -f %{buildroot}/usr/bin/ebtables-save

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/ebtables-legacy
/usr/bin/ebtables-legacy-restore
/usr/bin/ebtables-legacy-save
/usr/bin/ebtablesd
/usr/bin/ebtablesu

%files data
%defattr(-,root,root,-)
/usr/share/defaults/ebtables/ethertypes

%files dev
%defattr(-,root,root,-)
/usr/lib64/libebtc.so

%files lib
%defattr(-,root,root,-)
/usr/lib64/libebtc.so.0
/usr/lib64/libebtc.so.0.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/ebtables/f65e47501f802ee8bdca3650b3b80b9cf933bf8f

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man8/ebtables-legacy.8
