#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ebtables
Version  : v2.0.10
Release  : 35
URL      : ftp://ftp.netfilter.org/pub/ebtables/ebtables-v2.0.10-4.tar.gz
Source0  : ftp://ftp.netfilter.org/pub/ebtables/ebtables-v2.0.10-4.tar.gz
Summary  : Ethernet Bridge frame table administration tool
Group    : Development/Tools
License  : GPL-2.0
Requires: ebtables-bin
Requires: ebtables-data
Requires: ebtables-doc
Patch1: 0001-Remove-Werror-from-compilation.patch
Patch2: 0002-No-root-installation.patch
Patch3: 0003-link-ebtables-with-no-as-needed-and-adjust-the-link-.patch
Patch4: 0004-Do-not-install-sysv-init-script-nor-config-snipped-s.patch
Patch5: 0004-Changed-the-ethertypes-path.patch

%description
Ethernet bridge tables is a firewalling tool to transparantly filter network
traffic passing a bridge. The filtering possibilities are limited to link
layer filtering and some basic filtering on higher network layers.

The ebtables tool can be used together with the other Linux filtering tools,
like iptables. There are no incompatibility issues.

%package bin
Summary: bin components for the ebtables package.
Group: Binaries
Requires: ebtables-data

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
Requires: ebtables-bin
Requires: ebtables-data

%description dev
dev components for the ebtables package.


%package doc
Summary: doc components for the ebtables package.
Group: Documentation

%description doc
doc components for the ebtables package.


%prep
%setup -q -n ebtables-v2.0.10-4
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
make V=1 %{?_smp_mflags}

%install
rm -rf %{buildroot}
%make_install BINDIR=%{_sbindir} ETHERTYPESPATH=/usr/share/defaults/ebtables MANDIR=%{_mandir} LIBDIR=%{_libdir}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/ebtables
/usr/bin/ebtables-restore
/usr/bin/ebtables-save

%files data
%defattr(-,root,root,-)
/usr/share/defaults/ebtables/ethertypes

%files dev
%defattr(-,root,root,-)
/usr/lib64/*.so

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man8/*