Summary:	Not Erik's Windowing Toolkit - text mode windowing with slang
Summary(de):	Nicht Eriks Windowing Toolkit - Textmodus-Windowing mit Slang 
Summary(fr):	Not Erik's Windowing Toolkit - fenêtrage en mode texte avec slang
Summary(pl):	Not Erik's Windowing Toolkit - okna w trybie tekstowym ze slangiem
Summary(tr):	Not Erik's Windowing Toolkit - metin kipi pencereleme sistemi
Name:		newt
Version:	0.50
Release:	16
License:	LGPL
Group:		Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
Source0:	ftp://ftp.redhat.com/pub/redhat/code/newt/%{name}-%{version}.tar.gz
Patch0:		newt-pythondirs.patch
BuildRequires:	slang-devel
BuildRequires:	tcl-devel
BuildRequires:	python-devel >= 1.6b1
BuildRequires:	popt-devel
BuildRequires:	sgml-tools
Provides:	dialog
Obsoletes:	dialog
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
Newt jest bibliotek± typu toolkit ale to trybu tekstowego osadzon± na
bibliotece slang. Umo¿liwia budowanie aplikacji pracuj±cych w trybie
tekstowym umo¿liwij±c operowanie na okienkach, przyciskach (push
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
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
These are the header files and libraries for developing applications
which use newt. Newt is a windowing toolkit for text mode, which
provides many widgets and stackable windows.

%description -l de devel
Dies sind die Header-Dateien und Libraries zur Entwicklung von
Applikationen, die mit newt arbeiten. Newt ist ein Windowing-Toolkit
für Textmodus, der viele Widgets und stapelbare Fenster enthält.

%description -l fr devel
En-têtes et bibliothèques pour le développement d'applications
utilisant newt. newt est un tookit de fenêtrage pour le mode texte
offrant de nombreux widgets et des fenêtres empilables.

%description -l pl devel
Pliki nag³ówkowe dla newt.

%description -l tr devel
Bu paket, newt ile geliþtirme yapmak için gereken baþlýk dosyalarýný
ve kitaplýklarý içerir. Newt, metin ekranda çalýþan bir pencereleme
kitaplýðýdýr.

%package static
Summary:	Newt static library
Summary(pl):	Biblioteka statyczna newt
Group:		Development/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
Newt static library.

%description -l pl static
Biblioteka statyczna newt.

%package tcl
Summary:	Newt Tcl bindings
Summary(pl):	Dodatki do Tcl z Newt'a
Group:		Development/Languages/Tcl
Group(pl):	Programowanie/Jêzyki/Tcl
Requires:	%{name} = %{version}

%description tcl
Newt Tcl bindings.

%description -l pl tcl 
Dodatki do Tcl z Newt'a

%package python
Summary:	Newt python bindings
Summary(pl):	Dodatki do python'a z Newt'a
Group:		Development/Languages/Python
Group(pl):	Programowanie/Jêzyki/Python
Requires:	%{name} = %{version}
Requires:	python >= 1.5
Provides:	snack

%description python
Newt python bindings

%description python -l pl
Dodatki do python'a z Newt'a.

%package -n whiptail
Summary:	A dialog compliant program to build tty dialog boxes
Group:          Utilities/Terminal
Group(pl):      Narzêdzia/Terminal

%description -n whiptail
Dialog compliant utility that allows you to build user interfaces in a TTY 
(text mode only). You can call dialog from within a shell script to
ask the user questions or present with choices in a more user friendly
manner.

%prep
%setup -q
%patch0 -p1

%build
LDFLAGS="-s"
CFLAGS="$RPM_OPT_FLAGS"
export LDFLAGS CFLAGS
%configure \
	--enable-gpm-support
%{__make} PROGS="whiptail whiptcl.so testgrid" \
	pythondir = \$(prefix)/lib/python1.6 \
	pythonbindir = \$(prefix)/lib/python1.6/lib-dynload \
	pythonincludedir = \$(prefix)/include/python1.6
%{__make} shared \
	pythondir = \$(prefix)/lib/python1.6 \
	pythonbindir = \$(prefix)/lib/python1.6/lib-dynload \
	pythonincludedir = \$(prefix)/include/python1.6

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} instroot=$RPM_BUILD_ROOT install \
	pythondir = \$(prefix)/lib/python1.6 \
	pythonbindir = \$(prefix)/lib/python1.6/lib-dynload \
	pythonincludedir = \$(prefix)/include/python1.6
%{__make} instroot=$RPM_BUILD_ROOT install-sh \
	pythondir = \$(prefix)/lib/python1.6 \
	pythonbindir = \$(prefix)/lib/python1.6/lib-dynload \
	pythonincludedir = \$(prefix)/include/python1.6

ln -sf whiptail $RPM_BUILD_ROOT%{_bindir}/dialog

#strip $RPM_BUILD_ROOT%{_bindir}/*
strip --strip-unneeded $RPM_BUILD_ROOT%{_libdir}/lib*.so.*.* \
	$RPM_BUILD_ROOT%{_libdir}/python1.5/lib-dynload/*.so

sgml2txt tutorial.sgml

gzip -9nf CHANGES tutorial.txt

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so.*.*

%files -n whiptail
%attr(755,root,root) %{_bindir}/whiptail
%attr(755,root,root) %{_bindir}/dialog

%files tcl 
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*tcl.so

%files python
%defattr(644,root,root,755)
%{_libdir}/python1.5/*.py
%attr(755,root,root) %{_libdir}/python1.5/lib-dynload/*.so

%files devel
%defattr(644,root,root,755)
%doc CHANGES.gz tutorial.txt.gz

%{_includedir}/*.h
%attr(755,root,root) %{_libdir}/lib*.so

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
