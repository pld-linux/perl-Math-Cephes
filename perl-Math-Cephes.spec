#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Math
%define	pnam	Cephes
Summary:	Math::Cephes - Perl interface to the cephes math library
Summary(pl):	Math::Cephes - interfejs perlowy do biblioteki matematycznej cephes
Name:		perl-Math-Cephes
Version:	0.36
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	e4930ead1c799c96fe01e2ddf89db6b1
Patch0:		%{name}-glibc.patch
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
# it's too x86-centric about fp internals
ExclusiveArch:	%{ix86} amd64 ppc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides an interface to over 150 functions of the cephes
math library of Stephen Moshier.

%description -l pl
Ten modu³ dostarcza interfejs do ponad 150 funkcji z biblioteki
matematycznej cephes autorstwa Stephena Moshiera.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%attr(755,root,root) %{_bindir}/pmath
%{perl_vendorarch}/Math/Cephes.pm
%{perl_vendorarch}/Math/Cephes
%dir %{perl_vendorarch}/auto/Math/Cephes
%{perl_vendorarch}/auto/Math/Cephes/Cephes.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Math/Cephes/Cephes.so
%{_mandir}/man[13]/*
