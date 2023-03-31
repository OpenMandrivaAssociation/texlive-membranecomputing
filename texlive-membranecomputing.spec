Name:		texlive-membranecomputing
Version:	64627
Release:	2
Summary:	Membrane Computing notation
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/membranecomputing
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/membranecomputing.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/membranecomputing.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is a LaTeX package for the Membrane Computing community.
It comprises the definition of P systems, rules and some
concepts related to languages and computational complexity
usually needed for Membrane Computing research. The package
depends on ifthen and xstring.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/membranecomputing
%doc %{_texmfdistdir}/doc/latex/membranecomputing

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
