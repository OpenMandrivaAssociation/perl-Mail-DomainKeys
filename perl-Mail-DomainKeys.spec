%define module Mail-DomainKeys

Summary:	Perl module that implements DomainKeys
Name:		perl-%{module}
Version:	1.0
Release:	9
License:	Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/Mail-DomainKeys/
Source0:	http://www.cpan.org/modules/by-module/Mail/%{module}-%{version}.tar.gz
BuildRequires:	perl-devel
BuildRequires:	perl(Crypt::OpenSSL::RSA)
BuildRequires:	perl(Mail::Address)
BuildRequires:	perl(MIME::Base64)
BuildRequires:	perl(Net::DNS) => 0.34,
BuildRequires:	perl(Test::More)
BuildArch:	noarch

%description
Mail-DomainKeys is a Perl module that implements DomainKeys.

%prep
%setup -q -n %{module}-%{version}

%build
echo "y" | %__perl Makefile.PL INSTALLDIRS="vendor"
%make

%check
make test

%install
%makeinstall_std

%files
%defattr(-,root,root,0755)
%doc Changes README THANKS
%dir %{perl_vendorlib}/Mail/DomainKeys
%dir %{perl_vendorlib}/Mail/DomainKeys/Key
%{perl_vendorlib}/Mail/DomainKeys/*.pm
%{perl_vendorlib}/Mail/DomainKeys/Key/*.pm
%{perl_vendorlib}/Mail/DomainKeys.pm
%{_mandir}/man3/Mail::DomainKeys.3pm*



%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1.0-6mdv2012.0
+ Revision: 765398
- rebuilt for perl-5.14.2
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0-4
+ Revision: 667249
- mass rebuild

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.0-3mdv2011.0
+ Revision: 426520
- rebuild

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 1.0-2mdv2009.1
+ Revision: 351899
- rebuild

* Tue Jul 08 2008 Oden Eriksson <oeriksson@mandriva.com> 1.0-1mdv2009.0
+ Revision: 232761
- fix deps
- import perl-Mail-DomainKeys


* Tue Jul 08 2008 Oden Eriksson <oeriksson@mandriva.com> 1.0-1mdv2009.0
- initial Mandriva package 
