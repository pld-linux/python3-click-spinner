#
# Conditional build:
%bcond_without	tests	# unit tests

Summary:	Spinner for Click
Summary(pl.UTF-8):	Kręciołek dla Clicka
Name:		python3-click-spinner
Version:	0.1.10
Release:	4
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/click-spinner/
Source0:	https://files.pythonhosted.org/packages/source/c/click-spinner/click-spinner-%{version}.tar.gz
# Source0-md5:	ab68ed404401421819c81cc6c0677a87
URL:		https://pypi.org/project/click-spinner/
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools
BuildRequires:	python3-versioneer
%if %{with tests}
BuildRequires:	python3-click
BuildRequires:	python3-pytest
BuildRequires:	python3-six
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sometimes you would just like to show the user some progress, but a
progress bar is not suitable because you don't know how much longer it
would take. In these cases you might want to display a simple spinner.

%description -l pl.UTF-8
Czasami przydałoby się pokazać użytkownikowi jakiś postęp, ale pasek
postępu się nie nadaje, ponieważ nie wiemy, jak długo to jeszcze
potrwa. W takich przypadkach chcielibyśmy wyświetlić prosty kręciołek.

%prep
%setup -q -n click-spinner-%{version}

%{__rm} versioneer.py

%build
%py3_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python3} -m pytest tests
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%{py3_sitescriptdir}/click_spinner
%{py3_sitescriptdir}/click_spinner-%{version}-py*.egg-info
