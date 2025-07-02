Summary:	mcabber - small console Jabber client
Summary(pl.UTF-8):	mcabber - mały konsolowy klient protokołu Jabber
Name:		mcabber
Version:	1.1.2
Release:	1
License:	GPL v2+
Group:		Applications/Console
Source0:	https://mcabber.com/files/%{name}-%{version}.tar.bz2
# Source0-md5:	5c2f827e371fcfbf390c9eac66f9aaa5
Patch0:		%{name}-uninitialized.patch
Patch1:		%{name}-format.patch
URL:		https://mcabber.com/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	enchant-devel
BuildRequires:	glib2-devel >= 1:2.14.0
BuildRequires:	gpgme-devel >= 1.0.0
BuildRequires:	libidn-devel >= 0.0.0
BuildRequires:	libotr-devel >= 4.0.0
BuildRequires:	libtool
BuildRequires:	loudmouth-devel >= 1.5.3
BuildRequires:	ncurses-devel >= 5
BuildRequires:	ncurses-ext-devel >= 5
BuildRequires:	pkgconfig
Requires:	glib2 >= 1:2.14.0
Requires:	gpgme >= 1.0.0
Requires:	libotr >= 4.0.0
Requires:	loudmouth >= 1.5.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
mcabber is a small Jabber console client for Linux. mcabber includes
features such as SSL support, history logging, commands completion,
and external actions triggers.

%description -l pl.UTF-8
mcabber jest małym klientem protokołu Jabber dla Linuksa. Do
możliwości mcabbera należą: obsługa SSL, logowanie historii,
dopełnianie poleceń i wywoływanie zewnętrznych pleceń przy
zdarzeniach.

%package devel
Summary:	Header files for mcabber modules development
Summary(pl.UTF-8):	Pliki nagłówkowe do tworzenia modułów mcabbera
Group:		Development/Libraries
# doesn't require base
Requires:	glib2-devel >= 1:2.14.0
Requires:	loudmouth-devel >= 1.5.3
Requires:	ncurses-devel >= 5
Requires:	ncurses-ext-devel >= 5

%description devel
Header files for mcabber modules development.

%description devel -l pl.UTF-8
Pliki nagłówkowe do tworzenia modułów mcabbera.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1

%build
%{__libtoolize}
%{__aclocal} -I macros
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# plugins loaded via libgmodule
%{__rm} $RPM_BUILD_ROOT%{_libdir}/mcabber/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO mcabberrc.example
%attr(755,root,root) %{_bindir}/mcabber
%dir %{_libdir}/mcabber
%attr(755,root,root) %{_libdir}/mcabber/lib*.so
%{_datadir}/mcabber
%{_mandir}/man1/mcabber.1*

%files devel
%defattr(644,root,root,755)
%{_includedir}/mcabber
%{_pkgconfigdir}/mcabber.pc
