%global tl_name mathfont
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	3.0a
Release:	%{tl_revision}.1
Summary:	Use TrueType and OpenType fonts in math mode
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/unicodetex/latex/mathfont
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mathfont.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mathfont.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mathfont.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The mathfont package adapts unicode text fonts for math mode. The
package allows the user to specify a default unicode font for different
classes of math symbols, and it enables Unicode input in math mode. The
package provides tools to change the font locally for math alphabet
characters. When typesetting with LuaTeX, mathfont adds resizable
delimiters, big operators, and a MathConstants table to text fonts.

