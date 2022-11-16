Name:		texlive-mathfont
Version:	61719
Release:	1
Summary:	Use TrueType and OpenType fonts in math mode
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/mathfont
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mathfont.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mathfont.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mathfont.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The mathfont package adapts unicode text fonts for math mode.
The package allows the user to specify a default unicode font
for different classes of math symbols, and it provides tools to
change the font locally for math alphabet characters. When
typesetting with LuaTeX, mathfont adds resizable delimiters,
big operators, and a MathConstants table to text fonts.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/mathfont
%{_texmfdistdir}/tex/latex/mathfont
%doc %{_texmfdistdir}/doc/latex/mathfont

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
