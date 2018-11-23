Summary:	mcabber - small console Jabber client
Summary(pl.UTF-8):	mcabber - mały konsolowy klient protokołu Jabber
Name:		mcabber
Version:	1.1.0
Release:	2
License:	GPL
Group:		Applications/Console
Source0:	http://www.lilotux.net/~mikael/mcabber/files/%{name}-%{version}.tar.bz2
# Source0-md5:	4ff3626063285033c0a99b37827e0c11
URL:		http://www.lilotux.net/~mikael/mcabber/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	glib2-devel >= 2.0.0
BuildRequires:	gpgme-devel
BuildRequires:	libotr-devel
BuildRequires:	libtool
BuildRequires:	loudmouth-devel >= 1.4.2
BuildRequires:	ncurses-ext-devel
BuildRequires:	openssl-devel
BuildRequires:	pkgconfig
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

%prep
%setup -q

%build
%{__libtoolize} --automake
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
%{_datadir}/%{name}
