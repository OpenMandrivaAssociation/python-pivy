%global alpha a3

Name:           python-pivy
Version:        0.6.5
Release:        0.5%{?dist}
Summary:        Python binding for Coin

License:        ISC
URL:            https://github.com/FreeCAD/pivy

# Move to FreeCAD fork as it is being supported.
Source0:	https://github.com/FreeCAD/pivy/archive/%{version}%{alpha}.tar.gz

Patch0:         pivy-cmake.patch
Patch1:         pivy-setup_py.patch

BuildRequires: coin4-devel >= 2.4
BuildRequires: soqt-devel
BuildRequires: pkgconfig(python)
BuildRequires: pkgconfig(glu)
BuildRequires: simvoleon-devel
BuildRequires: swig
%{?python_provide:%python_provide python3-pivy}


%global _description\
Pivy is a Coin binding for Python. Coin is a high-level 3D graphics library with\
a C++ Application Programming Interface. Coin uses scene-graph data structures\
to render real-time graphics suitable for mostly all kinds of scientific and\
engineering visualization applications.\

%description %_description

%package examples
Summary: Pivy example files

%description examples
%{summary}

%prep
%autosetup -p1 -n pivy-%{version}%{alpha}

# Examples in the docs folder should not be set executable.
find ./docs -name "*.py" -exec chmod -x {} \;


%build
sed -i -e 's|QtInfo()|QtInfo(qmake_command=["qmake-qt5"])|g' setup.py
export CFLAGS="%{optflags} -fpermissive"
%py3_build


%install
%py3_install

# Fix install location for x86_64 systems.
%if %{_lib} == "lib64"
mv %{buildroot}%{_prefix}/lib %{buildroot}%{_libdir}
%endif

chmod +x %{buildroot}%{python3_sitearch}/pivy/sogui.py

find %{buildroot}%{python3_sitearch} -name "*.py" -exec sed -i "s|#!/usr/bin/env python|#!%{__python3}|" {} \;
 
%files
%license LICENSE
%doc AUTHORS NEWS README.md THANKS docs/* HACKING
%{python_sitearch}/pivy/
%{python_sitearch}/*.egg-info

%files examples
%doc examples
