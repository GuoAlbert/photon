%global security_hardening none
Summary:        Kernel
Name:           linux
Version:    	4.4.202
Release:        2%{?kat_build:.%kat_build}%{?dist}
License:    	GPLv2
URL:        	http://www.kernel.org/
Group:        	System Environment/Kernel
Vendor:         VMware, Inc.
Distribution: 	Photon
Source0:    	http://www.kernel.org/pub/linux/kernel/v4.x/%{name}-%{version}.tar.xz
%define sha1 linux=0f9d976a844c81b3174a79c62c1d1265116328c3
Source1:	config
%define ena_version 1.1.3
Source2:    	https://github.com/amzn/amzn-drivers/archive/ena_linux_1.1.3.tar.gz
%define sha1 ena_linux=84138e8d7eb230b45cb53835edf03ca08043d471
Source3:        update_photon_cfg.postun
Patch0:         double-tcp_mem-limits.patch
Patch1:         linux-4.4-sysctl-sched_weighted_cpuload_uses_rla.patch
Patch2:         linux-4.4-watchdog-Disable-watchdog-on-virtual-machines.patch
Patch3:         SUNRPC-Do-not-reuse-srcport-for-TIME_WAIT-socket.patch
Patch4:         06-sunrpc.patch
Patch5:         vmware-log-kmsg-dump-on-panic.patch
Patch6:         vmxnet3-1.4.6.0-update-rx-ring2-max-size.patch
Patch7:	        vmxnet3-1.4.6.0-avoid-calling-pskb_may_pull-with-interrupts-disabled.patch
#for linux-tools
Patch8:		perf-top-sigsegv-fix.patch
Patch9:         REVERT-sched-fair-Beef-up-wake_wide.patch
Patch10:        e1000e-prevent-div-by-zero-if-TIMINCA-is-zero.patch
Patch12:        vmxnet3-1.4.6.0-fix-lock-imbalance-in-vmxnet3_tq_xmit.patch
Patch13:        vmxnet3-1.4.7.0-set-CHECKSUM_UNNECESSARY-for-IPv6-packets.patch
Patch14:        vmxnet3-1.4.8.0-segCnt-can-be-1-for-LRO-packets.patch
#fixes CVE-2016-6187
Patch15:        apparmor-fix-oops-validate-buffer-size-in-apparmor_setprocattr.patch
Patch16:        vsock-transport-for-9p.patch
#allow some algorithms in FIPS mode
Patch17:        0001-Revert-crypto-testmgr-Disable-fips-allowed-for-authe.patch
Patch18:        0002-allow-also-ecb-cipher_null.patch
Patch19:	net-9p-vdfs-zerocopy.patch
Patch20:        0001-Enable-cache-loose-for-vdfs-9p.patch
# Fix for CVE-2018-8043
Patch22:        0001-net-phy-mdio-bcm-unimac-fix-potential-NULL-dereferen.patch
# Fix for CVE-2019-19066
Patch23:        0001-scsi_bfa_release_allocated_memory_in_case_of_error.patch

Patch26:        Implement-the-f-xattrat-family-of-functions.patch
Patch27:        0001-hwrng-rdrand-Add-RNG-driver-based-on-x86-rdrand-inst.patch
# Fix for CVE-2017-18232
Patch28:        0001-scsi-libsas-direct-call-probe-and-destruct.patch
# Fix for CVE-2018-10323
Patch29:        0001-xfs-set-format-back-to-extents-if-xfs_bmap_extents_t.patch
# Fix for CVE-2018-10322 (following 8 patches)
Patch34:        0001-xfs-add-missing-include-dependencies-to-xfs_dir2.h.patch
Patch35:        0002-xfs-replace-xfs_mode_to_ftype-table-with-switch-stat.patch
Patch36:        0003-xfs-fix-xfs_mode_to_ftype-prototype.patch
Patch37:        0004-xfs-sanity-check-directory-inode-di_size.patch
Patch38:        0005-xfs-sanity-check-inode-di_mode.patch
Patch39:        0006-xfs-verify-dinode-header-first.patch
Patch40:        0007-xfs-move-inode-fork-verifiers-to-xfs_dinode_verify.patch
Patch41:        0008-xfs-enhance-dinode-verifier.patch
# Fix for CVE-2018-16882
Patch43:        0001-KVM_Fix_UAF_in_nested_posted_interrupt_processing.patch
#Fix CVE-2019-8912
Patch44:        fix_use_after_free_in_sockfs_setattr.patch
# Fix for CVE-2019-12456
Patch45:        0001-scsi-mpt3sas_ctl-fix-double-fetch-bug-in-_ctl_ioctl_.patch
# Fix for CVE-2019-12379
Patch48:        0001-consolemap-Fix-a-memory-leaking-bug-in-drivers-tty-v.patch
# Fix for CVE-2019-12381
Patch49:        0001-ip_sockglue-Fix-missing-check-bug-in-ip_ra_control.patch
# Fix for CVE-2019-12382
Patch50:        0001-drm-edid-Fix-a-missing-check-bug-in-drm_load_edid_fi.patch
# Fix for CVE-2019-12378
Patch51:        0001-ipv6_sockglue-Fix-a-missing-check-bug-in-ip6_ra_cont.patch

