%global debug_package %{nil}

Name:           ssh-fingerprints
Version:        0.4
Release:        1%{?dist}
Summary:        Script for printing SSH fingerprints

License:        MIT
URL:            https://github.com/kepi/ssh-fingerprints
Source0:        %{url}/archive/v%{version}.tar.gz

Requires:       openssh

BuildArch:      noarch

%description
Small script to display all used SSH fingerprints for easier verification.

%prep
%autosetup

%install
# bin
mkdir -p %{buildroot}%{_bindir}
install -Dpm 755 -t %{buildroot}%{_bindir} %{name}

%files
%license LICENSE.txt
%doc README.org
%{_bindir}/%{name}

%changelog
* Sat May 11 2024 cyqsimon - 0.4-1
- Release 0.4
