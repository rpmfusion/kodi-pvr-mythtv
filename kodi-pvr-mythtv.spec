%global kodi_addon pvr.mythtv
%global kodi_version 19.0
%global kodi_codename Matrix

Name:           kodi-%(tr "." "-" <<<%{kodi_addon})
# Use Epoch to manage upgrades from older upstream
# (https://github.com/opdenkamp/xbmc-pvr-addons/)
Epoch:          1
Version:        7.3.1
Release:        1%{?dist}
Summary:        MythTV PVR for Kodi

# Some cppmyth private headers are LGPLv2+
License:        GPLv2+ and LGPLv2+
URL:            https://github.com/janbar/%{kodi_addon}/
Source0:        %{url}/archive/%{version}-%{kodi_codename}/%{kodi_addon}-%{version}.tar.gz
# Use external cppmyth library
Patch0:         %{name}-7.0.5-use_external_cppmyth.patch

BuildRequires:  cmake3
BuildRequires:  gcc-c++
BuildRequires:  kodi-devel >= %{kodi_version}
BuildRequires:  pkgconfig(cppmyth) >= 2.14.1
BuildRequires:  pkgconfig(zlib)
Requires:       kodi >= %{kodi_version}
ExcludeArch:    %{power64} ppc64le

%description
%{summary}.


%prep
%autosetup -n %{kodi_addon}-%{version}-%{kodi_codename} -p0

# Drop bundled cppmyth library, except private headers
find lib/cppmyth/ -type f -not -path "lib/cppmyth/src/private/*" -delete


%build
%cmake3
%cmake3_build


%install
%cmake3_install


%files
%doc README.md %{kodi_addon}/changelog.txt
%license LICENSE.md
%{_libdir}/kodi/addons/%{kodi_addon}/
%{_datadir}/kodi/addons/%{kodi_addon}/


%changelog
* Sun Jul 11 2021 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1:7.3.1-1
- Update to 7.3.1

* Fri Jan 29 2021 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1:7.3.0-1
- Update to 7.3.0

* Mon Nov 30 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1:7.2.0-1
- Update to 7.2.0

* Mon Nov 16 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1:7.1.1-1
- Update to 7.1.1

* Thu Aug 20 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1:7.0.5-1
- Update to 7.0.5 (switch to Matrix branch)

* Tue Aug 18 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1:5.10.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Feb 04 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1:5.10.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 13 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1:5.10.15-1
- Update to 5.10.15

* Fri Aug 09 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1:5.10.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jul 27 2019 Leigh Scott <leigh123linux@googlemail.com> - 1:5.10.7-1
- Update to 5.10.7 (rfbz #5304)

* Mon Mar 04 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1:5.10.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Dec 23 2018 Leigh Scott <leigh123linux@googlemail.com> - 1:5.10.2-1
- Update to 5.10.2 (rfbz #5121)

* Mon Oct 15 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1:5.8.6-2
- Enable arm build

* Sat Sep 01 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1:5.8.6-1
- Update to 5.8.6
- Enable aarch64 build

* Thu Jul 26 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1:5.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

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
