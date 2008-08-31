%define module Mail-IMAPClient

Name:		perl-%{module}
Version:	3.10
Release:	%mkrel 1
Summary:	An IMAP Client API
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/Mail/%{module}-%{version}.tar.gz
BuildRequires:	perl(Carp)
BuildRequires:	perl(Errno)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(Fcntl)
BuildRequires:	perl(IO::File)
BuildRequires:	perl(IO::Select)
BuildRequires:	perl(IO::Socket)
BuildRequires:	perl(Parse::RecDescent)
BuildRequires:	perl(Socket)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This module provides Perl routines that simplify a sockets connection to and an
IMAP conversation with an IMAP server.

%prep
%setup -q -n %{module}-%{version}

# fix perl path
find -type f | xargs perl -pi -e "s|/usr/local/bin/perl|%{_bindir}/perl|g"

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor < /dev/null
%make

%check
make test

%install
rm -rf %{buildroot}

%makeinstall_std

# fix permissions
find %{buildroot} -type f -exec chmod 0644 {} \;
find %{buildroot} -type d -exec chmod 0755 {} \;

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYRIGHT README examples
%{perl_vendorlib}/Mail
%{_mandir}/man3/*

