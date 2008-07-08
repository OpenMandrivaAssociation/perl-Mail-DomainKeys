%define module Mail-DomainKeys

Summary:	Perl module that implements DomainKeys
Name:		perl-%{module}
Version:	1.0
Release:	%mkrel 1
License:	Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/Mail-DomainKeys/
Source0:	http://www.cpan.org/modules/by-module/Mail/%{module}-%{version}.tar.gz
BuildRequires:	perl
BuildRequires:	perl(Crypt::OpenSSL::RSA)
BuildRequires:	perl(Mail::Address)
BuildRequires:	perl(MIME::Base64)
BuildRequires:	perl(Net::DNS) => 0.34,
BuildRequires:	perl(Test::More)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Mail-DomainKeys is a Perl module that implements DomainKeys.

%prep

%setup -q -n %{module}-%{version}

%build
echo "y" | %{__perl} Makefile.PL INSTALLDIRS="vendor"

%make

%check
make test

%install
rm -rf %{buildroot}

%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,0755)
%doc Changes README THANKS
%dir %{perl_vendorlib}/Mail/DomainKeys
%dir %{perl_vendorlib}/Mail/DomainKeys/Key
%{perl_vendorlib}/Mail/DomainKeys/*.pm
%{perl_vendorlib}/Mail/DomainKeys/Key/*.pm
%{perl_vendorlib}/Mail/DomainKeys.pm
%{_mandir}/man3/Mail::DomainKeys.3pm*

