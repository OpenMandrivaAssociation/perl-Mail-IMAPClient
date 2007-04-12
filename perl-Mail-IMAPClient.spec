%define real_name Mail-IMAPClient

Summary:	Mail::IMAPClient - an IMAP Client API
Name:		perl-%{real_name}
Version:	2.2.9
Release:	%mkrel 3
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{real_name}
Source0:	http://search.cpan.org/CPAN/authors/id/D/DJ/DJKERNEN/%{real_name}-%{version}.tar.bz2
Patch0:		Mail-IMAPClient-2.2.9-imapsync-1.182.diff
BuildRequires:	perl-devel
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
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This module provides Perl routines that simplify a sockets connection to and an
IMAP conversation with an IMAP server.

%prep

%setup -q -n %{real_name}-%{version}
%patch0 -p0

# fix perl path
find -type f | xargs perl -pi -e "s|/usr/local/bin/perl|%{_bindir}/perl|g"

%build
yes n | %{__perl} Makefile.PL INSTALLDIRS=vendor

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
%doc Artistic Copying COPYRIGHT README Todo docs examples
%dir %{perl_vendorlib}/Mail/IMAPClient
%{perl_vendorlib}/Mail/IMAPClient/*
%{perl_vendorlib}/Mail/IMAPClient.pm
%{perl_vendorlib}/Mail/IMAPClient.pod
%{_mandir}/man3/*

