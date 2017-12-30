# revision 20851
# category Package
# catalog-ctan /macros/generic/ean
# catalog-date 2007-01-01 18:45:52 +0100
# catalog-license gpl
# catalog-version undef
Name:		texlive-ean
Version:	20170414
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

%description
Provides EAN-8 and EAN-13 forms. The package needs the ocr-b
fonts; note that the fonts are not available under a free
licence, as the macros are.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/ean/ean13.tex
%{_texmfdistdir}/tex/generic/ean/ean8.tex
%doc %{_texmfdistdir}/doc/generic/ean/README
%doc %{_texmfdistdir}/doc/generic/ean/eantest.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20070101-2
+ Revision: 751277
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20070101-1
+ Revision: 718290
- texlive-ean
- texlive-ean
- texlive-ean
- texlive-ean

