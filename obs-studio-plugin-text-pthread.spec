%global srcname obs-text-pthread

Name:           obs-studio-plugin-text-pthread
Version:        2.0.2
Release:        1%{?dist}
Summary:        OBS text display plugin with many advanced features

License:        GPL-2.0-or-later
URL:            https://github.com/norihiro/obs-text-pthread
Source0:        %{url}/archive/refs/tags/%{version}/%{srcname}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  g++

BuildRequires:  pkgconfig(libobs)
BuildRequires:  pkgconfig(pango)

Supplements:    obs-studio%{?_isa}

%description
This OBS plugin aims to show beautiful text on OBS Studio
using pango, adding features like Markup, Transitions and others.

%prep
%autosetup -n %{srcname}-%{version}
%cmake \
    -D CMAKE_INSTALL_LIBDIR=/usr/lib64/ \
    -D CMAKE_INSTALL_PREFIX=/usr \
    -D LINUX_PORTABLE=OFF \
    -DCMAKE_SKIP_RPATH:BOOL=ON

%build
%cmake_build


%install
%cmake_install


%files
%license LICENSE
%{_libdir}/obs-plugins/%{srcname}*
%{_datadir}/obs/obs-plugins/%{srcname}/


%changelog
* Sat Aug 12 2023 Diego Herrera <dherrera@redhat.com> - 2.0.2-1
- First commit
