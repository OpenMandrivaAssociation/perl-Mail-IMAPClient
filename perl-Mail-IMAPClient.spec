%define modname	Mail-IMAPClient
%define modver 3.39

# We never had it and unlikely really need
%if %{_use_internal_dependency_generator}
%define __noautoreq 'perl\\(Mozilla::LDAP::Conn\\)'
%endif

Summary:	An IMAP Client API
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	1
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/Mail/Mail-IMAPClient-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Carp)
BuildRequires:	perl(Errno)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(Fcntl)
BuildRequires:	perl(IO::File)
BuildRequires:	perl(IO::Select)
BuildRequires:	perl(IO::Socket)
BuildRequires:	perl(Parse::RecDescent)
BuildRequires:	perl(Socket)
BuildRequires:	perl-devel

%description
This module provides Perl routines that simplify a sockets connection to and an
IMAP conversation with an IMAP server.

%prep
%setup -qn %{modname}-%{modver}

# fix perl path
find -type f | xargs perl -pi -e "s|/usr/local/bin/perl|%{_bindir}/perl|g"

%build
%__perl Makefile.PL INSTALLDIRS=vendor < /dev/null
%make

%check
make test

%install
%makeinstall_std
# fix permissions
find %{buildroot} -type f -exec chmod 0644 {} \;
find %{buildroot} -type d -exec chmod 0755 {} \;

%files
%doc README examples
%{perl_vendorlib}/Mail
%{_mandir}/man3/*



