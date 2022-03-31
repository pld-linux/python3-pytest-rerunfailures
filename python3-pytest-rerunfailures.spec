#
# Conditional build:
%bcond_without	tests	# unit tests

Summary:	pytest plugin to re-run tests to eliminate flaky failures
Summary(pl.UTF-8):	Wtyczka pytesta do ponownego uruchamiania testów w celu wyeliminowania chwilowych niepowodzeń
Name:		python3-pytest-rerunfailures
Version:	10.2
Release:	2
License:	MPL v2.0
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/pytest-rerunfailures/
Source0:	https://files.pythonhosted.org/packages/source/p/pytest-rerunfailures/pytest-rerunfailures-%{version}.tar.gz
# Source0-md5:	5af973c439ba57da6dd8991859bf497d
URL:		https://pypi.org/project/pytest-rerunfailures/
BuildRequires:	python3-modules >= 1:3.6
BuildRequires:	python3-setuptools >= 1:40.0
%if %{with tests}
BuildRequires:	python3-pytest >= 5.3
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pytest-rerunfailures is a plugin for py.test that re-runs tests to
eliminate intermittent failures.

%description -l pl.UTF-8
pytest-rerunfailures to wtyczka modułu py.test uruchamiająca ponownie
testy, aby wyeliminować chwilowe niepowodzenia.

%prep
%setup -q -n pytest-rerunfailures-%{version}

%build
%py3_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTEST_PLUGINS="pytest_rerunfailures" \
%{__python3} -m pytest test_pytest_rerunfailures.py
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.rst LICENSE README.rst
%{py3_sitescriptdir}/pytest_rerunfailures.py
%{py3_sitescriptdir}/__pycache__/pytest_rerunfailures.cpython-*.py[co]
%{py3_sitescriptdir}/pytest_rerunfailures-%{version}-py*.egg-info
