%define	name	gtkwave
%define	version 3.3.21
%define release %mkrel 1
%define Summary	GTKWave Electronic Waveform Viewer

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	%{Summary}
License: 	GPLv2+
Group:		Sciences/Other
Source0:	http://gtkwave.sourceforge.net/%name-%version.tar.gz
Source1:	%{name}-16.png
Source2:	%{name}-32.png
Source3:	%{name}-48.png
Patch0:		gtkwave-3.3.10-fix-str-fmt.patch
URL:		http://gtkwave.sourceforge.net/
BuildRequires:	gtk+2-devel
BuildRequires:	libxml2-devel
BuildRequires:	flex
BuildRequires:	gperf
BuildRequires:	bzip2-devel
BuildRequires:	zlib-devel
BuildRequires:	xz
BuildRequires:	lzma-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
GTKWave is a fully featured GTK+ based wave viewer for Unix and Win32 
which reads LXT, LXT2, VZT, and GHW files as well as standard Verilog 
VCD/EVCD files and allows their viewing. 

%prep
%setup -q
%patch0 -p1

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

# icons
install -D -m 644 %{SOURCE1} %{buildroot}%{_miconsdir}/%{name}.png
install -D -m 644 %{SOURCE2} %{buildroot}%{_iconsdir}/%{name}.png
install -D -m 644 %{SOURCE3} %{buildroot}%{_liconsdir}/%{name}.png

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=GTKWave
Comment=GTKWave Electronic Waveform Viewer
Exec=%{_bindir}/%{name} -n foo
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=GTK;Engineering;
EOF

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif

%files
%defattr(-, root, root)
%doc *.TXT doc examples
%{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/man5/*
%{_datadir}/gtkwave
%{_datadir}/applications/%{name}.desktop
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png

