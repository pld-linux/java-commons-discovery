%bcond_without	javadoc	# Build api docs
%include	/usr/lib/rpm/macros.java
%define		srcname	commons-discovery
Summary:	Commons Discovery - discovering implementations for pluggable interfaces
Summary(pl.UTF-8):	Pakiet Commons Discovery - wykrywanie implementacji dołączalnych interfejsów
Name:		java-commons-discovery
Version:	0.2
Release:	1
License:	Apache
Group:		Libraries/Java
Source0:	http://www.apache.org/dist/commons/discovery/source/commons-discovery-%{version}-src.tar.gz
# Source0-md5:	57968a150ea9b7158ac0e995c8f24080
Patch0:		jakarta-commons-discovery-source.patch
URL:		http://commons.apache.org/commons/discovery/
BuildRequires:	ant
BuildRequires:	java-commons-logging >= 1.0.1
BuildRequires:	java-gcj-compat-devel
BuildRequires:	jpackage-utils
BuildRequires:	junit >= 3.7
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	java-commons-logging >= 1.0.1
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
Requires:	jpackage-utils

%description javadoc
Javadoc for %{name}.

%description javadoc -l pl.UTF-8
Dokumentacja javadoc dla pakietu %{name}.

%prep
%setup -q -n commons-discovery-%{version}-src
chmod -R u+w .
%patch0 -p1

cp discovery/LICENSE.txt LICENSE

%build
cd discovery
export SHELL=/bin/sh
%ant	-Dbuild.compiler=extJavac \
	-Dcompile.source=1.4 \
	-Djunit.jar=%{_javadir}/junit.jar \
	-Dlogger.jar=%{_javadir}/commons-logging.jar \
	dist

%install
rm -rf $RPM_BUILD_ROOT
cd discovery

# jar
install -d $RPM_BUILD_ROOT%{_javadir}
cp -a dist/commons-discovery.jar $RPM_BUILD_ROOT%{_javadir}/commons-discovery-%{version}.jar
ln -s commons-discovery-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/commons-discovery.jar

# javadoc
%if %{with javadoc}
install -d $RPM_BUILD_ROOT%{_javadocdir}/%{srcname}-%{version}
cp -pr dist/docs/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{srcname}-%{version}
ln -s %{srcname}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{srcname} # ghost symlink
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post javadoc
ln -sf %{srcname}-%{version} %{_javadocdir}/%{srcname}

%files
%defattr(644,root,root,755)
%doc discovery/LICENSE.txt
%{_javadir}/*.jar

%if %{with javadoc}
%files javadoc
%defattr(644,root,root,755)
%{_javadocdir}/%{srcname}-%{version}
%ghost %{_javadocdir}/%{srcname}
%endif
