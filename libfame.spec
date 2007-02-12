# 
# TODO:
# - fix mmx sse stuff
# - http://sourceforge.net/tracker/index.php?func=detail&aid=977600&group_id=19741&atid=119741
# - fix -march forcing in configure.in
#
# Conditional build:
%bcond_without	static_libs	# don't build static library
#
Summary:	Fast Assembly Mpeg Encoding library
Summary(pl.UTF-8):   Szybka biblioteka kodująca MPEG
Name:		libfame
Version:	0.9.1
Release:	4
License:	LGPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/fame/%{name}-%{version}.tar.gz
# Source0-md5:	880085761e17a3b4fc41f4f6f198fd3b
Patch0:		%{name}-am18.patch
Patch1:		%{name}-gcc.patch
URL:		http://fame.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FAME is a library for fast MPEG encoding.

%description -l pl.UTF-8
FAME to biblioteka do szybkiego kodowania MPEG.

%package devel
Summary:	Includes to develop using FAME
Summary(pl.UTF-8):   Pliki nagłówkowe FAME
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
FAME is a library for fast MPEG encoding. This package contains
include files and other resources you can use to develop FAME
applications.

%description devel -l pl.UTF-8
FAME to biblioteka do szybkiego kodowania MPEG. Ten pakiet zawiera
pliki nagłówkowe i inne potrzebne do tworzenia aplikacji
korzystających z FAME.

%package static
Summary:	FAME static libraries
Summary(pl.UTF-8):   Biblioteki statyczne FAME
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
FAME is a library for fast MPEG encoding. This package contains static
version of FAME library.

%description static -l pl.UTF-8
FAME to biblioteka do szybkiego kodowania MPEG. Ten pakiet zawiera
statyczną wersję biblioteki FAME.

%prep
%setup -q
%patch0 -p1
%patch1 -p1 

rm -f acinclude.m4

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	%{!?with_static_libs:--disable-static}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS CHANGES README TODO
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*-config
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/*.la
%{_includedir}/fame*.h
%{_aclocaldir}/*
%{_mandir}/man3/*

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
%endif
