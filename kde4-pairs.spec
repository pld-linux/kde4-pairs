%define		_state		stable
%define		orgname		pairs

Summary:	K Desktop Environment - A game to enhance your memory
Summary(pl.UTF-8):	K Desktop Environment - Gra rozwijająca pamięć
Name:		kde4-pairs
Version:	4.13.1
Release:	1
License:	GPL
Group:		X11/Applications/Science
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	86de6f75abf97f3dbff920408aa8f4c3
URL:		http://www.kde.org/
BuildRequires:	kde4-kdelibs-devel >= %{version}
BuildRequires:	kde4-libkdeedu-devel >= %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pairs - a game to enhance your memory.

%description -l pl.UTF-8
Pairs - gra rozwijająca pamięć.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build/ install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

%find_lang	pairseditor	--with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f pairseditor.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pairs
%attr(755,root,root) %{_bindir}/pairseditor
%{_datadir}/apps/pairs
%{_datadir}/apps/pairseditor
%{_datadir}/config/pairs.knsrc
%{_desktopdir}/kde4/pairs.desktop
%{_desktopdir}/kde4/pairseditor.desktop
%{_iconsdir}/hicolor/scalable/apps/pairs.svgz
%{_iconsdir}/hicolor/scalable/apps/pairseditor.svgz
%{_iconsdir}/hicolor/*x*/apps/pairs.png
%{_iconsdir}/hicolor/*x*/apps/pairseditor.png
