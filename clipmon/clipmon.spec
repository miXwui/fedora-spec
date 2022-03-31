%global commit ed0d771a0995c599f083c5b56091331edee71e83
%global debug_package %{nil}

Name:           clipmon
Version:        0.1.0
Release:        0%{?dist}
Summary:        https://git.sr.ht/~whynothugo/%{name}
License:        ISC
URL:            https://git.sr.ht/~whynothugo/%{name}
# https://git.sr.ht/~whynothugo/clipmon/archive/%{commit}.tar.gz
Source0:        ${name}-%{commit}.tar.gz
Patch0:         remove-superfluous-logging.patch
BuildRequires:  rust
BuildRequires:  cargo

%description
`clipmon`, or **clip**board **mon**itor is a wayland helper that:

1. It keeps the selection when the application that copied exits. Normally,
   when the copying application exits, the selection is lost and this can be
   rather annoying. Keeping the selection around matches what is normally
   expected to happen on a modern desktop. **This feature is stable**.
2. Shows a notification when an application pastes a selection. This is
   intended as a security measure: when an untrusted application (ideally
   sandboxed) snooping on the clipboard, the user will quickly by notified of
   what's going on. **This feature is WIP**.

The initial intention was meretly the second feature, but due to limitations of
the underlying Wayland protocol, it's necessary to implement a clipboard
monitor to achieve this.

%prep
%setup -n %{name}-%{commit}
%patch0 -p1

%build
cargo build --release

%install
install -Dm755 %{_builddir}/%{name}-%{commit}/target/release/%{name} %{buildroot}%{_exec_prefix}/lib/%{name}
install -Dm644 %{_builddir}/%{name}-%{commit}/%{name}.service %{buildroot}%{_exec_prefix}/lib/systemd/user/%{name}.service

%files
%{_exec_prefix}/lib/%{name}
%{_exec_prefix}/lib/systemd/user/%{name}.service

%changelog
* Thu Mar 31 2022 Michael Wu <me@miXwui.com> - 0.1.0-1
- Initial package