# Fix for CVE-2019-11487
Patch52:        0001-mm-make-page-ref-count-overflow-check-tighter-and-mo.patch
Patch53:        0002-mm-add-try_get_page-helper-function.patch
Patch54:        0003-mm-handle-PTE-mapped-tail-pages-in-gerneric-fast-gup.patch
Patch55:        0004-mm-gup-remove-broken-VM_BUG_ON_PAGE-compound-check-f.patch
Patch56:        0005-mm-gup-ensure-real-head-page-is-ref-counted-when-usi.patch
Patch57:        0006-mm-prevent-get_user_pages-from-overflowing-page-refc.patch
Patch58:        0007-pipe-add-pipe_buf_get-helper.patch
Patch59:        0008-fs-prevent-page-refcount-overflow-in-pipe_buf_get.patch

# For Spectre
Patch67: 0169-x86-syscall-Clear-unused-extra-registers-on-syscall-.patch


%if 0%{?kat_build:1}
Patch1000:	%{kat_build}.patch
%endif
BuildRequires:  bc
BuildRequires:  kbd
BuildRequires:  kmod
BuildRequires:  glib-devel
BuildRequires:  xerces-c-devel
BuildRequires:  xml-security-c-devel
BuildRequires:  libdnet
BuildRequires:  libmspack
BuildRequires:  Linux-PAM
BuildRequires:  openssl-devel audit-devel
BuildRequires:  procps-ng-devel
BuildRequires:  elfutils-libelf-devel
Requires:       filesystem kmod coreutils
Requires(postun): coreutils
%define uname_r %{version}-%{release}

%description
The Linux package contains the Linux kernel. 


%package dev
Summary:    Kernel Dev
Group:        System Environment/Kernel
Provides:    linux-devel = %{version}-%{release}
Requires:    %{name} = %{version}-%{release}
Requires:    python2
%description dev
The Linux package contains the Linux kernel dev files

%package drivers-gpu
Summary:    Kernel GPU Drivers
Group:        System Environment/Kernel
Requires:    %{name} = %{version}-%{release}
%description drivers-gpu
The Linux package contains the Linux kernel drivers for GPU

%package sound
Summary:    Kernel Sound modules
Group:        System Environment/Kernel
Requires:    %{name} = %{version}-%{release}
%description sound
The Linux package contains the Linux kernel sound support

%package docs
Summary:    Kernel docs
Group:        System Environment/Kernel
Requires:    %{name} = %{version}-%{release}
Requires:    python2
%description docs
The Linux package contains the Linux kernel doc files

%package oprofile
Summary:    Kernel driver for oprofile, a statistical profiler for Linux systems
Group:        System Environment/Kernel
Requires:    %{name} = %{version}-%{release}
%description oprofile
Kernel driver for oprofile, a statistical profiler for Linux systems

%package tools
Summary:      This package contains the 'perf' performance analysis tools for Linux kernel
Group:        System/Tools
Requires:     audit
Requires:    %{name} = %{version}-%{release}
%description tools
This package contains the 'perf' performance analysis tools for Linux kernel.


%prep
%setup -q
%setup -D -b 2

%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch22 -p1
%patch23 -p1
%patch26 -p1
%patch27 -p1
%patch28 -p1
%patch29 -p1
%patch34 -p1
%patch35 -p1
%patch36 -p1
%patch37 -p1
%patch38 -p1
%patch39 -p1
%patch40 -p1
%patch41 -p1
%patch43 -p1
%patch44 -p1
%patch45 -p1
%patch48 -p1
%patch49 -p1
%patch50 -p1
%patch51 -p1
%patch52 -p1
%patch53 -p1
%patch54 -p1
%patch55 -p1
%patch56 -p1
%patch57 -p1
%patch58 -p1
%patch59 -p1
%patch67 -p1

%if 0%{?kat_build:1}
%patch1000 -p1
%endif

%build
make mrproper
cp %{SOURCE1} .config
sed -i 's/CONFIG_LOCALVERSION=""/CONFIG_LOCALVERSION="-%{release}"/' .config
make LC_ALL= oldconfig
make VERBOSE=1 KBUILD_BUILD_VERSION="1-photon" KBUILD_BUILD_HOST="photon" ARCH="x86_64" %{?_smp_mflags}
make -C tools perf
# build ENA module
bldroot=`pwd`
pushd ../amzn-drivers-ena_linux_%{ena_version}/kernel/linux/ena
make -C $bldroot M=`pwd` VERBOSE=1 modules %{?_smp_mflags}
popd

%define __modules_install_post \
    find %{buildroot}/lib/modules/%{uname_r} -name *.ko | xargs xz \
%{nil}
%define __modules_install_post \
for MODULE in `find %{buildroot}/lib/modules/%{uname_r} -name *.ko` ; do \
    ./scripts/sign-file sha512 certs/signing_key.pem certs/signing_key.x509 $MODULE \
    rm -f $MODULE.{sig,dig} \
    xz $MODULE \
    done \
%{nil}

# We want to compress modules after stripping. Extra step is added to
# the default __spec_install_post.
%define __spec_install_post\
    %{?__debug_package:%{__debug_install_post}}\
    %{__arch_install_post}\
    %{__os_install_post}\
    %{__modules_install_post}\
%{nil}

%install
install -vdm 755 %{buildroot}/etc
install -vdm 755 %{buildroot}/boot
install -vdm 755 %{buildroot}%{_defaultdocdir}/%{name}-%{uname_r}
install -vdm 755 %{buildroot}/etc/modprobe.d
install -vdm 755 %{buildroot}/usr/src/%{name}-headers-%{uname_r}
install -vdm 755 %{buildroot}/usr/lib/debug/lib/modules/%{uname_r}
make INSTALL_MOD_PATH=%{buildroot} modules_install
# install ENA module
bldroot=`pwd`
pushd ../amzn-drivers-ena_linux_%{ena_version}/kernel/linux/ena
make -C $bldroot M=`pwd` INSTALL_MOD_PATH=%{buildroot} modules_install
popd

