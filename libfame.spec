Summary:	Fast Assembly Mpeg Encoding library
Summary(pl):	Szybkaa biblioteka koduj±ca MPEG
Name:		libfame
Version:	0.8.9
Release:	1
License:	LGPL
Group:		Libraries
Group(cs):	Knihovny
Group(da):	Biblioteker
Group(de):	Bibliotheken
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(is):	Ağgerğasöfn
Group(it):	Librerie
Group(ja):	¥é¥¤¥Ö¥é¥ê
Group(no):	Biblioteker
Group(pl):	Biblioteki
Group(pt):	Bibliotecas
Group(pt_BR):	Bibliotecas
Group(ru):	âÉÂÌÉÏÔÅËÉ
Group(sl):	Knji¾nice
Group(sv):	Bibliotek
Group(uk):	â¦ÂÌ¦ÏÔÅËÉ
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
Group(cs):	Vıvojové prostøedky/Knihovny
Group(da):	Udvikling/Biblioteker
Group(de):	Entwicklung/Bibliotheken
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(is):	Şróunartól/Ağgerğasöfn
Group(it):	Sviluppo/Librerie
Group(ja):	³«È¯/¥é¥¤¥Ö¥é¥ê
Group(no):	Utvikling/Bibliotek
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(pt):	Desenvolvimento/Bibliotecas
Group(ru):	òÁÚÒÁÂÏÔËÁ/âÉÂÌÉÏÔÅËÉ
Group(sl):	Razvoj/Knji¾nice
Group(sv):	Utveckling/Bibliotek
Group(uk):	òÏÚÒÏÂËÁ/â¦ÂÌ¦ÏÔÅËÉ
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
Group(cs):	Vıvojové prostøedky/Knihovny
Group(da):	Udvikling/Biblioteker
Group(de):	Entwicklung/Bibliotheken
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(is):	Şróunartól/Ağgerğasöfn
Group(it):	Sviluppo/Librerie
Group(ja):	³«È¯/¥é¥¤¥Ö¥é¥ê
Group(no):	Utvikling/Bibliotek
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(pt):	Desenvolvimento/Bibliotecas
Group(ru):	òÁÚÒÁÂÏÔËÁ/âÉÂÌÉÏÔÅËÉ
Group(sl):	Razvoj/Knji¾nice
Group(sv):	Utveckling/Bibliotek
Group(uk):	òÏÚÒÏÂËÁ/â¦ÂÌ¦ÏÔÅËÉ
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
