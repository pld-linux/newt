Summary:     	Not Erik's Windowing Toolkit - text mode windowing with slang
Summary(de): 	Nicht Eriks Windowing Toolkit - Textmodus-Windowing mit Slang 
Summary(fr): 	Not Erik's Windowing Toolkit - fenêtrage en mode texte avec slang
Summary(pl): 	Not Erik's Windowing Toolkit - okna w trybie tekstowym ze slangiem
Summary(tr): 	Not Erik's Windowing Toolkit - metin kipi pencereleme sistemi
Name:        	newt
Version:     	0.40
Release:     	9
Copyright:   	LGPL
Group:       	Libraries
Group(pl):   	Biblioteki
Source:      	ftp://ftp.redhat.com/pub/redhat/code/newt/newt-%{version}.tar.gz
BuildPrereq:	slang-devel
BuildPrereq:	tcl-devel
Buildroot:   	/tmp/%{name}-%{version}-root

%description
Newt is a windowing toolkit for text mode built from the slang library. It
allows color text mode applications to easily use stackable windows, push
buttons, check boxes, radio buttons, lists, entry fields, labels, and
displayable text. Scrollbars are supported, and forms may be nested to
provide extra functionality. This pacakge contains the shared library for
programs that have been built with newt as well as a /usr/bin/dialog
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
/usr/bin/dialog namens whiptail.

%description -l fr
Newt est une boite à outil de fenétrage en mode texte, construit sur la
librarie slang. Elle permet aux applications en mode texte d'utiliser
simplement de multiples fenêtres, des bouttons, des cases à cocher... Les
barres de défilement sont supportées, et les fenêtres peuvent être
imbriquées pour donner des fonctionnalités nouvelles. Ce package contient
les librairies partagées pour les programmes construits avec newt comme un
remplaçant pour /usr/bin/dialog appelé whiptail.

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
Provides:	snack

%description python
Newt python bindings

%description python -l pl
Dodatki do python'a z Newt'a

%prep
%setup -q

%build
./configure \
	--enable-gpm-support
make PROGS="whiptail whiptcl.so testgrid"
make shared 

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

make instroot=$RPM_BUILD_ROOT install
make instroot=$RPM_BUILD_ROOT install-sh

strip $RPM_BUILD_ROOT/usr/bin/*

gzip -9nf CHANGES tutorial.sgml

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.gz

%attr(755,root,root) /usr/lib/*.so.*
%attr(711,root,root) /usr/bin/whiptail

%files tcl 
%defattr(644,root,root,755)
%attr(755,root,root) /usr/lib/*tcl.so

%files python
%defattr(644,root,root,755)
/usr/lib/python1.5/*.py
%attr(755,root,root) /usr/lib/python1.5/lib-dynload/*.so

%files devel
%doc tutorial.sgml.gz

%attr(644,root,root) /usr/include/*.h
%attr(755,root,root) /usr/lib/lib*.so

%files static
%attr(644,root,root) /usr/lib/*.a

%changelog
* Wed Apr 21 1999 Artur Frysiak <wiget@pld.org.pl>
  [0.30-6]
- added tcl and python subpackage
- recompiled on rpm 3

* Sun Mar 14 1999 Micha³ Kuratczyk <kura@pld.org.pl>
  [0.30-4]
- added Group(pl)
- added missing tutorial
- added gzipping documentation
- cosmetic changes

* Mon Oct 05 1998 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
[0.30-3d]
- build against PLD Tornado,
- translation modified for pl,
- fixed files permissions.
- changed %defattr(755,root,root) to %defattr(644,root,root,755),
- minor modifications of the spec file.

* Thu Sep  3 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
[0.30-3]
- added -q %setup parameter,
- changed Buildroot to /tmp/%%{name}-%%{version}-root,
- added using %%{name} and %%{version} in Source,
- added static subpackage,
- recompiled against slang 1.2.x,
- added striping shared libraries,
- added %attr and %defattr macros in %files (allow build package from
  non-root account).

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Fri May 01 1998 Cristian Gafton <gafton@redhat.com>
- devel package moved to Development/Libraries

* Thu Apr 30 1998 Erik Troan <ewt@redhat.com>
- removed whiptcl.so -- it should be in a separate package

* Mon Feb 16 1998 Erik Troan <ewt@redhat.com>
- added newtWinMenu()
- many bug fixes in grid code

* Wed Jan 21 1998 Erik Troan <ewt@redhat.com>
- removed newtWinTernary()
- made newtWinChoice() return codes consistent with newtWinTernary()

* Fri Jan 16 1998 Erik Troan <ewt@redhat.com>
- added changes from Bruce Perens
    - small cleanups
    - lets whiptail automatically resize windows
- the order of placing a grid and adding components to a form no longer
  matters
- added newtGridAddComponentsToForm()

* Wed Oct 08 1997 Erik Troan <ewt@redhat.com>
- added newtWinTernary()

* Tue Oct 07 1997 Erik Troan <ewt@redhat.com>
- made Make/spec files use a buildroot
- added grid support (for newt 0.11 actually)

* Mon Jun 02 1997 Erik Troan <ewt@redhat.com>
- Added patched from Clarence Smith for setting the size of a listbox
- Version 0.9

* Tue May 28 1997 Elliot Lee <sopwith@redhat.com> 0.8-2
- Touchups on Makefile
- Cleaned up NEWT_FLAGS_*

* Tue Mar 18 1997 Erik Troan <ewt@redhat.com>
- Cleaned up listbox
- Added whiptail
- Added newtButtonCompact button type and associated colors
- Added newtTextboxGetNumLines() and newtTextboxSetHeight()

* Tue Feb 25 1997 Erik Troan <ewt@redhat.com>
- Added changes from sopwith for C++ cleanliness and some listbox fixes.
