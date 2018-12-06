# Run tests in check section
# Some tests fail on s390 and aarch
%bcond_with check

%global goipath         github.com/shirou/gopsutil
Version:                2.18.05

%global common_description %{expand:
Psutil for golang.}

%gometa

Name:    %{goname}
Release: 2%{?dist}
Summary: Psutil for golang
License: BSD
URL:     %{gourl}
Source:  %{gosource}

BuildRequires: golang(golang.org/x/sys/unix)
BuildRequires: golang(golang.org/x/sys/windows)

%if %{with check}
BuildRequires: golang(github.com/stretchr/testify)
%endif

%description
%{common_description}


%package    devel
Summary:    %{summary}
 
%description devel
%{common_description}
 
This package contains the source code needed for building packages that import
the %{goipath} Go namespace.


%prep
%forgeautosetup


%install
%goinstall


%if %{with check}
%check
%gochecks
%endif


%files devel -f devel.file-list
%license LICENSE
%doc README.rst


%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.18.05-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Robert-André Mauchin <zebob.m@gmail.com> - 2.18.05-1
- Bump to 2.18.05

* Wed May 02 2018 Robert-André Mauchin <zebob.m@gmail.com> - 2.18.04-1
- First package for Fedora

