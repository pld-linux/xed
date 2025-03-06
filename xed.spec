Summary:	Xed Text Editor
Summary(pl.UTF-8):	Edytor tekstu Xed
Name:		xed
Version:	3.8.2
Release:	1
License:	GPL v2+ (Xed), GPL v3+ (open-uri-context-menu plugin)
Group:		X11/Applications/Editors
#Source0Download: https://github.com/linuxmint/xed/tags
Source0:	https://github.com/linuxmint/xed/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	38bb32da6cba4b248f2bcd4b32848968
URL:		https://github.com/linuxmint/xed
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gettext-tools >= 0.19.8
BuildRequires:	glib2-devel >= 1:2.40.0
BuildRequires:	gobject-introspection-devel >= 1.42.0
BuildRequires:	gspell-devel >= 0.2.5
BuildRequires:	gtk+3-devel >= 3.19.3
BuildRequires:	gtk-doc >= 1.0
BuildRequires:	gtksourceview4-devel >= 4.0.3
BuildRequires:	intltool
BuildRequires:	itstool
BuildRequires:	libpeas-devel >= 1.12.0
BuildRequires:	libpeas-gtk-devel >= 1.12.0
BuildRequires:	libsoup-devel >= 2.4
BuildRequires:	libxml2-devel >= 1:2.5.0
BuildRequires:	meson
BuildRequires:	ninja >= 1.5
BuildRequires:	pango-devel
BuildRequires:	pkgconfig
BuildRequires:	python3-devel >= 1:3
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(find_lang) >= 1.36
BuildRequires:	rpmbuild(macros) >= 2.042
BuildRequires:	sed >= 4.0
BuildRequires:	xapps-devel >= 1.9.0
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	yelp-tools
Requires(post,postun):	glib2 >= 1:2.40.0
Requires:	glib2 >= 1:2.40.0
Requires:	gobject-introspection >= 1.42.0
Requires:	gspell >= 0.2.5
Requires:	gtk+3 >= 3.19.3
Requires:	gtksourceview4 >= 4.0.3
Requires:	libpeas >= 1.12.0
Requires:	libpeas-gtk >= 1.12.0
Requires:	libxml2 >= 1:2.5.0
Requires:	python3-pygobject3 >= 3.0
Requires:	xapps-libs >= 1.9.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Xed is a small and lightweight text editor. It supports most standard
editing features, plus several not found in your average text editor
(plugins being the most notable of these).

%description -l pl.UTF-8
Xed to mały i lekki edytor tekstu. Obsługuje większość standardowych
funkcji edytorskich plus kilka nie spotykanych w przeciętnym edytorze
(najbardziej widoczna to wtyczki).

%package devel
Summary:	Header files for Xed plugins development
Summary(pl.UTF-8):	Pliki nagłówkowe do tworzenia wtyczek edytora Xed
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 1:2.40.0
Requires:	gtk+3-devel >= 3.19.3
Requires:	gtksourceview4-devel >= 4.0.3
Requires:	libpeas-devel >= 1.12.0
Requires:	libpeas-gtk-devel >= 1.12.0
Requires:	libxml2-devel >= 1:2.5.0
Requires:	xapps-devel >= 1.9.0
Requires:	xorg-lib-libX11-devel

%description devel
Header files for Xed plugins development.

%description devel -l pl.UTF-8
Pliki nagłówkowe do tworzenia wtyczek edytora Xed.

%package apidocs
Summary:	Xed API documentation
Summary(pl.UTF-8):	Dokumentacja API edytora Xed
Group:		Documentation
BuildArch:	noarch

%description apidocs
Xed API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API edytora Xed.

%prep
%setup -q

%build
%meson \
	--default-library=shared \
	-Ddocs=true \
	-Denable_gvfs_metadata=true \
	-Denable_spell=true

%meson_build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/ie

%find_lang xed --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas

%postun
%glib_compile_schemas

%files -f xed.lang
%defattr(644,root,root,755)
%doc AUTHORS README.md debian/changelog
%attr(755,root,root) %{_bindir}/xed
%dir %{_libdir}/xed
%attr(755,root,root) %{_libdir}/xed/libxed.so
%dir %{_libdir}/xed/girepository-1.0
%{_libdir}/xed/girepository-1.0/Xed-1.0.typelib
%dir %{_libdir}/xed/plugins
%{_datadir}/dbus-1/services/org.x.editor.service
%{_datadir}/glib-2.0/schemas/org.x.editor.gschema.xml
%{_datadir}/gtksourceview-4/styles/xed.xml
%{_datadir}/metainfo/org.x.editor.metainfo.xml
%dir %{_datadir}/xed
%{_datadir}/xed/icons
%dir %{_datadir}/xed/plugins
%{_desktopdir}/org.x.editor.desktop
%{_mandir}/man1/xed.1*

# C plugins

%{_libdir}/xed/plugins/docinfo.plugin
%attr(755,root,root) %{_libdir}/xed/plugins/libdocinfo.so
%{_datadir}/xed/plugins/docinfo

%{_libdir}/xed/plugins/filebrowser.plugin
%attr(755,root,root) %{_libdir}/xed/plugins/libfilebrowser.so
%{_datadir}/glib-2.0/schemas/org.x.editor.plugins.filebrowser.gschema.xml
%{_datadir}/xed/plugins/filebrowser

%{_libdir}/xed/plugins/modelines.plugin
%attr(755,root,root) %{_libdir}/xed/plugins/libmodelines.so
%{_datadir}/xed/plugins/modelines

%{_libdir}/xed/plugins/sort.plugin
%attr(755,root,root) %{_libdir}/xed/plugins/libsort.so

%{_libdir}/xed/plugins/spell.plugin
%attr(755,root,root) %{_libdir}/xed/plugins/libspell.so
%{_datadir}/glib-2.0/schemas/org.x.editor.plugins.spell.gschema.xml
%{_datadir}/xed/plugins/spell

%{_libdir}/xed/plugins/taglist.plugin
%attr(755,root,root) %{_libdir}/xed/plugins/libtaglist.so
%{_datadir}/xed/plugins/taglist

%{_libdir}/xed/plugins/time.plugin
%attr(755,root,root) %{_libdir}/xed/plugins/libtime.so
%{_datadir}/glib-2.0/schemas/org.x.editor.plugins.time.gschema.xml
%{_datadir}/xed/plugins/time

%{_libdir}/xed/plugins/trailsave.plugin
%attr(755,root,root) %{_libdir}/xed/plugins/libtrailsave.so

%attr(755,root,root) %{_libdir}/xed/plugins/libwordcompletion.so
%{_libdir}/xed/plugins/wordcompletion.plugin
%{_datadir}/glib-2.0/schemas/org.x.editor.plugins.wordcompletion.gschema.xml
%{_datadir}/xed/plugins/wordcompletion

# Python plugins

%{_libdir}/xed/plugins/bracket-complete

%{_libdir}/xed/plugins/joinlines.plugin
%{_libdir}/xed/plugins/joinlines

%{_libdir}/xed/plugins/open-uri-context-menu

%{_libdir}/xed/plugins/textsize.plugin
%{_libdir}/xed/plugins/textsize

%files devel
%defattr(644,root,root,755)
%{_includedir}/xed
%dir %{_datadir}/xed/gir-1.0
%{_datadir}/xed/gir-1.0/Xed-1.0.gir
%{_pkgconfigdir}/xed.pc

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/xed
