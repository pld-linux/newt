#
# Conditional build:
%bcond_with	c_only	# build only C libraries
#
%include	/usr/lib/rpm/macros.python
Summary:	Not Erik's Windowing Toolkit - text mode windowing with slang
Summary(de):	Nicht Eriks Windowing Toolkit - Textmodus-Windowing mit Slang
Summary(fr):	Not Erik's Windowing Toolkit - fen�trage en mode texte avec slang
Summary(pl):	Not Erik's Windowing Toolkit - okna w trybie tekstowym ze slangiem
Summary(tr):	Not Erik's Windowing Toolkit - metin kipi pencereleme sistemi
Name:		newt
Version:	0.50.34
Release:	9
License:	LGPL
Group:		Libraries
Source0:	ftp://www.msg.com.mx/pub/Newt/%{name}-%{version}.tar.gz
# Source0-md5:	e4b4a030cd8d7ee1a4d83ad73dfbb1bb
Patch0:		%{name}-pythondirs.patch
Patch1:		%{name}-textbox.patch
Patch2:		%{name}-install_sh.patch
Patch3:		%{name}-gpm-fix.diff
Patch4:		%{name}-omg_fix.patch
Patch5:		%{name}-PIC.patch
Patch6:		%{name}-norm.patch
Patch7:		%{name}-c_only.patch
URL:		http://www.msg.com.mx/Newt/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	popt-devel
%{?!with_c_only:BuildRequires:	python-devel >= 2.2}
#BuildRequires:	sgml-tools
BuildRequires:	slang-devel
%{?!with_c_only:BuildRequires:	tcl-devel >= 8.3.2}
BuildRequires:	docbook-utils
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
Newt ist ein Windowing-Toolkit f�r Textmodus, konstruiert auf der
Grundlage der Slang-Library, mit dessen Hilfe Farbtext-Modus-
Applikationen leicht mit stapelbaren Fenstern, Schaltfl�chen,
Optionsk�stchen, Listen, Eingabefeldern, Etiketten und Display-Text
arbeiten k�nnen. Auch Bildlaufleisten erden unterst�tzt, und der
Einbau von Formularen ist m�glich, wenn zus�tzliche Funktionalit�t
gefordert ist.

%description -l fr
Newt est une boite � outil de fen�trage en mode texte, construit sur
la librarie slang. Elle permet aux applications en mode texte
d'utiliser simplement de multiples fen�tres, des bouttons, des cases �
cocher... Les barres de d�filement sont support�es, et les fen�tres
peuvent �tre imbriqu�es pour donner des fonctionnalit�s nouvelles.

%description -l pl
Newt jest bibliotek� typu toolkit ale do trybu tekstowego, osadzon� na
bibliotece slang. Umo�liwia budowanie aplikacji pracuj�cych w trybie
tekstowym umo�liwij�c operowanie na okienkach, przyciskach (push
button), listach wyboru, etykietach i elementach tekstowych jakie s�
potrzebne przy tworzeniu interfejsu u�ytkownika w r�nych aplikacjach.

%description -l tr
Newt ile karakter tabanl� ekranlarda renkli pencereler, kayd�rma
�ubuklar�, �e�itli tu�lar olu�turulabilir.

%package devel
Summary:	Developer's toolkit for newt windowing library
Summary(de):	Entwickler-Toolkit f�r die newt-Windowing-Library
Summary(fr):	Toolkit de d�veloppement pour la biblioth�que de fen�trage newt
Summary(pl):	Pliki nag��wkowe dla newt
Summary(tr):	newt pencere kitapl��� i�in geli�tirme dosyalar�
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
These are the header files and libraries for developing applications
which use newt. Newt is a windowing toolkit for text mode, which
provides many widgets and stackable windows.

%description devel -l de
Dies sind die Header-Dateien und Libraries zur Entwicklung von
Applikationen, die mit newt arbeiten. Newt ist ein Windowing-Toolkit
f�r Textmodus, der viele Widgets und stapelbare Fenster enth�lt.

%description devel -l fr
En-t�tes et biblioth�ques pour le d�veloppement d'applications
utilisant newt. newt est un tookit de fen�trage pour le mode texte
offrant de nombreux widgets et des fen�tres empilables.

%description devel -l pl
Pliki nag��wkowe dla newt.

%description devel -l tr
Bu paket, newt ile geli�tirme yapmak i�in gereken ba�l�k dosyalar�n�
ve kitapl�klar� i�erir. Newt, metin ekranda �al��an bir pencereleme
kitapl���d�r.

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
Dodatki do Tcl z Newta

%package python
Summary:	Newt python bindings
Summary(pl):	Dodatki do pythona z Newta
Group:		Development/Languages/Python
Requires:	%{name} = %{version}-%{release}
%pyrequires_eq	python
Provides:	snack

%description python
Newt python bindings

%description python -l pl
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
Program umo�liwi�cy budowa� interfejsy u�ytkownika na terminalu
tekstowym, kompatybilny z programem dialog. Pozwala wywo�a� dialog ze
skryptu shella, aby zda� pytania u�ytkownikowi w spos�b bardziej
przyjazny.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p0
%patch5 -p1
%patch6 -p1
%if %{with c_only}
%patch7 -p1
%endif

%build
%{__aclocal}
%{__autoconf}
%configure \
	--enable-gpm-support

%{__make} \
	PROGS="whiptail %{?!with_c_only:whiptcl.so} testgrid"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
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

%if ! %{with c_only}
%files tcl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*tcl.so

%files python
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/*.so
%{py_sitedir}/*.py
%endif

%files devel
%defattr(644,root,root,755)
%doc CHANGES
#tutorial.txt
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a