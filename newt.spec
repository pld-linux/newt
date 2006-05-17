#
# Conditional build:
%bcond_without	python	# don't build Python module
%bcond_without	tcl	# build Tcl module
#
Summary:	Not Erik's Windowing Toolkit - text mode windowing with slang
Summary(de):	Nicht Eriks Windowing Toolkit - Textmodus-Windowing mit Slang
Summary(fr):	Not Erik's Windowing Toolkit - fenêtrage en mode texte avec slang
Summary(pl):	Not Erik's Windowing Toolkit - okna w trybie tekstowym ze slangiem
Summary(tr):	Not Erik's Windowing Toolkit - metin kipi pencereleme sistemi
Name:		newt
Version:	0.52.2
Release:	1
License:	LGPL
Group:		Libraries
# http://download.fedora.redhat.com/pub/fedora/linux/core/development/SRPMS/
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	3ab21d288fc156a29519cc3e6db57961
Patch0:		%{name}-textbox.patch
Patch1:		%{name}-install_sh.patch
Patch2:		%{name}-0.51.6-if1close.patch
Patch3:		%{name}-PIC.patch
Patch4:		%{name}-gcc34.patch
Patch5:		%{name}-nopython.patch
URL:		http://www.msg.com.mx/Newt/
BuildRequires:	autoconf
BuildRequires:	docbook-utils
BuildRequires:	popt-devel
%{?with_python:BuildRequires:	python-devel >= 2.2}
BuildRequires:	rpm-pythonprov
#BuildRequires:	sgml-tools
BuildRequires:	slang-devel >= 2.0.0
%{?with_tcl:BuildRequires:	tcl-devel >= 8.3.2}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Newt is a windowing toolkit for text mode built from the slang
library. It allows color text mode applications to easily use
stackable windows, push buttons, check boxes, radio buttons, lists,
entry fields, labels, and displayable text. Scrollbars are supported,
and forms may be nested to provide extra functionality. This pacakge
contains the shared library for programs that have been built with
newt.

%description -l de
Newt ist ein Windowing-Toolkit für Textmodus, konstruiert auf der
Grundlage der Slang-Library, mit dessen Hilfe Farbtext-Modus-
Applikationen leicht mit stapelbaren Fenstern, Schaltflächen,
Optionskästchen, Listen, Eingabefeldern, Etiketten und Display-Text
arbeiten können. Auch Bildlaufleisten erden unterstützt, und der
Einbau von Formularen ist möglich, wenn zusätzliche Funktionalität
gefordert ist.

%description -l fr
Newt est une boite à outil de fenétrage en mode texte, construit sur
la librarie slang. Elle permet aux applications en mode texte
d'utiliser simplement de multiples fenêtres, des bouttons, des cases à
cocher... Les barres de défilement sont supportées, et les fenêtres
peuvent être imbriquées pour donner des fonctionnalités nouvelles.

%description -l pl
Newt jest bibliotek± typu toolkit ale do trybu tekstowego, osadzon± na
bibliotece slang. Umo¿liwia budowanie aplikacji pracuj±cych w trybie
tekstowym umo¿liwiaj±c operowanie na okienkach, przyciskach (push
button), listach wyboru, etykietach i elementach tekstowych jakie s±
potrzebne przy tworzeniu interfejsu u¿ytkownika w ró¿nych aplikacjach.

%description -l tr
Newt ile karakter tabanlý ekranlarda renkli pencereler, kaydýrma
çubuklarý, çeþitli tuþlar oluþturulabilir.

%package devel
Summary:	Developer's toolkit for newt windowing library
Summary(de):	Entwickler-Toolkit für die newt-Windowing-Library
Summary(fr):	Toolkit de développement pour la bibliothèque de fenêtrage newt
Summary(pl):	Pliki nag³ówkowe dla newt
Summary(tr):	newt pencere kitaplýðý için geliþtirme dosyalarý
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
These are the header files and libraries for developing applications
which use newt. Newt is a windowing toolkit for text mode, which
provides many widgets and stackable windows.

%description devel -l de
Dies sind die Header-Dateien und Libraries zur Entwicklung von
Applikationen, die mit newt arbeiten. Newt ist ein Windowing-Toolkit
für Textmodus, der viele Widgets und stapelbare Fenster enthält.

%description devel -l fr
En-têtes et bibliothèques pour le développement d'applications
utilisant newt. newt est un tookit de fenêtrage pour le mode texte
offrant de nombreux widgets et des fenêtres empilables.

%description devel -l pl
Pliki nag³ówkowe dla newt.

%description devel -l tr
Bu paket, newt ile geliþtirme yapmak için gereken baþlýk dosyalarýný
ve kitaplýklarý içerir. Newt, metin ekranda çalýþan bir pencereleme
kitaplýðýdýr.

%package static
Summary:	Newt static library
Summary(pl):	Biblioteka statyczna newt
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Newt static library.

%description static -l pl
Biblioteka statyczna newt.

%package tcl
Summary:	Newt Tcl bindings
Summary(pl):	Dodatki do Tcl z Newta
Group:		Development/Languages/Tcl
Requires:	%{name} = %{version}-%{release}

%description tcl
Newt Tcl bindings.

%description tcl -l pl
Dodatki do Tcl z Newta.

%package -n python-snack
Summary:	Newt python bindings
Summary(pl):	Dodatki do pythona z Newta
Group:		Development/Languages/Python
%pyrequires_eq	python
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-python = %{version}-%{release}
Provides:	snack = %{version}-%{release}
Obsoletes:	newt-python

%description -n python-snack
Newt python bindings

%description -n python-snack -l pl
Dodatki do pythona z Newta.

%package -n whiptail
Summary:	A dialog compliant program to build tty dialog boxes
Summary(pl):	Program do tekstowych okienek dialogowych kompatybilny z dialog
Group:		Applications/Terminal

%description -n whiptail
Dialog compliant utility that allows you to build user interfaces in a
TTY (text mode only). You can call dialog from within a shell script
to ask the user questions or present with choices in a more user
friendly manner.

%description -n whiptail -l pl
Program umo¿liwiaj±cy budowaæ interfejsy u¿ytkownika na terminalu
tekstowym, kompatybilny z programem dialog. Pozwala wywo³aæ dialog ze
skryptu shella, aby zdaæ pytania u¿ytkownikowi w sposób bardziej
przyjazny.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

sed -i -e 's#gcc#%{__cc}#g' Makefile.in

%build
%{__autoconf}
%configure \
	--enable-gpm-support

%{__make} \
	CC="%{__cc}" \
	PROGS="whiptail %{?with_tcl:whiptcl.so} testgrid" \
	%{!?with_python:SNACKSO=}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	%{?with_tcl:WHIPTCLSO=whiptcl.so} \
	%{!?with_python:SNACKSO=} \
	instroot=$RPM_BUILD_ROOT \
	libdir=%{_libdir} \
	pythondir=%{py_sitedir} \
	pythonbindir=%{py_sitedir}

#it just plain doesn't work... fix it if you can
#sgml2txt tutorial.sgml

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so.*.*

%files -n whiptail
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/whiptail

%if %{with tcl}
%files tcl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*tcl.so
%endif

%if %{with python}
%files -n python-snack
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/*.so
%{py_sitedir}/*.py
%endif

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
