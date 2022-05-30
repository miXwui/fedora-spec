Name:           power-profiles-daemon
Version:        0.11.1
Release:        1%{?dist}
Summary:        Makes power profiles handling available over D-Bus

License:        GPLv3+
URL:            https://gitlab.freedesktop.org/hadess/power-profiles-daemon
Source0:        https://gitlab.freedesktop.org/hadess/power-profiles-daemon/uploads/f81e7fa231b3cb45dba87c85375aeaa2/power-profiles-daemon-0.11.1.tar.xz

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  gtk-doc
BuildRequires:  pkgconfig(udev)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(upower-glib)
BuildRequires:  pkgconfig(polkit-gobject-1)
BuildRequires:  systemd
BuildRequires:  umockdev
BuildRequires:  python3-dbusmock
BuildRequires:  systemd-rpm-macros

%description
%{summary}.

%package docs
Summary:        Documentation for %{name}
BuildArch:      noarch

%description docs
This package contains the documentation for %{name}.

%prep
%autosetup

%build
%meson -Dgtk_doc=true
%meson_build

%install
%meson_install
mkdir -p $RPM_BUILD_ROOT/%{_localstatedir}/lib/power-profiles-daemon

%check
%meson_test

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%triggerpostun -- power-profiles-daemon < 0.10.1-2
if [ $1 -gt 1 ] && [ -x /usr/bin/systemctl ] ; then
    # Apply power-profiles-daemon.service preset on upgrades to F35 and F36 as
    # the preset was changed to enabled in F35.
    /usr/bin/systemctl --no-reload preset power-profiles-daemon.service || :
fi

%files
%license COPYING
%doc README.md
%{_bindir}/powerprofilesctl
%{_libexecdir}/%{name}
%{_unitdir}/%{name}.service
%{_sysconfdir}/dbus-1/system.d/net.hadess.PowerProfiles.conf
%{_datadir}/dbus-1/system-services/net.hadess.PowerProfiles.service
%{_datadir}/polkit-1/actions/net.hadess.PowerProfiles.policy
%{_localstatedir}/lib/power-profiles-daemon

%files docs
%dir %{_datadir}/gtk-doc/
%dir %{_datadir}/gtk-doc/html/
%{_datadir}/gtk-doc/html/%{name}/

%changelog
* Mon May 02 2022 Bastien Nocera <bnocera@redhat.com> - 0.11.1-1
+ power-profiles-daemon-0.11.1-1
- Update to 0.11.1

* Fri Apr 29 2022 Bastien Nocera <bnocera@redhat.com> - 0.11-1
+ power-profiles-daemon-0.11-1
- Update to 0.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Nov 05 2021 Kalev Lember <klember@redhat.com> - 0.10.1-2
- Apply power-profiles-daemon.service preset on upgrades to F35 and F36

* Thu Oct 28 2021 Bastien Nocera <bnocera@redhat.com> - 0.10.1-1
- power-profiles-daemon-0.10.1-1
- Update to 0.10.1

* Mon Oct 04 2021 Bastien Nocera <bnocera@redhat.com> - 0.10.0-1
+ power-profiles-daemon-0.10.0-1
- Update to 0.10.0

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jul 20 2021 Bastien Nocera <bnocera@redhat.com> - 0.9.0-1
+ power-profiles-daemon-0.9.0-1
- Update to 0.9.0

* Wed Apr 14 2021 Bastien Nocera <bnocera@redhat.com> - 0.8.1-2
+ power-profiles-daemon-0.8.1-2
- Remove linter, as apparently unwanted in check section

* Thu Apr 01 2021 Bastien Nocera <bnocera@redhat.com> - 0.8.1-1
+ power-profiles-daemon-0.8.1-1
- Update to 0.8.1

* Mon Mar 22 2021 Bastien Nocera <bnocera@redhat.com> - 0.8-1
+ power-profiles-daemon-0.8-1
- Update to 0.8

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.1-4
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Oct 28 2020 Bastien Nocera <bnocera@redhat.com> - 0.1-2
+ power-profiles-daemon-0.1-2
- Reload presets when updating from an older version

* Fri Aug 07 2020 Bastien Nocera <bnocera@redhat.com> - 0.1-1
- Initial package
