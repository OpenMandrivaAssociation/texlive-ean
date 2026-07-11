%global tl_name ean
%global tl_revision 20851

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Macros for making EAN barcodes
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/generic/ean
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ean.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ean.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Provides EAN-8 and EAN-13 forms. The package needs the ocr-b fonts; note
that the fonts are not available under a free licence, as the macros
are.

