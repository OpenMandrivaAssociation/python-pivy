
%define module pivy

Summary: A Python binding for Coin
Name: python-%{module}
Version: 0.4.0
Release: %mkrel 0.20070826.3
Source0: http://pivy.coin3d.org/download/snapshot/releases/daily/Pivy-latest.tar.gz
License: BSD
Group: Development/Python
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Url: http://pivy.tammura.at/
BuildRequires: coin-devel >= 2.4
BuildRequires: libsoqt-devel
BuildRequires: python-devel
BuildRequires: simvoleon-devel
BuildRequires: swig

%description
Pivy is a Coin binding for Python. Coin is a high-level 3D graphics
library with a C++ Application Programming Interface. Coin uses
scene-graph data structures to render real-time graphics suitable for
mostly all kinds of scientific and engineering visualization
applications.


%package gui-soqt
Summary: A Python binding for SoQt
Group: Development/Python

%description gui-soqt
Pivy is a Coin binding for Python. Coin is a high-level 3D graphics
library with a C++ Application Programming Interface. Coin uses
scene-graph data structures to render real-time graphics suitable for
mostly all kinds of scientific and engineering visualization
applications.


%prep
%setup -n Pivy

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install --skip-build --root=$RPM_BUILD_ROOT
%if "%{_lib}" == "lib64"
mv $RPM_BUILD_ROOT%{_prefix}/lib $RPM_BUILD_ROOT%{_libdir}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{py_platsitedir}/pivy
%exclude %{py_platsitedir}/pivy/gui/*qt*
%doc examples

%files gui-soqt
%{py_platsitedir}/pivy/gui/*qt*
%{py_platsitedir}/Pivy*.egg-info
