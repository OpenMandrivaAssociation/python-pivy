%{?python_enable_dependency_generator}

Name:		python-pivy
Version:	0.6.8
Release:	1
Summary:	Python binding for Coin
License:	ISC
URL:		https://github.com/FreeCAD/pivy
# Move to FreeCAD fork as it is being supported.
Source0:	https://github.com/FreeCAD/pivy/archive/%{version}/pivy-%{version}.tar.gz
# (fedora)
Patch0:		pivy-cmake_config.patch

BuildRequires: cmake ninja
BuildRequires: coin-devel >= 2.4
BuildRequires: pkgconfig(python)
BuildRequires: pkgconfig(glu)
BuildRequires: qt5-qtbase-devel
BuildRequires: simvoleon-devel
BuildRequires: soqt-devel
BuildRequires: swig

Provides: python3dist(pivy)

%description
Pivy is a Coin binding for Python. Coin is a high-level 3D graphics library with\
a C++ Application Programming Interface. Coin uses scene-graph data structures\
to render real-time graphics suitable for mostly all kinds of scientific and\
engineering visualization applications.

%files
%license LICENSE
%doc AUTHORS NEWS README.md THANKS docs/* HACKING
%{python_sitearch}/pivy

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
%cmake -G Ninja
cd ..
%ninja_build -C build

%install
%ninja_install -C build

