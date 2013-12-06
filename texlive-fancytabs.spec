# revision 27684
# category Package
# catalog-ctan /macros/latex/contrib/fancytabs
# catalog-date 2012-09-17 18:38:18 +0200
# catalog-license lppl1.3
# catalog-version 1.8
Name:		texlive-fancytabs
Version:	1.8
Release:	2
Summary:	Fancy page border tabs
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/fancytabs
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fancytabs.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fancytabs.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fancytabs.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package can typeset tabs on the side of a page. It requires
TikZ from the pgf bundle.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/fancytabs/fancytabs.sty
%doc %{_texmfdistdir}/doc/latex/fancytabs/README
%doc %{_texmfdistdir}/doc/latex/fancytabs/fancytabs.pdf
#- source
%doc %{_texmfdistdir}/source/latex/fancytabs/fancytabs.dtx
%doc %{_texmfdistdir}/source/latex/fancytabs/fancytabs.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Fri Oct 26 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.8-1
+ Revision: 819991
- Update to latest release.

* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.6-2
+ Revision: 751790
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.6-1
+ Revision: 718417
- texlive-fancytabs
- texlive-fancytabs
- texlive-fancytabs
- texlive-fancytabs

