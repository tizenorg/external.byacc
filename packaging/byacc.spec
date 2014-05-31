#specfile originally created for Fedora, modified for Moblin Linux
%define byaccdate 20091027

Summary: Berkeley Yacc, a parser generator
Name: byacc
Version: 1.9.%{byaccdate}
Release: 3
License: Public Domain
Group: Development/Tools
URL: http://invisible-island.net/byacc/byacc.html
Source: ftp://invisible-island.net/byacc/byacc-%{byaccdate}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
Byacc (Berkeley Yacc) is a public domain LALR parser generator which
is used by many programs during their build process.

If you are going to do development on your system, you will want to install
this package.

%prep
%setup -q -n byacc-%{byaccdate}

%build
%configure --disable-dependency-tracking
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install
ln -s yacc $RPM_BUILD_ROOT/%{_bindir}/byacc
ln -s yacc.1 $RPM_BUILD_ROOT/%{_mandir}/man1/byacc.1

%check
echo ====================TESTING=========================
make check
echo ====================TESTING END=====================

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc ACKNOWLEDGEMENTS CHANGES NEW_FEATURES NOTES NO_WARRANTY README
%defattr(-,root,root,-)
%{_bindir}/yacc
%{_bindir}/byacc
%{_mandir}/man1/yacc.1*
%{_mandir}/man1/byacc.1*
