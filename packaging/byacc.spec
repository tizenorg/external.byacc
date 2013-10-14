%define byaccdate 20091027

Summary: Berkeley Yacc, a parser generator
Name: byacc
Version: 1.9.%{byaccdate}
Release: 2
License: Public Domain
Group: Platform Development/Building
URL: http://invisible-island.net/byacc/byacc.html
Source: %{name}-%{version}.tar.bz2
Source1001: packaging/byacc.manifest 

%description
Byacc (Berkeley Yacc) is a public domain LALR parser generator which
is used by many programs during their build process.

If you are going to do development on your system, you will want to install
this package.

%prep
%setup -q

%build
cp %{SOURCE1001} .
%configure --disable-dependency-tracking
make %{?jobs:-j%jobs}

%install
mkdir -p %{buildroot}/usr/share/license
cp README %{buildroot}/usr/share/license/%{name}
%make_install
ln -s yacc %{buildroot}/%{_bindir}/byacc
ln -s yacc.1 %{buildroot}/%{_mandir}/man1/byacc.1

%check
echo ====================TESTING=========================
make check
echo ====================TESTING END=====================

%clean
rm -rf %{buildroot}

%files
%doc ACKNOWLEDGEMENTS CHANGES NEW_FEATURES NOTES NO_WARRANTY README
%defattr(-,root,root,-)
%{_bindir}/yacc
%{_bindir}/byacc
%{_mandir}/man1/yacc.1*
%{_mandir}/man1/byacc.1*
/usr/share/license/%{name}
