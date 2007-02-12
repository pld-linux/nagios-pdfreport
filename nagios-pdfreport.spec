# TODO:
# - fix paths in report.cgi
# - add link to report.cgi on Nagios page
#
# Conditional build:
%bcond_without	autodeps	# don't BR packages needed only for resolving deps
#
%include	/usr/lib/rpm/macros.perl
Summary:	Creating PDF or HTML summary availability reports
Summary(pl.UTF-8):   Tworzenie raportów PDF lub HTML podsumowujących dostępność
Name:		nagios-pdfreport
Version:	1.0
Release:	0.1
License:	GPL
Group:		Applications/System
# from http://www.nagiosexchange.org/Frontends.37.0.html?&tx_netnagext_pi1[p_view]=220
Source0:	pdfreport-%{version}.tzr
# Source0-md5:	efb802233a0a56671c02f053f0f99376
URL:		http://www.nagiosexchange.org/Frontends.37.0.html?&tx_netnagext_pi1[p_view]=220
%{?with_autodeps:BuildRequires:	perl-Nagios-Object}
BuildRequires:	rpm-perlprov
Requires:	htmldoc
Requires:	nagios-cgi
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_plugindir	%{_libdir}/nagios/grapher

%description
Creating PDF or HTML summary availability reports.

%description -l pl.UTF-8
Tworzenie raportów PDF lub HTML podsumowujących dostępność.

%prep
%setup -q -n pdfreport-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir}/nagios/cgi,%{perl_vendorlib}/Nagios}

install report.cgi $RPM_BUILD_ROOT%{_libdir}/nagios/cgi
install ActivityLog.pm $RPM_BUILD_ROOT%{perl_vendorlib}/Nagios

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_libdir}/nagios/cgi/report.cgi
%{perl_vendorlib}/Nagios/ActivityLog.pm
