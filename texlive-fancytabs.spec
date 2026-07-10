%global tl_name fancytabs
%global tl_revision 41549

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.9
Release:	%{tl_revision}.1
Summary:	Fancy page border tabs
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/fancytabs
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fancytabs.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fancytabs.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fancytabs.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package can typeset tabs on the side of a page. It requires TikZ
from the pgf bundle.

