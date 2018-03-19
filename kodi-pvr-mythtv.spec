%global commit 59ff911e0b37a1235962be19ae5fb3010ecdf6eb
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate 20180225

%global kodi_addon pvr.mythtv
%global kodi_version 18.0

Name:           kodi-%(tr "." "-" <<<%{kodi_addon})
# Use Epoch to manage upgrades from older upstream
# (https://github.com/opdenkamp/xbmc-pvr-addons/)
Epoch:          1
Version:        5.7.0
Release:        1%{?dist}
Summary:        MythTV PVR for Kodi

# Some cppmyth private headers are LGPLv2+
License:        GPLv2+ and LGPLv2+
# Switch to main developer's fork for Kodi 18 support until the main
# project is updated
# URL:            https://github.com/kodi-pvr/%%{kodi_addon}/
# Source0:        https://github.com/kodi-pvr/%%{kodi_addon}/archive/%%{shortcommit}/%%{kodi_addon}-%%{shortcommit}.tar.gz
URL:            https://github.com/janbar/%{kodi_addon}/
Source0:        https://github.com/janbar/%{kodi_addon}/archive/%{shortcommit}/%{kodi_addon}-%{shortcommit}.tar.gz
# Use external cppmyth library
Patch0:         %{name}-5.7.0-use_external_cppmyth.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  kodi-devel >= %{kodi_version}
BuildRequires:  kodi-platform-devel >= %{kodi_version}
BuildRequires:  pkgconfig(cppmyth)
BuildRequires:  platform-devel
BuildRequires:  zlib-devel
Requires:       kodi >= %{kodi_version}
ExclusiveArch:  i686 x86_64

%description
%{summary}.


%prep
%autosetup -n %{kodi_addon}-%{commit} -p0

# Drop bundled cppmyth library, except private headers
find lib/cppmyth/ -type f -not -path "lib/cppmyth/src/private/*" -delete


%build
%cmake .
%make_build


%install
%make_install


%files
%doc README.md %{kodi_addon}/changelog.txt
%{_libdir}/kodi/addons/%{kodi_addon}/
%{_datadir}/kodi/addons/%{kodi_addon}/


%changelog
* Fri Mar 16 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1:5.7.0-1
- Update to latest stable release for Kodi 18

* Thu Mar 01 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 1:4.12.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Feb 20 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1:4.12.17-1
- Update to 4.12.17

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 1:4.12.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Apr 24 2017 Mohamed El Morabity <melmorabity@fedorapeople.org> - 1:4.12.14-1
- Update to latest stable release for Kodi 17

* Sun Jul 24 2016 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1:3.4.19-1
- Update to latest stable release for Kodi 16

* Mon Aug 24 2015 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1:2.5.0-1
- Initial RPM release
