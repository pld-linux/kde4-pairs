%define		_state		stable
%define		orgname		pairs

Summary:	K Desktop Environment - A game to enhance your memory
Summary(pl_PL.UTF8):	K Desktop Environment - Gra rozwijająca pamięć
Name:		kde4-pairs
Version:	4.9.0
Release:	1
License:	GPL
Group:		X11/Applications/Science
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.bz2
# Source0-md5:	ff50aa491f4f334e80a958e126e548a1
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

%find_lang %{orgname} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{orgname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pairs
%{_datadir}/apps/pairs
%{_datadir}/config.kcfg/pairs.kcfg
%{_datadir}/config/pairs.knsrc
%{_desktopdir}/kde4/pairs.desktop
%{_iconsdir}/hicolor/scalable/apps/pairs.svgz
%{_iconsdir}/hicolor/*x*/apps/pairs.png
%{_mandir}/man6/pairs.6*
