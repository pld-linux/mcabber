Summary:	mcabber - small console Jabber client
Summary(pl):	mcabber - ma³y konsolowy klient protoko³u Jabber
Name:		mcabber
Version:	0.6.5
Release:	1
Group:		Applications/Console
License:	GPL
Source0:	http://www.lilotux.net/%7emikael/mcabber/files/%{name}-%{version}.tar.bz2
# Source0-md5:	041f50bc3d8843e761ce8de78d0d32a3
URL:		http://www.lilotux.net/~mikael/mcabber/
BuildRequires:	glib2-devel
# this one for autocrap only:
BuildRequires:	gnutls-devel
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
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
cp -f /usr/share/automake/config.sub .
%configure \
	--with-openssl

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
