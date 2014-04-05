# TODO
# - unpackaged
#        /usr/lib64/silicon/plugins/libCdRecord.so
#        /usr/lib64/silicon/plugins/libFUseIso.so
#        /usr/lib64/silicon/plugins/libMkDiscFs.so
#        /usr/lib64/silicon/plugins/libMkIsoFs.so
Summary:	Disc burning application
Name:		silicon
Version:	2.0.0
Release:	0.4
License:	GPL v3
Group:		X11/Applications
Source0:	http://getsilicon.org/download/%{name}_%{version}_source.tar.gz
# Source0-md5:	f68fde5d5fd72c8e271b885e64ce7a5a
URL:		http://getsilicon.org/
Patch0:		splugin-lyricbrowser.patch
Patch1:		qtlocalpeer.patch
BuildRequires:	cmake
BuildRequires:	libstdc++-devel
BuildRequires:	qt4-build
BuildRequires:	taglib-devel
Requires:	desktop-file-utils
Requires:	dvd+rw-tools
Requires:	mkisofs
Requires:	mpg123
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Silicon Empire is set of tools to Burn, Copy, Backup and Manage your
optical discs like CDs, DVDs and Blu-Rays.

%package audio-disc
Summary:	Silicon audio disc
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}

%description audio-disc
Silicon application to create Audio discs:
- CDs
- DVDs
- Blu-Rays

%package converter
Summary:	Silicon converter
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}

%description converter
Silicon application to convert your files to other supported formats.

%package copy-disc
Summary:	Silicon copy disc
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}

%description copy-disc
Silicon application to copy a disc to another disc.

%package database
Summary:	Silicon database
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}

%description database
Silicon application to show informations and indexed data that
DiscScanner stored into the Silicon DataBase.

%package data-disc
Summary:	Silicon data disc
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}

%description data-disc
Silicon application to burn data discs or to create data images.

%package disc-details
Summary:	Silicon disc details
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}

%description disc-details
Silicon application to show disc, image or database disc details.

%package disc-eraser
Summary:	Silicon disc eraser
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}

%description disc-eraser
Silicon application to erase rw discs.

%package disc-imaging
Summary:	Silicon disc imaging
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}

%description disc-imaging
Silicon application to create images of your discs.

%package disc-scanner
Summary:	Silicon disc scanner
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}

%description disc-scanner
Silicon application to collect data from your discs to the Silicon
DataBase.

%package image-burner
Summary:	Silicon app image burner
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}

%description image-burner
Silicon application to burn a images to discs.

%package library
Summary:	Silicon app library
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}

%description library
Silicon application to manage your iso images in a classic way.

%package limoo
Summary:	Silicon app limoo
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}

%description limoo
Silicon application - Limoo image viewer.

%package mounter
Summary:	Silicon app mounter
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}

%description mounter
Silicon application to mount/umount images easily.

%package sample-app
Summary:	Silicon sample app
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}

%description sample-app
Silicon sample application

%package script-runner
Summary:	Silicon app script runner
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}

%description script-runner
%{summary}

%package tagarg-player
Summary:	Silicon app tagarg player
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}

%description tagarg-player
Silicon music player.

%package themes
Summary:	Silicon themes
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description themes
%{summary}

%package plugin-lyric-browser
Summary:	Silicon lyric browser plugin
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}

%description plugin-lyric-browser
%{summary}

%package plugin-now-playing
Summary:	Silicon now playing plugin
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}

%description plugin-now-playing
%{summary}

%package plugin-single-inner-dialog
Summary:	Silicon single inner dialog plugin
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}

%description plugin-single-inner-dialog
%{summary}

%package plugin-system-tray
Summary:	Silicon system tray plugin
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}

%description plugin-system-tray
%{summary}

%package plugin-tagarg-audio-disc
Summary:	Silicon tagarg audio disc plugin
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}

%description plugin-tagarg-audio-disc
%{summary}

%prep
%setup -q -n %{name}-empire
%patch0 -p1
%patch1 -p1

%build
cd src
install -d build
cd build
%cmake ..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C src/build install \
	DESTDIR=$RPM_BUILD_ROOT

desktop-file-validate $RPM_BUILD_ROOT%{_desktopdir}/%{name}.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database

%postun
%update_desktop_database

%files
%defattr(644,root,root,755)
%doc README Authors
%attr(755,root,root) %{_bindir}/%{name}
%attr(755,root,root) %{_libdir}/libSDataBase.so
%attr(755,root,root) %{_libdir}/libSiDi.so
%attr(755,root,root) %{_libdir}/libSiliconLib.so
%{_desktopdir}/silicon.desktop
%{_pixmapsdir}/%{name}.png
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/apps
%dir %{_libdir}/%{name}/plugins
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/languages
%dir %{_datadir}/%{name}/themes
%lang(de) %{_datadir}/%{name}/languages/lang-de.qm
%lang(en) %{_datadir}/%{name}/languages/lang-en.qm
%lang(es) %{_datadir}/%{name}/languages/lang-es.qm
%lang(fa) %{_datadir}/%{name}/languages/lang-fa.qm
%lang(zh_TW) %{_datadir}/%{name}/languages/lang-zh_TW.qm

%files audio-disc
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/apps/libAudioDisc.so

%files converter
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/apps/libConverter.so

%files copy-disc
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/apps/libCopyDisc.so

%files database
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/apps/libDataBase.so

%files data-disc
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/apps/libDataDisc.so

%files disc-details
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/apps/libDiscDetails.so

%files disc-eraser
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/apps/libDiscEraser.so

%files disc-imaging
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/apps/libDiscImaging.so

%files disc-scanner
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/apps/libDiscScanner.so

%files image-burner
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/apps/libImageBurner.so

%files library
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/apps/libLibrary.so

%files limoo
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/apps/libLimoo.so

%files mounter
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/apps/libMounter.so

%files sample-app
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/apps/libSampleApp.so

%files script-runner
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/apps/libScriptRunner.so

%files tagarg-player
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/apps/libTagargPlayer.so

%files themes
%defattr(644,root,root,755)
%{_datadir}/%{name}/themes/*

%files plugin-lyric-browser
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/libLyricBrowser.so

%files plugin-now-playing
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/libNowPlaying.so

%files plugin-single-inner-dialog
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/libSingleInnerDialog*.so

%files plugin-system-tray
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/libSystemTray.so

%files plugin-tagarg-audio-disc
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/libTagargAudioDisc.so
