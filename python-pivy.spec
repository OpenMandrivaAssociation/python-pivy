Name:		python-pivy
Version:	0.6.10
Release:	2
Summary:	Python binding for Coin
License:	ISC
URL:		https://github.com/coin3d/pivy
Source0:	https://github.com/coin3d/pivy/archive/%{version}/pivy-%{version}.tar.gz

BuildRequires:	cmake ninja
BuildRequires:	cmake(coin)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Quick)
#BuildRequires:	cmake(simvoleon)
BuildRequires:	cmake(pyside6)
BuildRequires:	cmake(simage)
BuildRequires:	cmake(soqt)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(python)
BuildRequires:  python%{pyver}dist(pip)
BuildRequires:  python%{pyver}dist(setuptools)
BuildRequires:	swig


%description
Pivy is a Coin binding for Python. Coin is a high-level 3D graphics library with\
a C++ Application Programming Interface. Coin uses scene-graph data structures\
to render real-time graphics suitable for mostly all kinds of scientific and\
engineering visualization applications.

%files
%license LICENSE
%doc AUTHORS NEWS README.md THANKS docs/* HACKING
%{python_sitearch}/pivy
%{python_sitearch}/Pivy-*.*-info/

#-----------------------------------------------------------------------------

%package examples
Summary: Pivy example files

%description examples
Pivy is a Coin binding for Python. Coin is a high-level 3D graphics library with\
a C++ Application Programming Interface. Coin uses scene-graph data structures\
to render real-time graphics suitable for mostly all kinds of scientific and\
engineering visualization applications.

%files examples
%doc examples

#-----------------------------------------------------------------------------

%prep
%autosetup -p1 -n pivy-%{version}

# Examples in the docs folder should not be set executable.
find ./docs -name "*.py" -exec chmod -x {} \;

%build
%cmake -Wno-dev \
	-DPIVY_USE_QT6:BOOL=ON \
	-G Ninja
%ninja_build

%install
%ninja_install -C build

# egg-info
%{py_install}
mv -f %{buildroot}/%{py_puresitedir}/Pivy-*.*-info/ %{buildroot}/%{py_platsitedir}/

