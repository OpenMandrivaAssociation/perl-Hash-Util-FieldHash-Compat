%define upstream_name    Hash-Util-FieldHash-Compat
%define upstream_version 0.03

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    Emulate Hash::Util::FieldHash using
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Hash/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Test::use::ok)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
Under older perls this module provides a drop in compatible api to the
Hash::Util::FieldHash manpage using the perltie manpage. When the
Hash::Util::FieldHash manpage is available it will use that instead.

This way code requiring field hashes can benefit from fast, robust field
hashes on Perl 5.10 and newer, but still run on older perls that don't ship
with that module.

See the Hash::Util::FieldHash manpage for all the details of the API.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%{make}

%check
%{make} test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)

%{_mandir}/man3/*
%perl_vendorlib/*


