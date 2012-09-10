# TODO
# - paths and deps for demo
%define		plugin	custom-radio-checkbox
Summary:	jQuery Custom Radio-Checkbox Plugin
Name:		jquery-%{plugin}
Version:	0.1
Release:	1
License:	MIT
Group:		Applications/WWW
Source0:	https://github.com/dciccale/Custom-radio-checkbox/tarball/master#/%{plugin}-%{version}.tgz
# Source0-md5:	709d8c43c13a2251b636a89d64ca557b
URL:		http://dciccale.github.com/Custom-radio-checkbox/
BuildRequires:	rpmbuild(macros) > 1.268
Requires:	jquery >= 1.4.4
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir	%{_datadir}/jquery/%{plugin}

%description
jQuery Custom Radio Checkbox plugin Customize native html radios &
checkboxes with any image you want.

%package demo
Summary:	Demo for jQuery.%{plugin}
Summary(pl.UTF-8):	Pliki demonstracyjne dla pakietu jQuery.%{plugin}
Group:		Development
Requires:	%{name} = %{version}-%{release}

%description demo
Demonstrations and samples for jQuery.%{plugin}.

%prep
%setup -qc
mv *-Custom-radio-checkbox-*/* .

# separate demo files
install -d demo/{css,js}
mv *.html demo
mv css/demo*.css demo/css
mv js/demo*.js demo/js

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_appdir},%{_examplesdir}/%{name}-%{version}}
cp -p js/jquery.%{plugin}.min.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}-%{version}.min.js
cp -p js/jquery.%{plugin}.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}-%{version}.js
ln -s %{plugin}-%{version}.min.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}.js

install -d $RPM_BUILD_ROOT%{_appdir}/css
cp -p css/%{plugin}.min.css $RPM_BUILD_ROOT%{_appdir}/css/%{plugin}-%{version}.min.css
cp -p css/%{plugin}.css $RPM_BUILD_ROOT%{_appdir}/css/%{plugin}-%{version}.css
ln -s %{plugin}-%{version}.min.css $RPM_BUILD_ROOT%{_appdir}/css/%{plugin}.css

cp -a img $RPM_BUILD_ROOT%{_appdir}

cp -a demo/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%{_appdir}

%files demo
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
