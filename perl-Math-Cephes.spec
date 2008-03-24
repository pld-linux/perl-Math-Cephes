#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Math
%define		pnam	Cephes
Summary:	Math::Cephes - Perl interface to the cephes math library
Summary(pl.UTF-8):	Math::Cephes - interfejs perlowy do biblioteki matematycznej cephes
Name:		perl-Math-Cephes
Version:	0.43
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Math/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	82df7759b5b1c7dc49a79fc616847168
URL:		http://search.cpan.org/dist/Math-Cephes/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
# it's too x86-centric about fp internals
ExclusiveArch:	%{ix86} %{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides an interface to over 150 functions of the cephes
math library of Stephen Moshier.

%description -l pl.UTF-8
Ten moduł dostarcza interfejs do ponad 150 funkcji z biblioteki
matematycznej cephes autorstwa Stephena Moshiera.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make} \
	CC="%{__cc}" \
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
