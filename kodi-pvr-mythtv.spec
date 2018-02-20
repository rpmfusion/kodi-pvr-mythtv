%global commit a41fed4cc70cabf1d3b157dca61d7352f2292398
%global short_commit %(c=%{commit}; echo ${c:0:7})
%global commit_date 20170827

%global kodi_addon pvr.mythtv
%global kodi_version 17.0

Name:           kodi-%(tr "." "-" <<<%{kodi_addon})
# Use Epoch to manage upgrades from older upstream
# (https://github.com/opdenkamp/xbmc-pvr-addons/)
Epoch:          1
Version:        4.12.17
Release:        1%{?dist}
Summary:        MythTV PVR for Kodi

Group:          Applications/Multimedia
License:        GPLv2+
URL:            https://github.com/kodi-pvr/%{kodi_addon}/
Source0:        https://github.com/kodi-pvr/%{kodi_addon}/archive/%{short_commit}/%{name}-%{short_commit}.tar.gz
# GPLv2 license file
Source1:        http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt
# Use external cppmyth library
Patch0:         %{name}-4.12.14-use_external_cppmyth.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  kodi-devel >= %{kodi_version}
BuildRequires:  kodi-platform-devel >= %{kodi_version}
BuildRequires:  pkgconfig(cppmyth) >= 2.9.4
BuildRequires:  platform-devel
Requires:       kodi >= %{kodi_version}
ExclusiveArch:  i686 x86_64

%description
Kodi frontend for MythTV (up to MythTV 0.28). Supports streaming of live TV &
recordings, listening to radio channels, EPG and timers.


%prep
%autosetup -n %{kodi_addon}-%{commit} -p0

# Drop bundled cppmyth library, except private headers
find lib/cppmyth/ -type f -not -path "lib/cppmyth/src/private/*" -delete

# Drop bundled zlib library
rm -r depends/common/zlib/

cp -p %{SOURCE1} .


%build
%cmake -DCMAKE_INSTALL_LIBDIR=%{_libdir}/kodi/ .
%make_build


%install
%make_install


%files
%doc %{kodi_addon}/changelog.txt
%license gpl-2.0.txt
%{_libdir}/kodi/addons/%{kodi_addon}/
%{_datadir}/kodi/addons/%{kodi_addon}/


%changelog
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
