%define upstream_name    Hash-Util-FieldHash-Compat
%define upstream_version 0.07

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Emulate Hash::Util::FieldHash using
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Hash/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Test::use::ok)
BuildArch:	noarch

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
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 16 2011 Funda Wang <fwang@mandriva.org> 0.30.0-2mdv2011.0
+ Revision: 653597
- rebuild for updated spec-helper

* Wed Jul 28 2010 Shlomi Fish <shlomif@mandriva.org> 0.30.0-1mdv2011.0
+ Revision: 562748
- import perl-Hash-Util-FieldHash-Compat


* Fri Feb 05 2010 cpan2dist 0.03-1mdv
- initial mdv release, generated with cpan2dist



