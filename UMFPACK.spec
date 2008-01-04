Summary:	UMFPACK: sparse multifrontal LU factorization
Summary(pl.UTF-8):	UMFPACK - wielofrontalny rozkład LU macierzy rzadkich
Name:		UMFPACK
Version:	5.2.0
Release:	2
License:	GPL v2+
Group:		Libraries
Source0:	http://www.cise.ufl.edu/research/sparse/umfpack/%{name}-%{version}.tar.gz
# Source0-md5:	8ad2d68c7c49dfcdd8321e806e6c611c
Patch0:		%{name}-ufconfig.patch
Patch1:		%{name}-shared.patch
Patch2:		%{name}-include-AMD.patch
URL:		http://www.cise.ufl.edu/research/sparse/umfpack/
BuildRequires:	AMD-devel
BuildRequires:	UFconfig
BuildRequires:	blas-devel
BuildRequires:	libtool >= 2:1.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
UMFPACK is a set of routines for solving unsymmetric sparse linear
systems, Ax=b, using the Unsymmetric MultiFrontal method. Written in
ANSI/ISO C, with a MATLAB (Version 6.0 and later) interface. Appears
as a built-in routine (for lu, backslash, and forward slash) in
MATLAB. Includes a MATLAB interface, a C-callable interface, and a
Fortran-callable interface. Note that "UMFPACK" is pronounced in two
syllables, "Umph Pack". It is not "You Em Ef Pack".

%description -l pl.UTF-8
UMFPACK to zbiór procedur do rozwiązywania niesymetrycznych rzadkich
układów równań liniowych Ax=b przy użyciu metody UMF (Unsymmetric
MultiFrontal). Jest napisany w ANSI/ISO C z interfejsem do MATLAB-a
(w wersji 6.0 i nowszych). W MATLAB-ie jest dostępny jako wbudowana
procedura (dla lu, backslasha i slasha). Oprócz interfejsu dla
MATLAB-a dostępny jest interfejs dostępny z C i Fortranu. Uwaga:
"UMFPACK" powinno się wymawiać jako dwie sylaby: "Umf Pak"; nie jako
"U Em Ef Pak".

%package devel
Summary:	Header files for UMFPACK library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki UMFPACK
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	AMD-devel
Requires:	UFconfig

%description devel
Header files for UMFPACK library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki UMFPACK.

%package static
Summary:	Static UMFPACK library
Summary(pl.UTF-8):	Statyczna biblioteka UMFPACK
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static UMFPACK library.

%description static -l pl.UTF-8
Statyczna biblioteka UMFPACK.

%prep
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}" \
	libdir=%{_libdir}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_includedir}/umfpack

%{__make} -C Lib install \
	DESTDIR=$RPM_BUILD_ROOT \
	libdir=%{_libdir}

install Include/*.h $RPM_BUILD_ROOT%{_includedir}/umfpack

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.txt Doc/{ChangeLog,License}
%attr(755,root,root) %{_libdir}/libumfpack.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libumfpack.so.0

%files devel
%defattr(644,root,root,755)
%doc Doc/{QuickStart,UserGuide}.pdf
%attr(755,root,root) %{_libdir}/libumfpack.so
%{_libdir}/libumfpack.la
%{_includedir}/umfpack

%files static
%defattr(644,root,root,755)
%{_libdir}/libumfpack.a
