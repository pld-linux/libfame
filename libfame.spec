Summary:	Fast Assembly Mpeg Encoding library
Summary(pl):	Szybkaa biblioteka koduj╠ca MPEG
Name:		libfame
Version:	0.8.8
Release:	2
License:	LGPL
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	Библиотеки
Group(uk):	Б╕бл╕отеки
Source0:	http://prdownloads.sourceforge.net/fame/%{name}-%{version}.tar.gz
URL:		http://fame.sourceforge.net
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FAME is a library for fast MPEG encoding.

%description -l pl
FAME to biblioteka do szybkiego kodowania MPEG.

%package devel
Summary:	Includes to develop using FAME
Summary(pl):	Pliki nagЁСwkowe FAME
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Разработка/Библиотеки
Group(uk):	Розробка/Б╕бл╕отеки
Requires:	%{name}

%description devel
FAME is a library for fast MPEG encoding. This package contains
include files and other resources you can use to develop FAME
applications.

%description devel -l pl
FAME to biblioteka do szybkiego kodowania MPEG. Ten pakiet zawiera
pliki nagЁСwkowe i inne potrzebne do tworzenia aplikacji
korzystaj╠cych z FAME.

%package static
Summary:	FAME static libraries
Summary(pl):	Biblioteki statyczne FAME
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Разработка/Библиотеки
Group(uk):	Розробка/Б╕бл╕отеки
Requires:	%{name}

%description static
FAME is a library for fast MPEG encoding. This package contains
static version of FAME library.

%description devel -l pl
FAME to biblioteka do szybkiego kodowania MPEG. Ten pakiet zawiera
statyczn╠ wersjЙ biblioteki FAME.

%prep
%setup -q

%build
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} prefix=$RPM_BUILD_ROOT%{_prefix} install

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
