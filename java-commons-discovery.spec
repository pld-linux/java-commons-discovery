%define	short_name	commons-discovery
Summary:	Jakarta Commons Discovery - discovering implementations for pluggable interfaces
Summary(pl):	Pakiet Jakarta Commons Discovery - wykrywanie implementacji do³±czalnych interfejsów
Name:		jakarta-commons-discovery
Version:	0.3
Release:	0.1
License:	Apache Software License
Group:		Development/Languages/Java
Source0:	http://www.apache.org/dist/jakarta/commons/discovery/source/commonsdiscovery%{version}src.tar.gz
# Source0-md5:	233726c301278b7ca8baa50eb7b0f582
URL:		http://jakarta.apache.org/commons/discovery/
BuildRequires:	jakarta-ant
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

%description -l pl
Komponent Discovery s³u¿y do wykrywania lub znajdowania implementacji
do³±czalnych interfejsów. Do³±czalne interfejsy s± okre¶lane wtedy,
gdy jest (lub bêdzie) dostêpnych wiele implementacji dostarczaj±cych
us³ugê opisan± przez interfejs. Discovery udostêpnia u³atwienia do
znajdowania i dziedziczenia klas oraz zarz±dzania cyklem ¿ycia klas
singleton (factory).

%package javadoc
Summary:	Javadoc for %{name}
Summary(pl):	Dokumentacja javadoc dla pakietu %{name}
Group:		Documentation

%description javadoc
Javadoc for %{name}.

%description javadoc -l pl
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
