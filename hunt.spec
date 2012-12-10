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



%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 1.5-9mdv2011.0
+ Revision: 619491
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 1.5-8mdv2010.0
+ Revision: 429480
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.5-7mdv2009.0
+ Revision: 247108
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 1.5-5mdv2008.1
+ Revision: 140755
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - use %%mkrel
    - import hunt


* Thu Jul 07 2005 Lenny Cartier <lenny@mandrakesoft.com> 1.5-5mdk
- rebuild

* Mon Feb 23 2004 Lenny Cartier <lenny@mandrakesoft.com> 1.5-4mdk
- rebuild

* Thu Jan 30 2003 Lenny Cartier <lenny@mandrakesoft.com> 1.5-3mdk
- rebuild

* Mon Apr 15 2002 Lenny Cartier <lenny@mandrakesoft.com> 1.5-2mdk
- URL

* Mon Apr 15 2002 Lenny Cartier <lenny@mandrakesoft.com> 1.5-1mdk
- updated by Olivier Thauvin <thauvin@aerov.jussieu.fr>

