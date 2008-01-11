%define	name	gtkwave
%define	version 3.0.10
%define release %mkrel 2
%define Summary	GTKWave Electronic Waveform Viewer

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	%{Summary}
License: 	GPL
Group:		Sciences/Other
Source0:	http://home.nc.rr.com/gtkwave/%{name}-%{version}.tar.bz2
Source1:	%{name}-16.png.bz2
Source2:	%{name}-32.png.bz2
Source3:	%{name}-48.png.bz2
Patch0:		gtkwave-3.0.10-use-system-libs.patch
URL:		http://home.nc.rr.com/gtkwave/index.html
BuildRequires:	gtk+2-devel
BuildRequires:	libxml2-devel
BuildRequires:	flex bzip2-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
GTKWave is a fully featured GTK+ based wave viewer for Unix and Win32 
which reads LXT, LXT2, VZT, and GHW files as well as standard Verilog 
VCD/EVCD files and allows their viewing. 

%prep
%setup -q 
bzcat %{SOURCE1} > %{name}-16.png
bzcat %{SOURCE2} > %{name}-32.png
bzcat %{SOURCE3} > %{name}-48.png
sed -i 's|$(bindir)|$(DESTDIR)/$(bindir)|g' Makefile.in
sed -i 's|$(mandir)|$(DESTDIR)/$(mandir)|g' Makefile.in
%patch0 -p1 -b .system-libs
rm -fr src/libz src/libbz2

%build
%configure <<EOF
2
EOF

make libdir=%_libdir

%install
rm -rf %{buildroot}
%makeinstall_std
%{find_lang} %{name}

# icons
install -D -m 644 %{name}-16.png %{buildroot}%{_miconsdir}/%{name}.png 
install -D -m 644 %{name}-32.png %{buildroot}%{_iconsdir}/%{name}.png 
install -D -m 644 %{name}-48.png %{buildroot}%{_liconsdir}/%{name}.png

# menu entry

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=GTKWave
Comment=%{Summary}
Exec=%{_bindir}/%{name} -n foo
Icon=%{name}.png
Terminal=false
Type=Application
StartupNotify=true
Categories=X-MandrivaLinux-MoreApplications-Sciences-Other;Engineering;
EOF

# fix conflict with vertex
mv %{buildroot}%{_bindir}/vertex{,.gtkwave}
mv %{buildroot}%{_mandir}/man1/vertex.1 \
    %{buildroot}%{_mandir}/man1/vertex.gtkwave.1

%clean
rm -rf %{buildroot}

%post
%{update_menus}

%postun
%{clean_menus}

%files -f %{name}.lang
%defattr(-, root, root)
%doc *.TXT doc examples
%{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/man5/*
%{_datadir}/applications/%{name}.desktop

%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png

