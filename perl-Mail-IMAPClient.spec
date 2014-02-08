%define upstream_name    Mail-IMAPClient
%define upstream_version 3.28

# We never had it and unlikely really need
%if %{_use_internal_dependency_generator}
%define __noautoreq 'perl\\(Mozilla::LDAP::Conn\\)'
%endif

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	6

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
BuildRequires:	perl-devel
BuildArch:	noarch

%description
This module provides Perl routines that simplify a sockets connection to and an
IMAP conversation with an IMAP server.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 3.280.0-4mdv2012.0
+ Revision: 765399
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 3.280.0-3
+ Revision: 763914
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 3.280.0-2
+ Revision: 667250
- mass rebuild

* Thu Mar 10 2011 Guillaume Rousse <guillomovitch@mandriva.org> 3.280.0-1
+ Revision: 643401
- update to new version 3.28

* Mon Feb 28 2011 Funda Wang <fwang@mandriva.org> 3.270.0-2
+ Revision: 640745
- rebuild to obsolete old packages

* Fri Feb 18 2011 Guillaume Rousse <guillomovitch@mandriva.org> 3.270.0-1
+ Revision: 638486
- update to new version 3.27

* Sat Feb 05 2011 Guillaume Rousse <guillomovitch@mandriva.org> 3.260.0-1
+ Revision: 636171
- new version

* Mon Jun 14 2010 Jérôme Quelin <jquelin@mandriva.org> 3.250.0-1mdv2010.1
+ Revision: 548021
- update to 3.25

* Fri Feb 05 2010 Jérôme Quelin <jquelin@mandriva.org> 3.230.0-1mdv2010.1
+ Revision: 501145
- update to 3.23

* Fri Jan 22 2010 Jérôme Quelin <jquelin@mandriva.org> 3.220.0-1mdv2010.1
+ Revision: 494932
- update to 3.22

* Thu Sep 24 2009 Jérôme Quelin <jquelin@mandriva.org> 3.210.0-1mdv2010.0
+ Revision: 448125
- update to 3.21

* Mon Aug 24 2009 Jérôme Quelin <jquelin@mandriva.org> 3.200.0-1mdv2010.0
+ Revision: 420271
- update to 3.20

* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 3.190.0-1mdv2010.0
+ Revision: 403842
- rebuild using %%perl_convert_version

* Sun Jun 21 2009 Guillaume Rousse <guillomovitch@mandriva.org> 3.19-1mdv2010.0
+ Revision: 387762
- update to new version 3.19

* Sun Jun 07 2009 Guillaume Rousse <guillomovitch@mandriva.org> 3.18-1mdv2010.0
+ Revision: 383529
- update to new version 3.18

* Fri May 22 2009 Guillaume Rousse <guillomovitch@mandriva.org> 3.17-1mdv2010.0
+ Revision: 378749
- update to new version 3.17

* Sat May 02 2009 Guillaume Rousse <guillomovitch@mandriva.org> 3.16-1mdv2010.0
+ Revision: 370490
- update to new version 3.16

* Tue Feb 17 2009 Guillaume Rousse <guillomovitch@mandriva.org> 3.14-1mdv2009.1
+ Revision: 341224
- update to new version 3.14

* Fri Jan 16 2009 Guillaume Rousse <guillomovitch@mandriva.org> 3.13-1mdv2009.1
+ Revision: 330197
- update to new version 3.13

* Tue Nov 25 2008 Guillaume Rousse <guillomovitch@mandriva.org> 3.12-1mdv2009.1
+ Revision: 306649
- update to new version 3.12

* Sat Oct 11 2008 Guillaume Rousse <guillomovitch@mandriva.org> 3.11-1mdv2009.1
+ Revision: 292218
- update to new version 3.11

* Sun Aug 31 2008 Guillaume Rousse <guillomovitch@mandriva.org> 3.10-1mdv2009.0
+ Revision: 277953
- update to new version 3.10

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 3.08-2mdv2009.0
+ Revision: 265413
- rebuild early 2009.0 package (before pixel changes)

* Sat Jun 07 2008 Guillaume Rousse <guillomovitch@mandriva.org> 3.08-1mdv2009.0
+ Revision: 216635
- new version

* Tue May 06 2008 Guillaume Rousse <guillomovitch@mandriva.org> 3.07-1mdv2009.0
+ Revision: 202293
- update to new version 3.07

* Tue Apr 15 2008 Guillaume Rousse <guillomovitch@mandriva.org> 3.06-1mdv2009.0
+ Revision: 193856
- update to new version 3.06

* Thu Feb 21 2008 Guillaume Rousse <guillomovitch@mandriva.org> 3.05-1mdv2008.1
+ Revision: 173534
- update to new version 3.05

* Sun Jan 27 2008 Guillaume Rousse <guillomovitch@mandriva.org> 3.04-1mdv2008.1
+ Revision: 158624
- update to new version 3.04

* Tue Jan 15 2008 Guillaume Rousse <guillomovitch@mandriva.org> 3.03-1mdv2008.1
+ Revision: 152913
- update to new version 3.03
- update to new version 3.03

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Dec 06 2007 Guillaume Rousse <guillomovitch@mandriva.org> 3.02-1mdv2008.1
+ Revision: 115862
- update to new version 3.02

* Thu Nov 29 2007 Guillaume Rousse <guillomovitch@mandriva.org> 3.00-1mdv2008.1
+ Revision: 113873
- new version
  drop imapsync patch, seems to be uneeded anymore (to confirm)
  spec cleanup


* Fri Oct 06 2006 Oden Eriksson <oeriksson@mandriva.com> 2.2.9-3mdv2007.0
- added a patch from imapsync-1.182 (P0)

* Fri Oct 06 2006 Oden Eriksson <oeriksson@mandriva.com> 2.2.9-2mdv2007.0
- rebuild

* Sat Jul 09 2005 Andreas Hasenack <andreas@mandriva.com> 2.2.9-1mdk
- packaged for Mandriva

