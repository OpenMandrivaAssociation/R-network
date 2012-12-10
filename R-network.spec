%bcond_without bootstrap
%global packname  network
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          1.7
Release:          2
Summary:          Classes for Relational Data
Group:            Sciences/Mathematics
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
Requires:         R-utils 
%if %{without bootstrap}
Requires:         R-sna R-statnet 
%endif
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-utils
%if %{without bootstrap}
BuildRequires:    R-sna R-statnet 
%endif

%description
Tools to create and modify network objects.  The network class can
represent a range of relational data types, and supports arbitrary
vertex/edge/graph attributes.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%if %{without bootstrap}
%check
%{_bindir}/R CMD check %{packname}
%endif

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/network.api


%changelog
* Wed Feb 22 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.7-2
+ Revision: 778815
- Rebuild with proper dependencies

* Sat Feb 18 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.7-1
+ Revision: 776946
- Import R-network
- Import R-network

