#global prerelease a3

Name:           python-pivy
Version:        0.6.6
Release:        1
Summary:        Python binding for Coin

License:        ISC
URL:            https://github.com/FreeCAD/pivy

# Move to FreeCAD fork as it is being supported.
Source0:	https://github.com/FreeCAD/pivy/archive/%{version}%{?prerelease:%{prerelease}}.tar.gz

#Patch0:         pivy-cmake.patch
Patch1:         pivy-setup_py.patch

BuildRequires: coin-devel >= 2.4
BuildRequires: soqt-devel
BuildRequires: pkgconfig(python)
BuildRequires: pkgconfig(glu)
BuildRequires: simvoleon-devel
BuildRequires: swig
BuildRequires: cmake ninja
BuildRequires: qt5-qtbase-devel
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
%autosetup -p1 -n pivy-%{version}%{?prerelease:%{prerelease}}

# Examples in the docs folder should not be set executable.
find ./docs -name "*.py" -exec chmod -x {} \;

%cmake -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%if "%{_lib}" != "lib"
mv %{buildroot}%{_prefix}/lib %{buildroot}%{_prefix}/%{_lib}
%endif
 
%files
%license LICENSE
%doc AUTHORS NEWS README.md THANKS docs/* HACKING
%{python_sitearch}/pivy

%files examples
%doc examples
