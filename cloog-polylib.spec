Summary:	The Chunky Loop Generator
Summary(pl.UTF-8):	Chunky Loop Generator - generator pętli cząstkowych
Name:		cloog-polylib
Version:	0.16.1
Release:	2
License:	LGPL v2.1+
Group:		Development/Tools
Source0:	http://www.bastoul.net/cloog/pages/download/%{name}-%{version}.tar.gz
# Source0-md5:	ba3bef32edfe9c61d0558132da5f32f2
URL:		http://www.cloog.org/
BuildRequires:	autoconf >= 2.13
BuildRequires:	automake
BuildRequires:	gmp-devel >= 4.1.3
BuildRequires:	gmp-c++-devel >= 4.1.3
BuildRequires:	libtool
BuildRequires:	polylib-devel
BuildRequires:	texinfo >= 4.12
Requires:	%{name}-libs = %{version}-%{release}
Provides:	cloog = %{version}
Obsoletes:	cloog
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CLooG is a software which generates loops for scanning Z-polyhedra.
That is, CLooG finds the code or pseudo-code where each integral point
of one or more parametrized polyhedron or parametrized polyhedra union
is reached. CLooG is designed to avoid control overhead and to produce
a very efficient code.

This version is based on PolyLib.

%description -l pl.UTF-8
CLooG to oprogramowanie generujące pętle do przeszukiwania
Z-wielościanów (Z-polyhedra). Oznacza to, że CLooG znajduje kod lub
pseudokod osiągający każdy punkt całkowity jednego lub większej liczby
sparametryzowanych wielościanów lub sum sparametryzowanych
wielościanów. CLooG jest zaprojektowany z myślą o zapobieganiu
narzutowi na sterowaniu oraz generowaniu bardzo wydajnego kodu.

Ta wersja jest oparta na bibliotece PolyLib.

%package libs
Summary:	Chunky Loop Generator shared library - PolyLib based version
Summary(pl.UTF-8):	Biblioteka współdzielona Chunky Loop Generatora - wersja oparta na PolyLib
Group:		Libraries

%description libs
Chunky Loop Generator shared library - PolyLib based version.

%description libs -l pl.UTF-8
Biblioteka współdzielona Chunky Loop Generatora - wersja oparta na
PolyLib.

%package devel
Summary:	Header files for the PolyLib based version of Chunky Loop Generator
Summary(pl.UTF-8):	Pliki nagłówkowe opartej na PolyLib wersji Chunky Loop Generatora
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	gmp-devel >= 4.1.3
Requires:	gmp-c++-devel >= 4.1.3
Requires:	polylib-devel
Provides:	cloog-devel = %{version}
Conflicts:	cloog-isl-devel
Conflicts:	cloog-ppl-devel

%description devel
The header files for Chunky Loop Generator library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki Chunky Loop Generatora.

%package static
Summary:	Static library of PolyLib based version of Chunky Loop Generator
Summary(pl.UTF-8):	Statyczna biblioteka opartej na PolyLib wersji Chunky Loop Generatora
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static library of PolyLib based version of Chunky Loop Generator.

%description static -l pl.UTF-8
Statyczna biblioteka opartej na PolyLib wersji Chunky Loop Generatora.

%prep
%setup -q

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	INSTALL="%{__install} -p" \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/cloog

%files libs
%defattr(644,root,root,755)
%doc cloog-core/README
%attr(755,root,root) %{_libdir}/libcloog-polylib.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcloog-polylib.so.1

%files devel
%defattr(644,root,root,755)
%doc cloog-core/doc/cloog.pdf
%attr(755,root,root) %{_libdir}/libcloog-polylib.so
%{_libdir}/libcloog-polylib.la
%dir %{_includedir}/cloog
%{_includedir}/cloog/*.h
%{_includedir}/cloog/matrix
%{_includedir}/cloog/polylib
%{_pkgconfigdir}/cloog-polylib.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libcloog-polylib.a
