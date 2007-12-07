Summary:	UMFPACK: sparse multifrontal LU factorization
Name:		UMFPACK
Version:	5.2.0
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://www.cise.ufl.edu/research/sparse/umfpack/%{name}-%{version}.tar.gz
# Source0-md5:	8ad2d68c7c49dfcdd8321e806e6c611c
Patch0:		%{name}-ufconfig.patch
Patch1:		%{name}-shared.patch
URL:		http://www.cise.ufl.edu/research/sparse/umfpack/
BuildRequires:	UFconfig
BuildRequires:	AMD-devel
BuildRequires:	blas-devel
BuildRequires:	libtool >= 2:1.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
UMFPACK is a set of routines for solving unsymmetric sparse
linear systems, Ax=b, using the Unsymmetric MultiFrontal method.
Written in ANSI/ISO C, with a MATLAB (Version 6.0 and later)
interface. Appears as a built-in routine (for lu, backslash,
and forward slash) in MATLAB. Includes a MATLAB interface,
a C-callable interface, and a Fortran-callable interface.
Note that "UMFPACK" is pronounced in two syllables, "Umph Pack".
It is not "You Em Ef Pack".

%package devel
Summary:	Header files for umfpack library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki umfpack
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	UFconfig

%description devel
Header files for umfpack library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki umfpack.

%package static
Summary:	Static umfpack library
Summary(pl.UTF-8):	Statyczna biblioteka umfpack
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static umfpack library.

%description static -l pl.UTF-8
Statyczna biblioteka umfpack.

%prep
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -fPIC" \
	libdir=%{_libdir}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_includedir}

%{__make} -C Lib install \
	DESTDIR=$RPM_BUILD_ROOT \
	libdir=%{_libdir}

install Include/* $RPM_BUILD_ROOT%{_includedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.txt
%attr(755,root,root) %{_libdir}/libumfpack.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libumfpack.so
%{_libdir}/libumfpack.la
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/libumfpack.a
