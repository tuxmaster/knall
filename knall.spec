Name:		knall
Version:	2.0.0
Release:	1%{?dist}
Summary:	Crash tests
Summary(de):	Unfalltest
License:	GPLv3
Source0:	knall.tar.xz	
URL:		https://github.com/tuxmaster/knall
BuildRequires:	java-devel >= 1:1.8.0 gcc-c++
Requires:	%{name}-cpp = %{version}-%{release}
Requires:	%{name}-python = %{version}-%{release}
Requires:	%{name}-kernel = %{version}-%{release}
Requires:	%{name}-java = %{version}-%{release}
Requires:	%{name}-ruby = %{version}-%{release}

%description
Test tools for check the chain of crashes.

%description -l de
Werkzeuge um das Verhalten des Systems bei Abstürzen zu testen.

%package cpp
Obsoletes:	Unfalltest	
Summary:	The C++ part
Summary(de):	Der C++ Teil

%description cpp
The C++ test.

%description cpp -l de
Der C++ Test.

%package python
BuildArch:	noarch
Summary:	The python part
Summary(de):	Der Python Teil

%description python
The python test.

%description python -l de
Der Python Test.

%package kernel
BuildArch:	noarch
Summary:	The kernel part
Summary(de):	Der Kernel Teil

%description kernel
The kernel test.

%description kernel -l de
Der Kernel Test.

%package java
BuildArch:	noarch
Requires:	java-headless >= 1:1.8.0 javapackages-tools
Summary:	The java part
Summary(de):	Der Java Teil

%description java
The java test.

%description java -l de
Der Java Test.

%package ruby
BuildArch:	noarch
Requires:	ruby(release)
Summary:	The ruby part
Summary(de):	Der Ruby Teil

%description ruby
The ruby test.

%description ruby -l de
Der Ruby Test.

%prep
%autosetup -n %{name}

%build
#C++
g++ cpp/knall.cpp $RPM_OPT_FLAGS -o knall-cpp
#Java
javac java/knall.java

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
#C++
install -m 755 knall-cpp %{buildroot}%{_bindir}/
#Python
install -m 755 python/knall %{buildroot}%{_bindir}/knall-python
#Kernel
install -m 755 kernel/knall %{buildroot}%{_bindir}/knall-kernel
#Java
install -m 444 java/knall.class %{buildroot}%{_bindir}/
install -m 755 java/knall-java %{buildroot}%{_bindir}/
#Ruby
install -m 755 ruby/knall-ruby %{buildroot}%{_bindir}/

%clean
rm -rf %{buildroot}

%files 

%files cpp
%defattr(-,root,root,-)
%{_bindir}/knall-cpp

%files python
%defattr(-,root,root,-)
%{_bindir}/knall-python

%files kernel
%defattr(-,root,root,-)
%{_bindir}/knall-kernel

%files java
%defattr(-,root,root,-)
%{_bindir}/knall-java
%{_bindir}/knall.class

%files ruby
%defattr(-,root,root,-)
%{_bindir}/knall-ruby

%changelog
*
- Fix compiler name for RHEL/Fedora

* Sat Apr 25 2020 tuxmaster <github@terrortux.de> - 2.0.0-1
- Remove deprecated group tag
- Switch to python3
- Clean up spec file

* Thu Jul 27 2017 tuxmaster <github@terrortux.de> 1.0.0-2
- Obsoletes the old Unfalltest package at the cpp part.
- Fix rpmlint errors.

* Sat Jan 07 2017 tuxmaster <github@terrortux.de> 1.0.0-1
- start
