Name:		texlive-fancytabs
Version:	41549
Release:	1
Summary:	Fancy page border tabs
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/fancytabs
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fancytabs.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fancytabs.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fancytabs.source.r%{version}.tar.xz
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
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
