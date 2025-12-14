Name:		python-roman
Version:	5.2
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/r/roman/roman-%{version}.tar.gz
Summary:	Integer to Roman numerals converter
URL:		https://pypi.org/project/roman/
License:	ZPL-2.1
Group:		Development/Python
BuildSystem:	python
BuildRequires:	python%{pyver}dist(setuptools)
BuildArch:	noarch

%description
Integer to Roman numerals converter

%files
%{_bindir}/roman
%{py_sitedir}/roman
%{py_sitedir}/roman-*.*-info
