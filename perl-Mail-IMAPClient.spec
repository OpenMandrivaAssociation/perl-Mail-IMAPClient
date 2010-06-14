%define upstream_name    Mail-IMAPClient
%define upstream_version 3.25

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	An IMAP Client API
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Mail/%{upstream_name}-%{upstream_version}.tar.gz

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
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
This module provides Perl routines that simplify a sockets connection to and an
IMAP conversation with an IMAP server.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
