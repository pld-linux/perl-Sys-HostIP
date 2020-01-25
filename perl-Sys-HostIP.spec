#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	Sys
%define	pnam	HostIP
Summary:	Sys::HostIP - Try extra hard to get ip address related info
#Summary(pl.UTF-8):	
Name:		perl-Sys-HostIP
Version:	1.3.1
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Sys/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	71793ea0f880b126be92fdaa0ccfef83
URL:		http://search.cpan.org/dist/Sys-HostIP/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	/sbin/ifconfig
%endif
Requires:	/sbin/ifconfig
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sys::HostIP does what it can to determine the ip address of your
machine. All 3 methods work fine on every system that I've been able to test
on. (Irix, OpenBSD, FreeBSD, NetBSD, Solaris, Linux, OSX, Win32, Cygwin). It 
does this by parsing ifconfig(8) (ipconfig on Win32/Cygwin) output. 

# %description -l pl.UTF-8
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Sys/*.pm
%{_mandir}/man3/*
