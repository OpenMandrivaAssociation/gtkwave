%define _disable_ld_no_undefined 1

Name:		gtkwave
Version:	3.3.120
Release:	1
Summary:	Electronic Waveform Viewer
License:	GPLv2+
Group:		Sciences/Other
Source0:	http://gtkwave.sourceforge.net/gtkwave-gtk3-%{version}.tar.gz

URL:		http://gtkwave.sourceforge.net/
BuildRequires:	pkgconfig(gio-unix-2.0) >= 2.0
BuildRequires:	pkgconfig(gtk+-3.0) >= 3.0.0
BuildRequires:	pkgconfig(gtk+-unix-print-3.0)
BuildRequires:	pkgconfig(libtirpc)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	flex
BuildRequires:	gperf
BuildRequires:	pkgconfig(bzip2)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	lzma-devel
BuildRequires:	pkgconfig(tk)
BuildRequires:	pkgconfig(tcl)
BuildRequires:	judy-devel

Recommends:	gedit
Requires:	hicolor-icon-theme
Requires:	shared-mime-info

%description
GTKWave is a fully featured GTK+ based wave viewer for Unix and Win32 
which reads LXT, LXT2, VZT, and GHW files as well as standard Verilog 
VCD/EVCD files and allows their viewing. 

%prep
%setup -q -n gtkwave-gtk3-%{version}
 
%build
%configure \
	--disable-dependency-tracking \
	--disable-mime-update \
	--enable-gtk3 \
	--enable-judy \
	--with-gsettings \
 	--disable-tcl \
	--with-tirpc
%make_build
 
%install
make install \
	DESTDIR=%{buildroot} \
	pkgdatadir=%{_pkgdocdir} \
	INSTALL="install -p"



%files
%doc *.TXT doc examples
%{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/man5/*
%{_datadir}/icons/gnome/*/*
%{_datadir}/gtkwave
%{_datadir}/mime/packages/*
%{_datadir}/applications/%{name}.desktop
%{_miconsdir}/%{name}.png
%{_iconsdir}/*.png
%{_liconsdir}/%{name}.png



%changelog
* Fri Aug 03 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 3.3.38-2
+ Revision: 811665
- enale judy and struct packing

* Mon Jul 23 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 3.3.38-1
+ Revision: 810735
- update to 3.3.38

* Mon Feb 13 2012 Alexander Khrukin <akhrukin@mandriva.org> 3.3.31-1
+ Revision: 773796
- BR:tcl-devel
- version update 3.3.31

* Sat Jun 04 2011 Funda Wang <fwang@mandriva.org> 3.3.22-1
+ Revision: 682719
- new version 3.3.22

* Sat Apr 30 2011 Funda Wang <fwang@mandriva.org> 3.3.21-1
+ Revision: 661030
- update to new version 3.3.21

* Wed Mar 16 2011 StÃ©phane TÃ©letchÃ©a <steletch@mandriva.org> 3.3.20-1
+ Revision: 645234
- update to new version 3.3.20

* Sun Dec 26 2010 Funda Wang <fwang@mandriva.org> 3.3.18-1mdv2011.0
+ Revision: 625193
- update to new version 3.3.18

* Wed Dec 01 2010 Funda Wang <fwang@mandriva.org> 3.3.17-1mdv2011.0
+ Revision: 604306
- update to new version 3.3.17

* Sun Nov 28 2010 Funda Wang <fwang@mandriva.org> 3.3.16-1mdv2011.0
+ Revision: 602174
- update to new version 3.3.16

* Thu Nov 25 2010 Funda Wang <fwang@mandriva.org> 3.3.15-1mdv2011.0
+ Revision: 600924
- update to new version 3.3.15

* Sat Sep 25 2010 Funda Wang <fwang@mandriva.org> 3.3.13-1mdv2011.0
+ Revision: 580945
- update to new version 3.3.13

* Mon Aug 30 2010 Funda Wang <fwang@mandriva.org> 3.3.12-1mdv2011.0
+ Revision: 574254
- update to new version 3.3.12

* Sat Jul 17 2010 Funda Wang <fwang@mandriva.org> 3.3.10-1mdv2011.0
+ Revision: 554488
- new version 3.3.10

* Sun Mar 21 2010 Funda Wang <fwang@mandriva.org> 3.3.5-1mdv2010.1
+ Revision: 525968
- Br lzma
- update to new version 3.3.5

  + Sandro Cazzaniga <kharec@mandriva.org>
    - update to 3.3.4

  + Frederik Himpe <fhimpe@mandriva.org>
    - Fix BuildRequires
    - update to new version 3.3.3

* Mon Jan 11 2010 JÃ©rÃ´me Brenier <incubusss@mandriva.org> 3.3.2-2mdv2010.1
+ Revision: 489973
- bump release
- new version 3.3.2
- redo str fmt patch

* Tue Dec 29 2009 Funda Wang <fwang@mandriva.org> 3.3.0-1mdv2010.1
+ Revision: 483213
- new version 3.3.0

* Sun Nov 15 2009 Funda Wang <fwang@mandriva.org> 3.2.3-1mdv2010.1
+ Revision: 466156
- new version 3.2.3

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 3.0.10-4mdv2009.0
+ Revision: 246713
- rebuild
- fix 'error: for key "Icon" in group "Desktop Entry" is an icon name with an
  extension, but there should be no extension as described in the Icon Theme
  Specification if the value is not an absolute path'
- drop old menu

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Wed Jan 02 2008 Olivier Blin <blino@mandriva.org> 3.0.10-2mdv2008.1
+ Revision: 140744
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - import gtkwave


* Mon Aug 28 2006 Guillaume Rousse <guillomovitch@mandriva.org> 3.0.10-2mdv2007.0
- fix conflict with gtkwave

* Thu Aug 24 2006 Stew Benedict <sbenedict@mandriva.com> 3.0.10-1mdv2007.0
- 3.0.10, redo P0, xdg menu

* Thu May 25 2006 Stew Benedict <sbenedict@mandriva.com> 3.0.2-1mdv2007.0
- 3.0.2
- drop -devel package, use system zlib, libbz2 (P0), change menu entry

* Fri Aug 26 2005 Guillaume Rousse <guillomovitch@mandriva.org> 2.0.0-0.pre5.3mdk
- fix build 
- fix menu entry
- fix libtool file perms
- less strict requires

* Thu Jul 28 2005 Guillaume Rousse <guillomovitch@mandriva.org> 2.0.0-0.pre5.2mdk 
- spec cleanup

* Wed Jul 21 2004 Guillaume Rousse <guillomovitch@mandrake.org> 2.0.0-0.pre5.1mdk
- new version
- rpmbuildupdate aware
- fixed menu category
- fixed buildrequires
- devel subpackage

* Tue Jul 15 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 2.0.0-0.pre3.3mdk
- rebuild

* Tue Jun 24 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 2.0.0-0.pre3.2mdk
- fix group
- rm -rf %%{buildroot} in %%install, not %%prep
- change summary macro to avoid conflicts with -debug package
- updated url
- quiet setup
- buildrequires

* Sat Feb 08 2003 Guillaume Rousse <g.rousse@linux-mandrake.com> 2.0.0-0.pre3.1mdk
- first Mandrake release

