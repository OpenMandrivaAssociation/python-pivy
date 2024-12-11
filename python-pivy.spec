%{?python_enable_dependency_generator}

Name:		python-pivy
Version:	0.6.9
Release:	1
Summary:	Python binding for Coin
License:	ISC
URL:		https://github.com/coin3d/pivy
Source0:	https://github.com/coin3d/pivy/archive/%{version}/pivy-%{version}.tar.gz
# (fedora)
#Patch0:		pivy-cmake_config.patch

BuildRequires:	cmake ninja
BuildRequires:	cmake(coin)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Core5Compat)
BuildRequires:	cmake(Qt6Quick)
#BuildRequires:	cmake(simvoleon)
BuildRequires:	cmake(pyside6)
BuildRequires:	cmake(simage)
BuildRequires:	cmake(soqt)
BuildRequires:	pkgconfig(python)
BuildRequires:	pkgconfig(glu)
BuildRequires:	swig

Provides: python%pyver}dist(pivy)

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
LDFLAGS="%{build_ldflags} -lm" 
export CC=gcc
export CXX=g++

%cmake -Wno-dev \
	-G Ninja
cd ..
%ninja_build -C build

%install
%ninja_install -C build

