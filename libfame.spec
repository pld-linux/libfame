Summary:	Fast Assembly Mpeg Encoding library
Name:		libfame
Version:	0.8.8
Release:	1
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

%package devel
Summary:	Libraries and include to develop using FAME
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
FAME is a library for fast MPEG encoding.

This is the libraries, include files and other resources you can use
to develop FAME applications.

%prep
rm -rf ${RPM_BUILD_ROOT}

%setup -q

%build
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} prefix=$RPM_BUILD_ROOT%{_prefix} install

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGES COPYING README
%{_libdir}/lib*.so.*

%files devel
%defattr(644,root,root,755)
%doc CHANGES COPYING README
%attr(755,root,root) %{_bindir}/*-config
%{_libdir}/lib*.so
%{_libdir}/*a
%{_includedir}/fame*.h
%{_aclocaldir}/*
%{_mandir}/man3/*
