%define name hunt
%define version 1.5
%define release %mkrel 9

Summary: Connection intruder
Name: %name	
Version: %version
Release: %release
License:	GPL
Group:		Networking/Other
Source0:	ftp://ftp.gncz.cz/pub/linux/hunt/%{name}-%{version}.tar.bz2
Url:		http://lin.fsid.cvut.cz/~kra/index.html#HUNT
BuildRoot:	%{_tmppath}/%{name}-buildroot

%description
Hunt is a program for intruding into a connection, watching it and
resetting it.

%prep
rm -rf $RPM_BUILD_ROOT

%setup -q

%build
%make
cd tpserv
# gcc, not egcs
%make CC=gcc

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}/man1
install -d $RPM_BUILD_ROOT%{_bindir}

install man/hunt.1 $RPM_BUILD_ROOT%{_mandir}/man1
install hunt $RPM_BUILD_ROOT%{_bindir}
install tpserv/tpserv $RPM_BUILD_ROOT%{_bindir}
install tpsetup/transproxy $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README* INSTALL CHANGES TODO 
%{_bindir}/*
%{_mandir}/man1/*

