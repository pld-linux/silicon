Summary:	Disc burning application
Name:		silicon
Version:	2.0.0
Release:	0.6
License:	GPL v3
Group:		X11/Applications
Source0:	http://getsilicon.org/download/%{name}_%{version}_source.tar.gz
# Source0-md5:	f68fde5d5fd72c8e271b885e64ce7a5a
URL:		http://getsilicon.org/
Patch0:		splugin-lyricbrowser.patch
Patch1:		qtlocalpeer.patch
BuildRequires:	QtCore-devel
BuildRequires:	QtDBus-devel
BuildRequires:	QtDeclarative-devel
BuildRequires:	QtGui-devel
BuildRequires:	QtNetwork-devel
BuildRequires:	QtSql-devel
BuildRequires:	QtTest-devel
BuildRequires:	cmake
BuildRequires:	desktop-file-utils
BuildRequires:	libstdc++-devel
BuildRequires:	phonon-devel
BuildRequires:	qt4-build
BuildRequires:	qt4-linguist
BuildRequires:	taglib-devel
Requires:	desktop-file-utils
Requires:	dvd+rw-tools
Requires:	mkisofs
Suggests:	mpg123
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Silicon Empire is set of tools to Burn, Copy, Backup and Manage your
optical discs like CDs, DVDs and Blu-Rays.

%package apps
Summary:	Apps for Silicon Empire
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Obsoletes:	silicon-audio-disc
Obsoletes:	silicon-converter
Obsoletes:	silicon-copy-disc
Obsoletes:	silicon-data-disc
Obsoletes:	silicon-database
Obsoletes:	silicon-disc-details
Obsoletes:	silicon-disc-eraser
Obsoletes:	silicon-disc-imaging
Obsoletes:	silicon-disc-scanner
Obsoletes:	silicon-image-burner
Obsoletes:	silicon-library
Obsoletes:	silicon-limoo
Obsoletes:	silicon-mounter
Obsoletes:	silicon-sample-app
Obsoletes:	silicon-script-runner
Obsoletes:	silicon-tagarg-player

%description apps
Applications for Silicon Empire:
- converter: convert your files to other supported formats.
- copy-disc: copy a disc to another disc.
- database: show information and indexed data that DiscScanner stored
  into the Silicon DataBase.
- data-disc: burn data discs or to create data images.
- disc-details: show disc, image or database disc details.
- disc-eraser: erase rw discs.
- disc-imaging: create images of your discs.
- disc-scanner: collect data from your discs to the Silicon DataBase.
- image-burner: burn a images to discs.
- library: manage your iso images in a classic way.
- limoo: Limoo image viewer.
- mounter: mount/umount images easily.
- script-runner: script runner
- tagarg-player: tagarg player

%package plugins
Summary:	Plugins for Silicon Empire
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Obsoletes:	silicon-plugin-lyric-browser
Obsoletes:	silicon-plugin-now-playing
Obsoletes:	silicon-plugin-single-inner-dialog
Obsoletes:	silicon-plugin-system-tray
Obsoletes:	silicon-plugin-tagarg-audio-disc

%description plugins
Plugins for Silicon Empire Application:
- lyric-browser: lyric browser plugin
- now-playing: now playing plugin
- single-inner-dialog: single inner dialog plugin
- system-tray: system tray plugin
- tagarg-audio-disc: tagarg audio disc plugin

%package themes
Summary:	Silicon themes
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description themes
Silicon themes.

%prep
%setup -q -n %{name}-empire
%patch0 -p1
%patch1 -p1

%build
cd src
install -d build
cd build
%cmake .. \
	-DMPG123_FOUND=/usr/bin/mpg123 \
	-DMPG321_FOUND=/usr/bin/mpg321 \
	-DWODIM_FOUND=/usr/bin/wodim \
	-DCDRECORD_FOUND=/usr/bin/cdrecord \
	-DMKISOFS_FOUND=/usr/bin/mkisofs \
	-DGENISOIMAGE_FOUND=/usr/bin/genisoimage \
	-DREADCD_FOUND=/usr/bin/readcd \
	-DREADOM_FOUND=/usr/bin/readom \
	-DUDISKS_FOUND=/usr/bin/udisks \
	-DFUSEISO_FOUND=/usr/bin/fuseiso \
	-DDVD_FORMAT_FOUND=/usr/bin/dvd+rw-format \
	-DPOLKIT_FOUND=/usr/bin/pkexec \

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

%files apps
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/apps/libAudioDisc.so
%attr(755,root,root) %{_libdir}/%{name}/apps/libConverter.so
%attr(755,root,root) %{_libdir}/%{name}/apps/libCopyDisc.so
%attr(755,root,root) %{_libdir}/%{name}/apps/libDataBase.so
%attr(755,root,root) %{_libdir}/%{name}/apps/libDataDisc.so
%attr(755,root,root) %{_libdir}/%{name}/apps/libDiscDetails.so
%attr(755,root,root) %{_libdir}/%{name}/apps/libDiscEraser.so
%attr(755,root,root) %{_libdir}/%{name}/apps/libDiscImaging.so
%attr(755,root,root) %{_libdir}/%{name}/apps/libDiscScanner.so
%attr(755,root,root) %{_libdir}/%{name}/apps/libImageBurner.so
%attr(755,root,root) %{_libdir}/%{name}/apps/libLibrary.so
%attr(755,root,root) %{_libdir}/%{name}/apps/libLimoo.so
%attr(755,root,root) %{_libdir}/%{name}/apps/libMounter.so
%attr(755,root,root) %{_libdir}/%{name}/apps/libSampleApp.so
%attr(755,root,root) %{_libdir}/%{name}/apps/libScriptRunner.so
%attr(755,root,root) %{_libdir}/%{name}/apps/libTagargPlayer.so

%files plugins
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/libAudioCdRecord.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/libCdRecord.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/libEraser.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/libFUseIso.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/libLyricBrowser.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/libMkDiscFs.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/libMkIsoFs.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/libNowPlaying.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/libReadCd.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/libSingleInnerDialog*.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/libUDisks.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/libmpg123.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/libmpg321.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/libSystemTray.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/libTagargAudioDisc.so

%files themes
%defattr(644,root,root,755)
%{_datadir}/%{name}/themes/*
