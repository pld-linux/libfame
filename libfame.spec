Summary:	Fast Assembly Mpeg Encoding library
Summary(pl):	Szybkaa biblioteka koduj±ca MPEG
Name:		libfame
Version:	0.8.9
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://prdownloads.sourceforge.net/fame/%{name}-%{version}.tar.gz
URL:		http://fame.sourceforge.net
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FAME is a library for fast MPEG encoding.

%description -l pl
FAME to biblioteka do szybkiego kodowania MPEG.

%package devel
Summary:	Includes to develop using FAME
Summary(pl):	Pliki nag³ówkowe FAME
Group:		Development/Libraries
Requires:	%{name}

%description devel
FAME is a library for fast MPEG encoding. This package contains
include files and other resources you can use to develop FAME
applications.

%description devel -l pl
FAME to biblioteka do szybkiego kodowania MPEG. Ten pakiet zawiera
pliki nag³ówkowe i inne potrzebne do tworzenia aplikacji
korzystaj±cych z FAME.

%package static
Summary:	FAME static libraries
Summary(pl):	Biblioteki statyczne FAME
Group:		Development/Libraries
Requires:	%{name}

%description static
FAME is a library for fast MPEG encoding. This package contains static
version of FAME library.

%description devel -l pl
FAME to biblioteka do szybkiego kodowania MPEG. Ten pakiet zawiera
statyczn± wersjê biblioteki FAME.

%prep
%setup -q

%build
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

gzip -9nf CHANGES README

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGES.gz README.gz
%{_libdir}/lib*.so.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*-config
%{_libdir}/lib*.so
%{_includedir}/fame*.h
%{_aclocaldir}/*
%{_mandir}/man3/*

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
