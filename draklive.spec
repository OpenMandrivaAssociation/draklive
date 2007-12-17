%define name draklive
%define version 0.6
%define release %mkrel 1

Summary:	Live systems generation and copying tool
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{name}-%{version}.tar.bz2
License:	GPLv2+
Group:		System/Configuration/Other
Url:		http://wiki.mandriva.com/Development/Packaging/Tools/draklive
BuildArch:      noarch
Requires:       syslinux grub
Requires:       cdrkit cdrkit-genisoimage mkcd
Requires:       curl rsync dosfstools mtools patch squashfs-tools setarch urpmi

%description
This tool lets you generate Mandriva live systems.

%prep
%setup -q

%build

%install
rm -rf %{buildroot}
install -D -m 0755 %{name} %{buildroot}/%{_sbindir}/%{name}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc NEWS
%{_sbindir}/%{name}
