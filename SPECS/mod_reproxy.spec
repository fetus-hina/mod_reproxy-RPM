Summary: x-reproxy-url header support to Apache/2.x.
Name: mod_reproxy
Version: 0.02
Release: 1%{?dist}
Group: System Environment/Daemons
License: Unknown
URL: https://github.com/kazuho/mod_reproxy

Packager: HiNa <hina@jp3cki.jp>

Source0: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: apr-devel, httpd-devel
Requires: httpd

%description
This module adds x-reproxy-url header support to Apache/2.x.

%prep
%setup

%{__cat} <<EOF >mod_reproxy.conf
LoadModule reproxy_module modules/mod_reproxy.so
EOF

%build
%{_sbindir}/apxs -a -c -Wc,-Wall -Wc,-g -Wc,-O2 mod_reproxy.c

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 .libs/mod_reproxy.so %{buildroot}%{_libdir}/httpd/modules/mod_reproxy.so
%{__install} -Dp -m0644 mod_reproxy.conf %{buildroot}%{_sysconfdir}/httpd/conf.d/mod_reproxy.conf
%{__install} -Dp -m0644 README  %{buildroot}%{_defaultdocdir}/%{name}-%{version}/README

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%config(noreplace) %{_defaultdocdir}/%{name}-%{version}/README
%config(noreplace) %{_sysconfdir}/httpd/conf.d/mod_reproxy.conf
%{_libdir}/httpd/modules/mod_reproxy.so

%changelog
* Fri Apr 27 2012 HiNa <hina@jp3cki.jp> - 0.02
- Initial package.
