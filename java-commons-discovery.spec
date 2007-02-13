%define	short_name	commons-discovery
Summary:	Jakarta Commons Discovery - discovering implementations for pluggable interfaces
Summary(pl.UTF-8):	Pakiet Jakarta Commons Discovery - wykrywanie implementacji dołączalnych interfejsów
Name:		jakarta-commons-discovery
Version:	0.2
Release:	0.1
License:	Apache Software License
Group:		Development/Languages/Java
Source0:	http://www.apache.org/dist/jakarta/commons/discovery/source/commons-discovery-%{version}-src.tar.gz
# Source0-md5:	57968a150ea9b7158ac0e995c8f24080
URL:		http://jakarta.apache.org/commons/discovery/
BuildRequires:	ant
BuildRequires:	jakarta-commons-logging >= 1.0.1
BuildRequires:	junit >= 3.7
Requires:	jakarta-commons-logging >= 1.0.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Discovery component is about discovering, or finding,
implementations for pluggable interfaces. Pluggable interfaces are
specified with the intent that multiple implementations are, or will
be, available to provide the service described by the interface.
Discovery provides facilities for finding and instantiating classes,
and for lifecycle management of singleton (factory) classes.

%description -l pl.UTF-8
Komponent Discovery służy do wykrywania lub znajdowania implementacji
dołączalnych interfejsów. Dołączalne interfejsy są określane wtedy,
gdy jest (lub będzie) dostępnych wiele implementacji dostarczających
usługę opisaną przez interfejs. Discovery udostępnia ułatwienia do
znajdowania i dziedziczenia klas oraz zarządzania cyklem życia klas
singleton (factory).

%package javadoc
Summary:	Javadoc for %{name}
Summary(pl.UTF-8):	Dokumentacja javadoc dla pakietu %{name}
Group:		Documentation

%description javadoc
Javadoc for %{name}.

%description javadoc -l pl.UTF-8
Dokumentacja javadoc dla pakietu %{name}.

%prep
%setup -q -n commons-discovery-%{version}
chmod u+w .

# No NOTICE.txt file in the sources
touch NOTICE.txt

%build
ant \
	-Djunit.jar=/usr/share/java/junit.jar \
	-Dlogger.jar=/usr/share/java/commons-logging.jar \
	test.discovery dist

%install
rm -rf $RPM_BUILD_ROOT

# jar
install -d $RPM_BUILD_ROOT%{_javadir}
cp -p dist/%{short_name}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
cd $RPM_BUILD_ROOT%{_javadir}
ln -s %{name}-%{version}.jar %{short_name}-%{version}.jar
for jar in *-%{version}.jar; do
	ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`
done
cd -

# javadoc
install -d $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr dist/docs/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE.txt
%{_javadir}/*

%files javadoc
%defattr(644,root,root,755)
%{_javadocdir}/%{name}-%{version}
