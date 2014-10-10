%define module Mail-DomainKeys

Summary:	Perl module that implements DomainKeys
Name:		perl-%{module}
Version:	1.0
Release:	15
License:	Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/Mail-DomainKeys/
Source0:	http://www.cpan.org/modules/by-module/Mail/%{module}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	perl-devel
BuildRequires:	perl(Crypt::OpenSSL::RSA)
BuildRequires:	perl(Mail::Address)
BuildRequires:	perl(MIME::Base64)
BuildRequires:	perl(Net::DNS) => 0.34,
BuildRequires:	perl(Test::More)

%description
Mail-DomainKeys is a Perl module that implements DomainKeys.

%prep
%setup -qn %{module}-%{version}

%build
echo "y" | %__perl Makefile.PL INSTALLDIRS="vendor"
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README THANKS
%dir %{perl_vendorlib}/Mail/DomainKeys
%dir %{perl_vendorlib}/Mail/DomainKeys/Key
%{perl_vendorlib}/Mail/DomainKeys/*.pm
%{perl_vendorlib}/Mail/DomainKeys/Key/*.pm
%{perl_vendorlib}/Mail/DomainKeys.pm
%{_mandir}/man3/Mail::DomainKeys.3pm*

