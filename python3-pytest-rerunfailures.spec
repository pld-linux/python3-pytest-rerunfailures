#
# Conditional build:
%bcond_without	tests	# unit tests

Summary:	pytest plugin to re-run tests to eliminate flaky failures
Summary(pl.UTF-8):	Wtyczka pytesta do ponownego uruchamiania testów w celu wyeliminowania chwilowych niepowodzeń
Name:		python3-pytest-rerunfailures
Version:	16.7
Release:	1
License:	MPL v2.0
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/pytest-rerunfailures/
Source0:	https://files.pythonhosted.org/packages/source/p/pytest-rerunfailures/pytest_rerunfailures-%{version}.tar.gz
# Source0-md5:	b3117a456d80c6af097b37586637042e
URL:		https://pypi.org/project/pytest-rerunfailures/
BuildRequires:	python3-build
BuildRequires:	python3-installer
BuildRequires:	python3-modules >= 1:3.10
BuildRequires:	python3-setuptools >= 1:61
%if %{with tests}
BuildRequires:	python3-packaging >= 17.1
BuildRequires:	python3-pytest >= 8.2
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 2.044
Requires:	python3-modules >= 1:3.10
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pytest-rerunfailures is a plugin for py.test that re-runs tests to
eliminate intermittent failures.

%description -l pl.UTF-8
pytest-rerunfailures to wtyczka modułu py.test uruchamiająca ponownie
testy, aby wyeliminować chwilowe niepowodzenia.

%prep
%setup -q -n pytest_rerunfailures-%{version}

%build
%py3_build_pyproject

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTEST_PLUGINS="pytest_rerunfailures" \
PYTHONPATH=$(pwd)/src \
%{__python3} -m pytest tests/test_pytest_rerunfailures.py
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.rst LICENSE README.rst
%{py3_sitescriptdir}/pytest_rerunfailures.py
%{py3_sitescriptdir}/__pycache__/pytest_rerunfailures.cpython-*.py[co]
%{py3_sitescriptdir}/pytest_rerunfailures-%{version}.dist-info
