# Note that this is NOT a relocatable package
%define ver      0.8.8
%define rel      1
%define prefix   /usr

Summary:   Fast Assembly Mpeg Encoding library
Name:      libfame
Version:   %ver
Release:   %rel
Copyright: LGPL
Group:     System Environment/Libraries
Source0:   libfame-%{PACKAGE_VERSION}.tar.gz
URL:       http://fame.sourceforge.net
BuildRoot: /tmp/libfame-%{PACKAGE_VERSION}-root
Packager:  Vivien Chappelier <vivien.chappelier@enst-bretagne.fr>
Docdir: %{prefix}/doc

%description
FAME is a library for fast MPEG encoding.

%package devel
Summary: Libraries and include to develop using FAME
Group: Development/Libraries
Requires: %{name}

%description devel
FAME is a library for fast MPEG encoding.

This is the libraries, include files and other resources you can use
to develop FAME applications.

%prep
rm -rf ${RPM_BUILD_ROOT}

%setup -q

%build
# Needed for snapshot releases.
if [ ! -f configure ]; then
  CFLAGS="$RPM_OPT_FLAGS" ./autogen.sh --prefix=%prefix
else
  CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=%prefix
fi

if [ "$SMP" != "" ]; then
  (make "MAKE=make -k -j $SMP"; exit 0)
  make
else
  make
fi

%install
rm -rf $RPM_BUILD_ROOT

make prefix=$RPM_BUILD_ROOT%{prefix} install

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%defattr(-, root, root)
%doc CHANGES COPYING README
%{_libdir}/lib*.so.*

%files devel
%defattr(-, root, root)
%doc CHANGES COPYING README
%{_bindir}/*-config
%{_libdir}/lib*.so
%{_libdir}/*a
%{_includedir}/fame*.h
%{_datadir}/aclocal/*
%{prefix}/man/man3/*
%changelog
