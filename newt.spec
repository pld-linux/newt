Summary:     	Not Erik's Windowing Toolkit - text mode windowing with slang
Summary(de): 	Nicht Eriks Windowing Toolkit - Textmodus-Windowing mit Slang 
Summary(fr): 	Not Erik's Windowing Toolkit - fenêtrage en mode texte avec slang
Summary(pl): 	Not Erik's Windowing Toolkit - okna w trybie tekstowym ze slangiem
Summary(tr): 	Not Erik's Windowing Toolkit - metin kipi pencereleme sistemi
Name:        	newt
Version:     	0.50
Release:     	1
Copyright:   	LGPL
Group:       	Libraries
Group(pl):   	Biblioteki
Source:      	ftp://ftp.redhat.com/pub/redhat/code/newt/newt-%{version}.tar.gz
BuildRequires:	slang-devel
BuildRequires:	tcl-devel
BuildRequires:	popt-devel
Buildroot:   	/tmp/%{name}-%{version}-root

%description
Newt is a windowing toolkit for text mode built from the slang library. It
allows color text mode applications to easily use stackable windows, push
buttons, check boxes, radio buttons, lists, entry fields, labels, and
displayable text. Scrollbars are supported, and forms may be nested to
provide extra functionality. This pacakge contains the shared library for
programs that have been built with newt as well as a %{_bindir}/dialog
replacement called whiptail.

%description -l pl
Newt jest programem do okien w trybie tekstowym, budowany ze slangiem.
Pozwala na u¿ywanie kolorowych alikacji tekstowych w oknach.

%description -l de
Newt ist ein Windowing-Toolkit für Textmodus, konstruiert auf der Grundlage
der Slang-Library, mit dessen Hilfe Farbtext-Modus- Applikationen leicht mit
stapelbaren Fenstern, Schaltflächen, Optionskästchen, Listen,
Eingabefeldern, Etiketten und Display-Text arbeiten können. Auch
Bildlaufleisten erden unterstützt, und der Einbau von Formularen ist
möglich, wenn zusätzliche Funktionalität gefordert ist. Dieses Paket enthält
die gemeinsam nutzbare Library für mit Newt gebaute Programme sowie einen
%{_bindir}/dialog namens whiptail.

%description -l fr
Newt est une boite à outil de fenétrage en mode texte, construit sur la
librarie slang. Elle permet aux applications en mode texte d'utiliser
simplement de multiples fenêtres, des bouttons, des cases à cocher... Les
barres de défilement sont supportées, et les fenêtres peuvent être
imbriquées pour donner des fonctionnalités nouvelles. Ce package contient
les librairies partagées pour les programmes construits avec newt comme un
remplaçant pour %{_bindir}/dialog appelé whiptail.

%description -l tr
Newt ile karakter tabanlý ekranlarda renkli pencereler, kaydýrma çubuklarý,
çeþitli tuþlar oluþturulabilir. Bu paket newt kullanan yazýlýmlarýn gerek
duyacaðý kitaplýðý ve whiptail isimli geliþmiþ bir dialog sürümü
içermektedir.

%package devel
Summary:     	Developer's toolkit for newt windowing library
Summary(de): 	Entwickler-Toolkit für die newt-Windowing-Library 
Summary(pl): 	Pliki nag³ówkowe dla newt
Summary(fr): 	Toolkit de développement pour la bibliothèque de fenêtrage newt
Summary(tr): 	newt pencere kitaplýðý için geliþtirme dosyalarý
Group:       	Development/Libraries
Group(pl):   	Programowanie/Biblioteki
Requires:    	%{name} = %{version}

%description devel
These are the header files and libraries for developing applications which
use newt. Newt is a windowing toolkit for text mode, which provides many
widgets and stackable windows.

%description -l pl devel
Pliki nag³ówkowe dla newt.

%description -l de devel
Dies sind die Header-Dateien und Libraries zur Entwicklung von
Applikationen, die mit newt arbeiten. Newt ist ein Windowing-Toolkit für
Textmodus, der viele Widgets und stapelbare Fenster enthält.

%description -l fr devel
En-têtes et bibliothèques pour le développement d'applications utilisant
newt. newt est un tookit de fenêtrage pour le mode texte offrant de nombreux
widgets et des fenêtres empilables.

%description -l tr devel
Bu paket, newt ile geliþtirme yapmak için gereken baþlýk dosyalarýný ve
kitaplýklarý içerir. Newt, metin ekranda çalýþan bir pencereleme kitaplýðýdýr.

%package static
Summary:     	Newt static library
Summary(pl): 	Biblioteka statyczna newt
Group:       	Development/Libraries
Group(pl):   	Programowanie/Biblioteki
Requires:    	%{name}-devel = %{version}

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
Newt Tcl bindings

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
Dodatki do python'a z Newt'a

%prep
%setup -q

%build
./configure %{_target_platform} \
	--enable-gpm-support
make PROGS="whiptail whiptcl.so testgrid"
make shared 

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

make instroot=$RPM_BUILD_ROOT install
make instroot=$RPM_BUILD_ROOT install-sh

strip $RPM_BUILD_ROOT%{_bindir}/*

gzip -9nf CHANGES tutorial.sgml

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.gz

%attr(755,root,root) %{_libdir}/*.so.*
%attr(755,root,root) %{_bindir}/whiptail

%files tcl 
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*tcl.so

%files python
%defattr(644,root,root,755)
%{_libdir}/python1.5/*.py
%attr(755,root,root) %{_libdir}/python1.5/lib-dynload/*.so

%files devel
%doc tutorial.sgml.gz

%attr(644,root,root) %{_includedir}/*.h
%attr(755,root,root) %{_libdir}/lib*.so

%files static
%attr(644,root,root) %{_libdir}/*.a
