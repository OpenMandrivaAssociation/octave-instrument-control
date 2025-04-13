%global octpkg instrument-control

Summary:	Low level I/O functions for several interfaces with Octave
Name:		octave-instrument-control
Version:	0.9.4
Release:	2
License:	GPLv3+
Group:		Sciences/Mathematics
Url:		https://packages.octave.org/instrument-control/
Source0:	https://downloads.sourceforge.net/octave/instrument-control-%{version}.tar.gz

BuildRequires:  octave-devel >= 4.0.0
BuildRequires:	pkgconfig(libtirpc)
BuildRequires:	pkgconfig(libmodbus)
Requires:	octave(api) = %{octave_api}

Requires(post): octave
Requires(postun): octave

%patchlist
octave-instrument-control-0.9.4-prebuild.patch

%description
Low level I/O functions for serial, i2c, parallel, tcp, gpib, vxi11,
udp and usbtmc interfaces.

%files
%license COPYING
%doc NEWS
%dir %{octpkgdir}
%{octpkgdir}/*
%dir %{octpkglibdir}
%{octpkglibdir}/*

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{octpkg}-%{version}

%build
%set_build_flags
%octave_pkg_build

%install
%octave_pkg_install

%check
%octave_pkg_check

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

