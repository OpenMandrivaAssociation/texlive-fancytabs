Name:		texlive-fancytabs
Version:	1.6
Release:	1
Summary:	Fancy page border tabs
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/fancytabs
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fancytabs.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fancytabs.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fancytabs.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package can typeset tabs on the side of a page. It requires
TikZ from the pgf bundle.

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