# Verify for build-id match
# We observe different IDs sometimes
# TODO: debug it
ID1=`readelf -n vmlinux | grep "Build ID"`
./scripts/extract-vmlinux arch/x86/boot/bzImage > extracted-vmlinux
ID2=`readelf -n extracted-vmlinux | grep "Build ID"`
if [ "$ID1" != "$ID2" ] ; then
	echo "Build IDs do not match"
	echo $ID1
	echo $ID2
	exit 1
fi
install -vm 644 arch/x86/boot/bzImage %{buildroot}/boot/vmlinuz-%{uname_r}
# Restrict the permission on System.map-X file
install -vm 400 System.map %{buildroot}/boot/System.map-%{uname_r}
install -vm 644 .config %{buildroot}/boot/config-%{uname_r}
cp -r Documentation/*        %{buildroot}%{_defaultdocdir}/%{name}-%{uname_r}
install -vm 644 vmlinux %{buildroot}/usr/lib/debug/lib/modules/%{uname_r}/vmlinux-%{uname_r}
# `perf test vmlinux` needs it
ln -s vmlinux-%{uname_r} %{buildroot}/usr/lib/debug/lib/modules/%{uname_r}/vmlinux

cat > %{buildroot}/boot/%{name}-%{uname_r}.cfg << "EOF"
# GRUB Environment Block
photon_cmdline=init=/lib/systemd/systemd ro loglevel=3 quiet plymouth.enable=0
photon_linux=vmlinuz-%{uname_r}
photon_initrd=initrd.img-%{uname_r}
EOF

#    Cleanup dangling symlinks
rm -rf %{buildroot}/lib/modules/%{uname_r}/source
rm -rf %{buildroot}/lib/modules/%{uname_r}/build

find . -name Makefile* -o -name Kconfig* -o -name *.pl | xargs  sh -c 'cp --parents "$@" %{buildroot}/usr/src/%{name}-headers-%{uname_r}' copy
find arch/x86/include include scripts -type f | xargs  sh -c 'cp --parents "$@" %{buildroot}/usr/src/%{name}-headers-%{uname_r}' copy
find $(find arch/x86 -name include -o -name scripts -type d) -type f | xargs  sh -c 'cp --parents "$@" %{buildroot}/usr/src/%{name}-headers-%{uname_r}' copy
find arch/x86/include Module.symvers include scripts -type f | xargs  sh -c 'cp --parents "$@" %{buildroot}/usr/src/%{name}-headers-%{uname_r}' copy

cp .config %{buildroot}/usr/src/%{name}-headers-%{uname_r} # copy .config manually to be where it's expected to be
ln -sf "/usr/src/%{name}-headers-%{uname_r}" "%{buildroot}/lib/modules/%{uname_r}/build"
find %{buildroot}/lib/modules -name '*.ko' -print0 | xargs -0 chmod u+x

# disable (JOBS=1) parallel build to fix this issue:
# fixdep: error opening depfile: ./.plugin_cfg80211.o.d: No such file or directory
# Linux version that was affected is 4.4.26
make -C tools JOBS=1 DESTDIR=%{buildroot} prefix=%{_prefix} perf_install

%include %{SOURCE3}

%post
/sbin/depmod -a %{uname_r}
ln -sf %{name}-%{uname_r}.cfg /boot/photon.cfg

%post drivers-gpu
/sbin/depmod -a %{uname_r}

%post sound
/sbin/depmod -a %{uname_r}

%post oprofile
/sbin/depmod -a %{uname_r}

%files
%defattr(-,root,root)
/boot/System.map-%{uname_r}
/boot/config-%{uname_r}
/boot/vmlinuz-%{uname_r}
%config(noreplace) /boot/%{name}-%{uname_r}.cfg
/lib/firmware/*
%defattr(0644,root,root)
/lib/modules/%{uname_r}/*
%exclude /lib/modules/%{uname_r}/build
%exclude /lib/modules/%{uname_r}/kernel/drivers/gpu
%exclude /lib/modules/%{uname_r}/kernel/sound
%exclude /lib/modules/%{uname_r}/kernel/arch/x86/oprofile/

%files docs
%defattr(-,root,root)
%{_defaultdocdir}/%{name}-%{uname_r}/*

%files dev
%defattr(-,root,root)
/lib/modules/%{uname_r}/build
/usr/src/%{name}-headers-%{uname_r}

%files drivers-gpu
%defattr(-,root,root)
%exclude /lib/modules/%{uname_r}/kernel/drivers/gpu/drm/cirrus/
/lib/modules/%{uname_r}/kernel/drivers/gpu

%files sound
%defattr(-,root,root)
/lib/modules/%{uname_r}/kernel/sound

%files oprofile
%defattr(-,root,root)
/lib/modules/%{uname_r}/kernel/arch/x86/oprofile/

%files tools
%defattr(-,root,root)
/usr/libexec
/usr/lib64/traceevent
%{_bindir}
/etc/bash_completion.d/*
/usr/share/perf-core

%changelog
*   Tue Nov 26 2019 Ajay Kaher <akaher@vmware.com> 4.4.202-2
-   Fix CVE-2019-19066
*   Tue Nov 19 2019 Srivatsa S. Bhat (VMware) <srivatsa@csail.mit.edu> 4.4.202-1
-   Update to version 4.4.202
*   Tue Nov 12 2019 Srivatsa S. Bhat (VMware) <srivatsa@csail.mit.edu> 4.4.201-1
-   Update to version 4.4.201
*   Thu Nov 07 2019 Srivatsa S. Bhat (VMware) <srivatsa@csail.mit.edu> 4.4.199-1
-   Update to version 4.4.199
*   Fri Oct 11 2019 Ajay Kaher <akaher@vmware.com> 4.4.196-1
-   Update to version 4.4.196
*   Wed Sep 18 2019 bvikas <bvikas@vmware.com> 4.4.193-1
-   Update to version 4.4.193
*   Mon Sep 09 2019 Srivatsa S. Bhat (VMware) <srivatsa@csail.mit.edu> 4.4.191-1
-   Update to version 4.4.191
*   Mon Sep 02 2019 Mounesh Badiger <badigerm@vmware.com> 4.4.189-2
-   9p: use loose cache only for metadata
*   Mon Aug 12 2019 Alexey Makhalov <amakhalov@vmware.com> 4.4.189-1
-   Update to version 4.4.189 to fix CVE-2019-1125
*   Thu Jul 25 2019 Keerthana K <keerthanak@vmware.com> 4.4.185-3
-   Fix postun scriplet.
*   Thu Jul 25 2019 Ajay Kaher <akaher@vmware.com> 4.4.185-2
-   Fix CVE-2019-11487
*   Wed Jul 10 2019 VIKASH BANSAL <bvikas@vmware.com> 4.4.185-1
-   Update to version 4.4.185
*   Mon Jun 17 2019 Srivatsa S. Bhat (VMware) <srivatsa@csail.mit.edu> 4.4.182-1
-   Update to version 4.4.182
-   Fix CVE-2019-12456, CVE-2018-16597, CVE-2018-19407, CVE-2019-12379,
-   CVE-2019-12381, CVE-2019-12382, CVE-2019-12378
*   Tue Jun 11 2019 Srivatsa S. Bhat (VMware) <srivatsa@csail.mit.edu> 4.4.181-1
-   Update to version 4.4.181
*   Tue May 28 2019 Srivatsa S. Bhat (VMware) <srivatsa@csail.mit.edu> 4.4.180-3
-   Change default I/O scheduler to 'deadline' to fix performance issue.
*   Tue May 28 2019 Keerthana K <keerthanak@vmware.com> 4.4.180-2
-   Fix to parse through /boot folder and update symlink (/boot/photon.cfg) if
-   mulitple kernels are installed and current linux kernel is removed.
*   Fri May 17 2019 Ajay Kaher <akaher@vmware.com> 4.4.180-1
-   Update to version 4.4.180
*   Tue May 14 2019 Ajay Kaher <akaher@vmware.com> 4.4.178-2
-   Fix CVE-2019-11599
*   Fri Apr 05 2019 Srivatsa S. Bhat (VMware) <srivatsa@csail.mit.edu> 4.4.178-1
-   Update to version 4.4.178
*   Wed Mar 27 2019 Srivatsa S. Bhat (VMware) <srivatsa@csail.mit.edu> 4.4.177-1
-   Update to version 4.4.177
*   Fri Feb 22 2019 Srinidhi Rao<srinidhir@vmware.com> 4.4.174-1
-   Update kernel version to 4.4.174
*   Thu Feb 21 2019 Him Kalyan Bordoloi <bordoloih@vmware.com> 4.4.171-3
-   Fix CVE-2019-8912
*   Wed Jan 30 2019 Ajay Kaher <akaher@vmware.com> 4.4.171-2
-   Fix CVE-2018-16882
*   Thu Jan 24 2019 Ajay Kaher <akaher@vmware.com> 4.4.171-1
-   Update to version 4.4.171
*   Tue Jan 15 2019 Alexey Makhalov <amakhalov@vmware.com> 4.4.164-4
-   .config: disable CONFIG_FANOTIFY_ACCESS_PERMISSIONS
-   Removed deprecated -q option for depmod
*   Thu Dec 20 2018 Alexey Makhalov <amakhalov@vmware.com> 4.4.164-3
-   .config: CONFIG_FANOTIFY_ACCESS_PERMISSIONS=y
*   Wed Dec 12 2018 Kamal Charan <kcharan@vmware.com> 4.4.164-2
-   Add 9p zero copy data path using crossfd
*   Mon Nov 26 2018 Srivatsa S. Bhat (VMware) <srivatsa@csail.mit.edu> 4.4.164-1
-   Update to version 4.4.164
*   Wed Nov 14 2018 Srivatsa S. Bhat (VMware) <srivatsa@csail.mit.edu> 4.4.163-1
-   Update to version 4.4.163
*   Mon Oct 15 2018 Srivatsa S. Bhat <srivatsa@csail.mit.edu> 4.4.161-1
-   Update to version 4.4.161
*   Mon Sep 24 2018 Srivatsa S. Bhat <srivatsa@csail.mit.edu> 4.4.157-1
-   Update to version 4.4.157 and fix CVE-2018-10879
*   Tue Sep 18 2018 Srivatsa S. Bhat <srivatsa@csail.mit.edu> 4.4.153-3
-   Improve error-handling of rdrand-rng kernel driver.
*   Fri Sep 07 2018 Srivatsa S. Bhat <srivatsa@csail.mit.edu> 4.4.153-2
-   Fix CVE-2018-13053
*   Tue Sep 04 2018 Srivatsa S. Bhat <srivatsa@csail.mit.edu> 4.4.153-1
-   Update to version 4.4.153
*   Fri Aug 24 2018 Bo Gan <ganb@vmware.com> 4.4.152-1
-   Update to version 4.4.152
*   Fri Aug 17 2018 Bo Gan <ganb@vmware.com> 4.4.148-1
-   Update to version 4.4.148 (l1tf fixes)
*   Thu Aug 09 2018 Srivatsa S. Bhat <srivatsa@csail.mit.edu> 4.4.147-1
-   Update to version 4.4.147 to fix CVE-2018-12233.
*   Tue Aug 07 2018 Srivatsa S. Bhat <srivatsa@csail.mit.edu> 4.4.146-1
-   Update to version 4.4.146
*   Mon Jul 30 2018 Srivatsa S. Bhat <srivatsa@csail.mit.edu> 4.4.145-1
-   Update to version 4.4.145 and clear stack on fork.
*   Thu Jul 26 2018 Srivatsa S. Bhat <srivatsa@csail.mit.edu> 4.4.144-1
-   Update to version 4.4.144 and fix CVE-2018-10322
*   Mon Jul 16 2018 Srivatsa S. Bhat <srivatsa@csail.mit.edu> 4.4.140-1
-   Update to version 4.4.140 and fix CVE-2017-18249
*   Wed Jul 11 2018 Srivatsa S. Bhat <srivatsa@csail.mit.edu> 4.4.139-3
-   Use AppArmor security module by default.
*   Tue Jul 10 2018 Srivatsa S. Bhat <srivatsa@csail.mit.edu> 4.4.139-2
-   Fix CVE-2017-18232 and CVE-2018-10323.
*   Tue Jul 03 2018 Srivatsa S. Bhat <srivatsa@csail.mit.edu> 4.4.139-1
-   Update to version 4.4.139
*   Thu Jun 28 2018 Srivatsa S. Bhat <srivatsa@csail.mit.edu> 4.4.138-2
-   Add rdrand-based RNG driver to enhance kernel entropy.
*   Mon Jun 25 2018 Srivatsa S. Bhat <srivatsa@csail.mit.edu> 4.4.138-1
-   Update to version 4.4.138
*   Thu Jun 14 2018 Srivatsa S. Bhat <srivatsa@csail.mit.edu> 4.4.137-2
-   Add more spectre mitigations (IBPB/IBRS) and support for SSBD.
*   Wed Jun 13 2018 Alexey Makhalov <amakhalov@vmware.com> 4.4.137-1
-   Update to version 4.4.137. Fix panic in kprobe.
*   Mon May 21 2018 Bo Gan <ganb@vmware.com> 4.4.131-3
-   Implement the f*xattrat family of syscalls (Previously linux-esx only)
*   Fri May 04 2018 Srivatsa S. Bhat <srivatsa@csail.mit.edu> 4.4.131-2
-   Fix CVE-2018-8043, CVE-2017-18216, CVE-2018-8087, CVE-2017-18241.
*   Fri May 04 2018 Srivatsa S. Bhat <srivatsa@csail.mit.edu> 4.4.131-1
-   Update to version 4.4.131
*   Wed May 02 2018 Srivatsa S. Bhat <srivatsa@csail.mit.edu> 4.4.130-2
-   Fix CVE-2017-18255.
*   Mon Apr 30 2018 Srivatsa S. Bhat <srivatsa@csail.mit.edu> 4.4.130-1
-   Update to version 4.4.130 and fix CVE-2018-1000026.
*   Thu Apr 19 2018 Srivatsa S. Bhat <srivatsa@csail.mit.edu> 4.4.124-2
-   Add full retpoline support by building with retpoline-enabled gcc.
*   Tue Mar 27 2018 Srivatsa S. Bhat <srivatsa@csail.mit.edu> 4.4.124-1
-   Update to version 4.4.124
*   Thu Mar 08 2018 Him Kalyan Bordoloi <bordoloih@vmware.com> 4.4.115-2
-   Add build dependency of libelf. Needed by perf to resolve symbols.
*   Mon Feb 05 2018 Srivatsa S. Bhat <srivatsa@csail.mit.edu> 4.4.115-1
-   Update to version 4.4.115
*   Wed Jan 31 2018 Srivatsa S. Bhat <srivatsa@csail.mit.edu> 4.4.114-1
-   Update version to 4.4.114
*   Fri Jan 26 2018 Srivatsa S. Bhat <srivatsa@csail.mit.edu> 4.4.113-1
-   Update version to 4.4.113.
*   Fri Jan 19 2018 Bo Gan <ganb@vmware.com> 4.4.112-1
-   Version update to 4.4.112
*   Wed Jan 10 2018 Bo Gan <ganb@vmware.com> 4.4.111-1
-   Version update to 4.4.111
*   Mon Jan 08 2018 Bo Gan <ganb@vmware.com> 4.4.110-2
-   Initial Spectre fix
-   Add Observable speculation barrier
-   Clear unused register upon syscall entry
*   Fri Jan 05 2018 Anish Swaminathan <anishs@vmware.com> 4.4.110-1
-   Version update to 4.4.110
*   Thu Jan 04 2018 Srivatsa S. Bhat <srivatsa@csail.mit.edu> 4.4.109-3
-   Update vsock transport for 9p with newer version.
*   Wed Jan 03 2018 Srivatsa S. Bhat <srivatsa@csail.mit.edu> 4.4.109-2
-   Fix SMB3 mount regression.
*   Tue Jan 02 2018 Srivatsa S. Bhat <srivatsa@csail.mit.edu> 4.4.109-1
-   Version update
-   Add patches to fix CVE-2017-8824, CVE-2017-17448 and CVE-2017-17450.
*   Tue Dec 19 2017 Srivatsa S. Bhat <srivatsa@csail.mit.edu> 4.4.106-1
-   Version update
*   Tue Dec 12 2017 Alexey Makhalov <amakhalov@vmware.com> 4.4.104-2
-   KAT build support
*   Fri Dec 08 2017 Srivatsa S. Bhat <srivatsa@csail.mit.edu> 4.4.104-1
-   Version update
*   Mon Dec 04 2017 Srivatsa S. Bhat <srivatsa@csail.mit.edu> 4.4.103-1
-   Version update
*   Mon Nov 20 2017 Srivatsa S. Bhat <srivatsa@csail.mit.edu> 4.4.99-1
-   Version update
*   Tue Nov 07 2017 Alexey Makhalov <amakhalov@vmware.com> 4.4.96-1
-   Version update
*   Mon Oct 16 2017 Srivatsa S. Bhat <srivatsa@csail.mit.edu> 4.4.92-1
-   Version update
*   Mon Oct 16 2017 Srivatsa S. Bhat <srivatsa@csail.mit.edu> 4.4.88-2
-   Fix CVE-2017-11472 (ACPICA: Namespace: fix operand cache leak)
*   Fri Sep 22 2017 Alexey Makhalov <amakhalov@vmware.com> 4.4.88-1
-   Version update
*   Mon Sep 04 2017 Alexey Makhalov <amakhalov@vmware.com> 4.4.86-1
-   Fix CVE-2017-11600
*   Thu Aug 17 2017 Alexey Makhalov <amakhalov@vmware.com> 4.4.82-2
-   .config: disable XEN_BALLOON_MEMORY_HOTPLUG
*   Tue Aug 15 2017 Alexey Makhalov <amakhalov@vmware.com> 4.4.82-1
-   Version update
*   Fri Aug 11 2017 Alexey Makhalov <amakhalov@vmware.com> 4.4.81-1
-   Version update
*   Tue Aug 08 2017 Alexey Makhalov <amakhalov@vmware.com> 4.4.79-2
-   Fix CVE-2017-10911, CVE-2017-7542
-   [bugfix] Added ccm,gcm,ghash,zlib,lzo crypto modules to avoid
    panic on modprobe tcrypt
*   Wed Aug 02 2017 Alexey Makhalov <amakhalov@vmware.com> 4.4.79-1
-   Fix CVE-2017-11473
*   Tue Aug 01 2017 Anish Swaminathan <anishs@vmware.com> 4.4.77-2
-   Allow some algorithms in FIPS mode
-   Reverts 284a0f6e87b0721e1be8bca419893902d9cf577a and backports
-   bcf741cb779283081db47853264cc94854e7ad83 in the kernel tree
*   Mon Jul 17 2017 Alexey Makhalov <amakhalov@vmware.com> 4.4.77-1
-   Fix CVE-2017-11176
*   Wed Jun 28 2017 Alexey Makhalov <amakhalov@vmware.com> 4.4.74-1
-   [feature] 9P FS security support
-   [feature] DM Delay target support
-   Fix CVE-2017-1000364 ("stack clash") and CVE-2017-9605
*   Mon Jun 19 2017 Anish Swaminathan <anishs@vmware.com>  4.4.71-2
-   [feature] IPV6 netfilter NAT masquerade, security support
*   Wed Jun 7 2017 Alexey Makhalov <amakhalov@vmware.com> 4.4.71-1
-   Fix CVE-2017-8890, CVE-2017-9074, CVE-2017-9075, CVE-2017-9076
    CVE-2017-9077 and CVE-2017-9242
*   Tue Jun 6 2017 Alexey Makhalov <amakhalov@vmware.com> 4.4.70-3
-   [feature] IPV6 netfilter NAT table support
*   Fri May 26 2017 Alexey Makhalov <amakhalov@vmware.com> 4.4.70-2
-   Added ENA driver for AMI
*   Thu May 25 2017 Alexey Makhalov <amakhalov@vmware.com> 4.4.70-1
-   Fix CVE-2017-7487 and CVE-2017-9059
*   Tue May 9 2017 Alexey Makhalov <amakhalov@vmware.com> 4.4.67-1
-   Version update
-   Sign and compress modules after stripping. fips=1 requires signed modules
-   Removed version suffix from config file name
*   Tue May 2 2017 Alexey Makhalov <amakhalov@vmware.com> 4.4.65-1
-   Version update, remove upstreamed patches
-   Added crypto modules for NSX
-   Move linux-tools as a -tools subpackage
*   Thu Apr 27 2017 Alexey Makhalov <amakhalov@vmware.com> 4.4.64-1
-   Fix CVE-2017-7889
-   Fix Bug #1852790
*   Thu Apr 20 2017 Alexey Makhalov <amakhalov@vmware.com> 4.4.62-1
-   Fix CVE-2017-2671 and CVE-2017-7618
*   Mon Apr 10 2017 Alexey Makhalov <amakhalov@vmware.com> 4.4.60-1
-   Fix CVE-2017-7184, CVE-2017-7187, CVE-2017-7294,
    CVE-2017-7308 and CVE-2017-7346
*   Wed Mar 15 2017 Alexey Makhalov <amakhalov@vmware.com> 4.4.54-1
-   Update to linux-4.4.54 to fix CVE-2017-6346 and CVE-2017-6347
*   Thu Feb 23 2017 Alexey Makhalov <amakhalov@vmware.com> 4.4.51-1
-   Update to linux-4.4.51 and apply a patch to fix
    CVE-2017-5986 and CVE-2017-6074
*   Wed Feb 1 2017 Alexey Makhalov <amakhalov@vmware.com> 4.4.41-2
-   .config: added MODULES_SIG, CRYPTO_FIPS support.
*   Mon Jan 9 2017 Alexey Makhalov <amakhalov@vmware.com> 4.4.41-1
-   Update to linux-4.4.41
    to fix CVE-2016-10088, CVE-2016-9793 and CVE-2016-9576
*   Thu Dec  8 2016 Alexey Makhalov <amakhalov@vmware.com> 4.4.35-3
-   net-packet-fix-race-condition-in-packet_set_ring.patch
    to fix CVE-2016-8655
*   Wed Nov 30 2016 Alexey Makhalov <amakhalov@vmware.com> 4.4.35-2
-   Expand `uname -r` with release number
-   Check for build-id matching
-   Added syscalls tracing support
-   Compress modules
*   Mon Nov 28 2016 Alexey Makhalov <amakhalov@vmware.com> 4.4.35-1
-   Update to linux-4.4.35
-   vfio-pci-fix-integer-overflows-bitmask-check.patch
    to fix CVE-2016-9083
*   Tue Nov 22 2016 Alexey Makhalov <amakhalov@vmware.com> 4.4.31-4
-   net-9p-vsock.patch
*   Thu Nov 17 2016 Alexey Makhalov <amakhalov@vmware.com> 4.4.31-3
-   tty-prevent-ldisc-drivers-from-re-using-stale-tty-fields.patch
    to fix CVE-2015-8964
*   Tue Nov 15 2016 Alexey Makhalov <amakhalov@vmware.com> 4.4.31-2
-   .config: add cgrup_hugetlb support
-   .config: add netfilter_xt_{set,target_ct} support
-   .config: add netfilter_xt_match_{cgroup,ipvs} support
*   Thu Nov 10 2016 Alexey Makhalov <amakhalov@vmware.com> 4.4.31-1
-   Update to linux-4.4.31
*   Fri Oct 21 2016 Alexey Makhalov <amakhalov@vmware.com> 4.4.26-1
-   Update to linux-4.4.26
*   Wed Oct 19 2016 Alexey Makhalov <amakhalov@vmware.com> 4.4.20-6
-   net-add-recursion-limit-to-GRO.patch
-   scsi-arcmsr-buffer-overflow-in-arcmsr_iop_message_xfer.patch
*   Tue Oct 18 2016 Alexey Makhalov <amakhalov@vmware.com> 4.4.20-5
-   ipip-properly-mark-ipip-GRO-packets-as-encapsulated.patch
-   tunnels-dont-apply-GRO-to-multiple-layers-of-encapsulation.patch
*   Mon Oct  3 2016 Alexey Makhalov <amakhalov@vmware.com> 4.4.20-4
-   Package vmlinux with PROGBITS sections in -debuginfo subpackage
*   Tue Sep 27 2016 Alexey Makhalov <amakhalov@vmware.com> 4.4.20-3
-   .config: CONFIG_IP_SET_HASH_{IPMARK,MAC}=m
*   Tue Sep 20 2016 Alexey Makhalov <amakhalov@vmware.com> 4.4.20-2
-   Add -release number for /boot/* files
-   Use initrd.img with version and release number
*   Wed Sep  7 2016 Alexey Makhalov <amakhalov@vmware.com> 4.4.20-1
-   Update to linux-4.4.20
-   apparmor-fix-oops-validate-buffer-size-in-apparmor_setprocattr.patch
-   keys-fix-asn.1-indefinite-length-object-parsing.patch
*   Thu Aug 25 2016 Alexey Makhalov <amakhalov@vmware.com> 4.4.8-11
-   vmxnet3 patches to bumpup a version to 1.4.8.0
*   Wed Aug 10 2016 Alexey Makhalov <amakhalov@vmware.com> 4.4.8-10
-   Added VSOCK-Detach-QP-check-should-filter-out-non-matching-QPs.patch
-   .config: pmem hotplug + ACPI NFIT support
-   .config: enable EXPERT mode, disable UID16 syscalls
*   Thu Jul 07 2016 Alexey Makhalov <amakhalov@vmware.com> 4.4.8-9
-   .config: pmem + fs_dax support
*   Fri Jun 17 2016 Alexey Makhalov <amakhalov@vmware.com> 4.4.8-8
-   patch: e1000e-prevent-div-by-zero-if-TIMINCA-is-zero.patch
-   .config: disable rt group scheduling - not supported by systemd
*   Wed Jun 15 2016 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 4.4.8-7
-   fixed the capitalization for - System.map 
*   Thu May 26 2016 Alexey Makhalov <amakhalov@vmware.com> 4.4.8-6
-   patch: REVERT-sched-fair-Beef-up-wake_wide.patch
*   Tue May 24 2016 Priyesh Padmavilasom <ppadmavilasom@vmware.com> 4.4.8-5
-   GA - Bump release of all rpms
*   Mon May 23 2016 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 4.4.8-4
-   Fixed generation of debug symbols for kernel modules & vmlinux.
*   Mon May 23 2016 Divya Thaluru <dthaluru@vmware.com> 4.4.8-3
-   Added patches to fix CVE-2016-3134, CVE-2016-3135
*   Wed May 18 2016 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 4.4.8-2
-   Enabled CONFIG_UPROBES in config as needed by ktap
*   Wed May 04 2016 Alexey Makhalov <amakhalov@vmware.com> 4.4.8-1
-   Update to linux-4.4.8
-   Added net-Drivers-Vmxnet3-set-... patch
*   Tue May 03 2016 Vinay Kulkarni <kulkarniv@vmware.com> 4.2.0-27
-   Compile Intel GigE and VMXNET3 as part of kernel.
*   Thu Apr 28 2016 Nick Shi <nshi@vmware.com> 4.2.0-26
-   Compile cramfs.ko to allow mounting cramfs image
*   Tue Apr 12 2016 Vinay Kulkarni <kulkarniv@vmware.com> 4.2.0-25
-   Revert network interface renaming disable in kernel.
*   Tue Mar 29 2016 Alexey Makhalov <amakhalov@vmware.com> 4.2.0-24
-   Support kmsg dumping to vmware.log on panic
-   sunrpc: xs_bind uses ip_local_reserved_ports
*   Mon Mar 28 2016 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 4.2.0-23
-   Enabled Regular stack protection in Linux kernel in config
*   Thu Mar 17 2016 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 4.2.0-22
-   Restrict the permissions of the /boot/System.map-X file
*   Fri Mar 04 2016 Alexey Makhalov <amakhalov@vmware.com> 4.2.0-21
-   Patch: SUNRPC: Do not reuse srcport for TIME_WAIT socket.
*   Wed Mar 02 2016 Alexey Makhalov <amakhalov@vmware.com> 4.2.0-20
-   Patch: SUNRPC: Ensure that we wait for connections to complete
    before retrying
*   Fri Feb 26 2016 Alexey Makhalov <amakhalov@vmware.com> 4.2.0-19
-   Disable watchdog under VMware hypervisor.
*   Thu Feb 25 2016 Alexey Makhalov <amakhalov@vmware.com> 4.2.0-18
-   Added rpcsec_gss_krb5 and nfs_fscache
*   Mon Feb 22 2016 Alexey Makhalov <amakhalov@vmware.com> 4.2.0-17
-   Added sysctl param to control weighted_cpuload() behavior
*   Thu Feb 18 2016 Divya Thaluru <dthaluru@vmware.com> 4.2.0-16
-   Disabling network renaming
*   Sun Feb 14 2016 Alexey Makhalov <amakhalov@vmware.com> 4.2.0-15
-   veth patch: don’t modify ip_summed
*   Thu Feb 11 2016 Alexey Makhalov <amakhalov@vmware.com> 4.2.0-14
-   Full tickless -> idle tickless + simple CPU time accounting
-   SLUB -> SLAB
-   Disable NUMA balancing
-   Disable stack protector
-   No build_forced no-CBs CPUs
-   Disable Expert configuration mode
-   Disable most of debug features from 'Kernel hacking'
*   Mon Feb 08 2016 Alexey Makhalov <amakhalov@vmware.com> 4.2.0-13
-   Double tcp_mem limits, patch is added.
*   Wed Feb 03 2016 Anish Swaminathan <anishs@vmware.com>  4.2.0-12
-   Fixes for CVE-2015-7990/6937 and CVE-2015-8660.
*   Tue Jan 26 2016 Anish Swaminathan <anishs@vmware.com> 4.2.0-11
-   Revert CONFIG_HZ=250
*   Fri Jan 22 2016 Alexey Makhalov <amakhalov@vmware.com> 4.2.0-10
-   Fix for CVE-2016-0728
*   Wed Jan 13 2016 Alexey Makhalov <amakhalov@vmware.com> 4.2.0-9
-   CONFIG_HZ=250
*   Tue Jan 12 2016 Mahmoud Bassiouny <mbassiouny@vmware.com> 4.2.0-8
-   Remove rootfstype from the kernel parameter.
*   Mon Jan 04 2016 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 4.2.0-7
-   Disabled all the tracing options in kernel config.
-   Disabled preempt.
-   Disabled sched autogroup.
*   Thu Dec 17 2015 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 4.2.0-6
-   Enabled kprobe for systemtap & disabled dynamic function tracing in config
*   Fri Dec 11 2015 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 4.2.0-5
-   Added oprofile kernel driver sub-package.
*   Fri Nov 13 2015 Mahmoud Bassiouny <mbassiouny@vmware.com> 4.2.0-4
-   Change the linux image directory.
*   Wed Nov 11 2015 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 4.2.0-3
-   Added the build essential files in the dev sub-package.
*   Mon Nov 09 2015 Vinay Kulkarni <kulkarniv@vmware.com> 4.2.0-2
-   Enable Geneve module support for generic kernel.
*   Fri Oct 23 2015 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 4.2.0-1
-   Upgraded the generic linux kernel to version 4.2.0 & and updated timer handling to full tickless mode. 
*   Tue Sep 22 2015 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 4.0.9-5
-   Added driver support for frame buffer devices and ACPI
*   Wed Sep 2 2015 Alexey Makhalov <amakhalov@vmware.com> 4.0.9-4
-   Added mouse ps/2 module.
*   Fri Aug 14 2015 Alexey Makhalov <amakhalov@vmware.com> 4.0.9-3
-   Use photon.cfg as a symlink.
*   Thu Aug 13 2015 Alexey Makhalov <amakhalov@vmware.com> 4.0.9-2
-   Added environment file(photon.cfg) for grub.
*   Wed Aug 12 2015 Sharath George <sharathg@vmware.com> 4.0.9-1
-   Upgrading kernel version.
*   Wed Aug 12 2015 Alexey Makhalov <amakhalov@vmware.com> 3.19.2-5
-   Updated OVT to version 10.0.0.
-   Rename -gpu-drivers to -drivers-gpu in accordance to directory structure.
-   Added -sound package/
*   Tue Aug 11 2015 Anish Swaminathan<anishs@vmware.com> 3.19.2-4
-   Removed Requires dependencies. 
*   Fri Jul 24 2015 Harish Udaiya Kumar <hudaiyakumar@gmail.com> 3.19.2-3
-   Updated the config file to include graphics drivers.
*   Mon May 18 2015 Touseef Liaqat <tliaqat@vmware.com> 3.13.3-2
-   Update according to UsrMove.
*   Wed Nov 5 2014 Divya Thaluru <dthaluru@vmware.com> 3.13.3-1
-   Initial build. First version

