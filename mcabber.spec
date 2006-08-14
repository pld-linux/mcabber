Summary:	mcabber - small console Jabber client
Summary(pl):	mcabber - ma³y konsolowy klient protoko³u Jabber
Name:		mcabber
Version:	0.8.0
Release:	1
Group:		Applications/Console
License:	GPL
Source0:	http://www.lilotux.net/%7emikael/mcabber/files/%{name}-%{version}.tar.bz2
# Source0-md5:	31addfc6f22d1c84ab7e84bdbfb103fb
URL:		http://www.lilotux.net/~mikael/mcabber/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	glib2-devel >= 2.0.0
BuildRequires:	ncurses-ext-devel
BuildRequires:	openssl-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
mcabber is a small Jabber console client for Linux. mcabber includes
features such as SSL support, history logging, commands completion,
and external actions triggers.

%description -l pl
mcabber jest ma³ym klientem protoko³u Jabber dla Linuksa.
Do mo¿liwo¶ci mcabbera nale¿±: wsparcie dla SSL, logowanie
historii, dope³nianie poleceñ i wywo³ywanie zewnêtrznych pleceñ
przy zdarzeniach.

%prep
%setup -q

%build
CPPFLAGS="-I/usr/include/ncurses"; export CPPFLAGS
%{__aclocal} -I macros
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-ssl

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO mcabberrc.example
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
