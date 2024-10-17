%define name draklive
%define version 0.9
%define release 7

Summary:	Live systems generation and copying tool
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{name}-%{version}.tar.xz
License:	GPLv2+
Group:		System/Configuration/Other
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Url:		https://wiki.mandriva.com/Development/Packaging/Tools/draklive
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



%changelog
* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 0.9-4mdv2011.0
+ Revision: 663854
- mass rebuild

* Thu Jul 22 2010 Funda Wang <fwang@mandriva.org> 0.9-3mdv2011.0
+ Revision: 556995
- rebuild

* Mon Mar 01 2010 Thierry Vignaud <tv@mandriva.org> 0.9-2mdv2010.1
+ Revision: 512890
- Suggests: x11-server-xnest mkisofs
  (according to http://wiki.mandriva.com/en/Draklive#Quickstart)

* Mon Jan 18 2010 Christophe Fergeau <cfergeau@mandriva.com> 0.9-1mdv2010.1
+ Revision: 493117
- 0.9:
  * config
- automatically export draklive settings to DRAKLIVE_ environment variables for install
- allow to specify mount options in fstab in media->{mount_options}
- make it possible to specify mount options for tmpfs mounts
- allow to skip writing fstab with live->{system}{skip_fstab}
- allow to skip writing bootloader config with live->{system}{skip_bootloader_config}
- allow to skip bootloader install with live->{system}{skip_bootloader_install}
- allow not to create initrd with live->{system}{no_initrd}
- allow to select which settings fields are used to build name, in live->{name_fields}
  * install
- generate lst.names files list
- make sure zh_TW and zh_CN will be included in language list
- clean resolv.conf later (so that network can be used in post)
  * initrd
- dropped splashy support, added plymouth support
  (using bootloader::add_boot_splash)
- don't mount /dev/pts since this causes huge slowdowns
- mount tmpfs partitions with 0755 perms (#51565):
  When using the obsolete --attach-to-session plymouth option, /dev/pts
  has to be mounted. But for some reason, nash interacts badly with
  mounted /dev/pts and freezes for dozen of seconds when running a builtin
  command. Remote --attach-to-session from plymouth which lets us get rid
  of /dev/pts mounting.
- add hack to use modules list from chroot
  (to handle different IDE modules name in build and target environments)
- detect some modules as built-in and do not wrongly abort
- do not create initrd symlink or append splash if no initrd has been created
- make sure /proc and /sys are available when building initrd (useful
  to see error messages at least, from Paulo Ricardo Zanoni)
- use bootloader module to build initrd and create kernel symlinks
  (Gdium friendly)
  * bootloader
- default to grub bootloader for harddisk storage
- fix installing grub to separate /boot partition
- use per-media additional boot_entries
- do not add default boot entry if media->{boot_entries} is specified
  (to allow having a custom default entry)
- fix installing grub to hidden /boot in master image
- set LD_LIBRARY_PATH to chroot libraries when running grub
- die in bootloader step if selected kernel does not exist
- do not add initrd in grub menu if it does not exist
- allow to install bootloader on separate /boot partition
- make sure the grub install script is executable
- do not overwrite grub conf for "classical" boot when installing
  bootloader
- use same bootloader install code for disks and USB masters
- remove hardcoded splashy code and use back bootloader::add_boot_splash
- run switch-themes -u
- use bootloader module to find kernel (Gdium friendly)
- update gfxboot theme before copying gfxboot files
- fix getting bootsplash theme (fixes gfxboot theme)
- do not add vga mode on kernel command line if forced in append
  (for drakx-based replicator)
- fix setting splash for classical bootloader
- create media specific gfxmenu if needed only
- always copy gfxmenu in build boot dir (needed for replicator)
- do not create bootloader files if bootloader install is to be skipped
- fix writing media specific boot for disk masters
  * master
- use -fatfirst option when hybridifying an image
- use DrakX partitioning/formatting code
- run udevsettle, like done in diskdrake::interactive::write_partitions
- allow to set custom media geometry in media->{geom}
- allow to format disk devices
- add ext4 and swap support in mkfs
- use ext4 by default for harddisk
- set label at mkfs time
- fix setting label on fat
- fix setting label for USB devices
- add default label for harddisk storage
- always compute master size from pre-computed partition sizes
- use apparent size when computing loopbacks size (system loopback can be sparse)
- supplement / partition label with default one if needed
- allow to add an OEM rescue partition in the master (quite hackish, using live->{oem_rescue})
- preset fs_type for OEM_RESCUE partition too
- allow to set inode size in media->{inode_size} for ext2/ext3 file systems
- preserve timestamps when copying files
  * image
- allow to compress master images as gzip instead of bzip2 by setting
  compression_method=gzip in settings.cfg (from Paulo Ricardo Zanoni)
  * vm-image
- create vmdk virtual machine images (for VMware, VirtualBox, qemu)
  * replicator
- copy syslinux dir for replicator too
- always create syslinux msg files (useful for cdrom replicator)
- allow drakx-based replicator
  (by setting live->{settings}{replicator_type} to "drakx")
- write image size in master list file
- write bootloader config for replicator media
  * record
- use full disk device when recording harddisk/oem_rescue/replicator/USB masters
- allow to mount multiple partitions before recording target master
- do not try to use configured media source when it is not a label, it
  could be a device (/dev/sda1) that should not be touched on the
  build machine, force it to be passed as an option

* Thu Aug 20 2009 Olivier Blin <oblin@mandriva.com> 0.8-3mdv2010.0
+ Revision: 418361
- suggest drakx-installer-images and drakx-installer-rescue for replicator images

* Thu Jun 04 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.8-2mdv2010.0
+ Revision: 382829
- 0.8:
- forgot to package some new .pm files

* Tue Apr 28 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.8-1mdv2010.0
+ Revision: 369113
- 0.8:
  * loop
- use legacy mksquashfs3 instead of the new mksquashfs
- use 1MB squashfs blocks, this gives us about 10%% better compression
  * bootloader
- remove unneeded locale files from gfxboot bootlogo file (causes boot issues
  on some machines)
- add 'harddrive' boot entry to chainload to the harddrive bootloader
- use latest syslinux + gfxboot COM module
  * master
- hybridify generated ISOs so that they can be dumped on USB keys
- Update package name for squashfs3

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 0.7-2mdv2009.0
+ Revision: 220685
- rebuild

* Thu Apr 03 2008 Olivier Blin <oblin@mandriva.com> 0.7-1mdv2008.1
+ Revision: 192040
- suggest draklive-config-One
- 0.7
- initrd
  o do not copy and load twice additional modules if they were listed in
  extra modules
  o use nash-mount instead of mount
  o create /etc/blkid and use "showlabels --removable" to get CD-Rom
  labels in blkid cache
  o adapt to new probe-modules syntax for storage bus
  o use stage1's probe-modules instead of dropped nash's insmod
  o move initrd modules in /lib/modules/`uname -r`
  o gzip initrd modules
  o use depmod to generate modules.dep
  o do not print excluding modules warning if not needed
  o check that there is enough space left in initrd
  o umount /proc/bus/usb before pivot_root in initrd
  o add firewire controllers (bus and disk) in CDROM live (#31356)
  o use libraries from /lib instead of /lib/i686 (#38649) and /lib/tls
  (#21683) to be able to boot on processors without cmov
- bootloader
  o remove hardcoded fastboot option (new initscripts do not fsck rw /)
- master
  o handle genisoimage progress more nicely
  o insert mkcd checksum before computing md5/sha1 checksums
  o hide mkcd output
- dist
  o rename "images" directory as "dist"
  o create packages lst in dist
  o write a .langs file with human-readable langs list
  o write full list of rpm packages and list of rpm leaves, sorted by
  package size
- misc
  o do not try to use consolehelper to display "must be root" message,
  it's broken outside of X

  + Thierry Vignaud <tv@mandriva.org>
    - fix no-buildroot-tag
    - kill re-definition of %%buildroot on Pixel's request

* Thu Dec 13 2007 Olivier Blin <oblin@mandriva.com> 0.6-1mdv2008.1
+ Revision: 119524
- 0.6
- require mkcd (to add md5sum)

* Wed Sep 19 2007 Adam Williamson <awilliamson@mandriva.org> 0.5-2mdv2008.0
+ Revision: 90117
- rebuild for 2008
- new license policy

  + Olivier Blin <oblin@mandriva.com>
    - require dosfstools


* Tue Mar 13 2007 Olivier Blin <oblin@mandriva.com> 0.5-1mdv2007.1
+ Revision: 142269
- 0.5

* Wed Mar 07 2007 Olivier Blin <oblin@mandriva.com> 0.4-1mdv2007.1
+ Revision: 134804
- 0.4

* Mon Feb 12 2007 Olivier Blin <oblin@mandriva.com> 0.3-1mdv2007.1
+ Revision: 120038
- require urpmi
- require curl
- require wodim and genisomage
- require grub
- add NEWS file
- 0.3
- do not package copy wizard anymore
- update url
- require setarch
- require squashfs-tools
- require patch
- Import draklive

* Sun Sep 17 2006 Olivier Blin <oblin@mandriva.com> 0.2-1mdv2007.0
- 0.2

* Tue Aug 22 2006 Olivier Blin <oblin@mandriva.com> 0.1-2mdv2007.0
- allow to add additionnal boot entries
- run shell in initrd when the "debug" option is on cmdline
- use patch batch mode (-t) not to apply already applied patches
  and die if a patch can't be applied
- create modules tree root (for x86_64)
- remove modprobe.preload.d files
- require syslinux, cdrecord, rsync and mtools

* Tue Jun 20 2006 Olivier Blin <oblin@mandriva.com> 0.1-1mdv2007.0
- initial release

