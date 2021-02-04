#
# Conditional build:
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	pytest plugin to re-run tests to eliminate flaky failures
Summary(pl.UTF-8):	Wtyczka pytesta do ponownego uruchamiania testów w celu wyeliminowania chwilowych niepowodzeń
Name:		python-pytest-rerunfailures
# NOTE: keep 8.x here for python2/pytest 4.x support
Version:	8.0
Release:	1
License:	MPL v2.0
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/pytest-rerunfailures/
Source0:	https://files.pythonhosted.org/packages/source/p/pytest-rerunfailures/pytest-rerunfailures-%{version}.tar.gz
# Source0-md5:	565b70f1d9f0e3b996724d47fdcbb238
URL:		https://pypi.org/project/pytest-rerunfailures/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-mock
BuildRequires:	python-pytest >= 4.4
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.5
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-pytest >= 4.4
BuildRequires:	python3-pytest < 5.3
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pytest-rerunfailures is a plugin for py.test that re-runs tests to
eliminate intermittent failures.

%description -l pl.UTF-8
pytest-rerunfailures to wtyczka modułu py.test uruchamiająca ponownie
testy, aby wyeliminować chwilowe niepowodzenia.

%package -n python3-pytest-rerunfailures
Summary:	pytest plugin to re-run tests to eliminate flaky failures
Summary(pl.UTF-8):	Wtyczka pytesta do ponownego uruchamiania testów w celu wyeliminowania chwilowych niepowodzeń
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.5

%description -n python3-pytest-rerunfailures
pytest-rerunfailures is a plugin for py.test that re-runs tests to
eliminate intermittent failures.

%description -n python3-pytest-rerunfailures -l pl.UTF-8
pytest-rerunfailures to wtyczka modułu py.test uruchamiająca ponownie
testy, aby wyeliminować chwilowe niepowodzenia.

%prep
%setup -q -n pytest-rerunfailures-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTEST_PLUGINS="pytest_rerunfailures" \
%{__python} -m pytest test_pytest_rerunfailures.py
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTEST_PLUGINS="pytest_rerunfailures" \
%{__python3} -m pytest test_pytest_rerunfailures.py
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc CHANGES.rst LICENSE README.rst
%{py_sitescriptdir}/pytest_rerunfailures.py[co]
%{py_sitescriptdir}/pytest_rerunfailures-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-pytest-rerunfailures
%defattr(644,root,root,755)
%doc CHANGES.rst LICENSE README.rst
%{py3_sitescriptdir}/pytest_rerunfailures.py
%{py3_sitescriptdir}/__pycache__/pytest_rerunfailures.cpython-*.py[co]
%{py3_sitescriptdir}/pytest_rerunfailures-%{version}-py*.egg-info
%endif
