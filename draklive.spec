%define name draklive
%define version 0.9
%define release %mkrel 4

Summary:	Live systems generation and copying tool
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{name}-%{version}.tar.xz
License:	GPLv2+
Group:		System/Configuration/Other
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Url:		http://wiki.mandriva.com/Development/Packaging/Tools/draklive
BuildArch:      noarch
Requires:       syslinux grub
Requires:       cdrkit cdrkit-genisoimage mkcd
Requires:       curl rsync dosfstools mtools patch squashfs3-tools setarch urpmi
Suggests:	draklive-config-One
Suggests:	drakx-installer-images drakx-installer-rescue
Suggests:	x11-server-xnest mkisofs

%description
This tool lets you generate Mandriva live systems.

%prep
%setup -q

%build

%install
rm -rf %{buildroot}
install -D -m 0755 %{name} %{buildroot}/%{_sbindir}/%{name}
mkdir -p %{buildroot}/%{perl_vendorlib}/MDV/Draklive/
install -D -m 0755 lib/MDV/Draklive/*.pm %{buildroot}/%{perl_vendorlib}/MDV/Draklive/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc NEWS
%{_sbindir}/%{name}
%{perl_vendorlib}/MDV/Draklive/*

