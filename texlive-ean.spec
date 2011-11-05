# revision 20851
# category Package
# catalog-ctan /macros/generic/ean
# catalog-date 2007-01-01 18:45:52 +0100
# catalog-license gpl
# catalog-version undef
Name:		texlive-ean
Version:	20070101
Release:	1
Summary:	Macros for making EAN barcodes
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/generic/ean
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ean.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ean.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
Provides EAN-8 and EAN-13 forms. The package needs the ocr-b
fonts; note that the fonts are not available under a free
licence, as the macros are.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/ean/ean13.tex
%{_texmfdistdir}/tex/generic/ean/ean8.tex
%doc %{_texmfdistdir}/doc/generic/ean/README
%doc %{_texmfdistdir}/doc/generic/ean/eantest.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
