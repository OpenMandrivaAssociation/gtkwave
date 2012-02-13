%define	name	gtkwave
%define	version 3.3.31
%define release 1
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
URL:		http://gtkwave.sourceforge.net/
BuildRequires:	gtk+2-devel
BuildRequires:	libxml2-devel
BuildRequires:	flex
BuildRequires:	gperf
BuildRequires:	bzip2-devel
BuildRequires:	zlib-devel
BuildRequires:	xz
BuildRequires:	lzma-devel
BuildRequires:	tk-devel
BuildRequires:	tcl-devel

%description
GTKWave is a fully featured GTK+ based wave viewer for Unix and Win32 
which reads LXT, LXT2, VZT, and GHW files as well as standard Verilog 
VCD/EVCD files and allows their viewing. 

%prep
%setup -q

%build
%configure2_5x
%make

%install
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

