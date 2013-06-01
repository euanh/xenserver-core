Name:           biniou
Version:        1.0.6
Release:        0
Summary:        Binary data format designed for speed, safety, ease of use and backward compatibility as protocols evolve
License:        BSD3
Group:          Development/Other
URL:            http://mjambon.com/releases/biniou/biniou-1.0.6.tar.gz
Source0:        biniou-1.0.6.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:  ocaml
Requires:       ocaml

%description
Binary data format designed for speed, safety, ease of use and backward compatibility as protocols evolve.

%prep
%setup -q -n biniou-%{version}

%build
make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_libdir}/ocaml
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
mkdir -p %{buildroot}/%{_bindir}
make install BINDIR=%{buildroot}/%{_bindir}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc LICENSE README.md
%{_libdir}/ocaml/biniou/*
%{_bindir}/bdump

%changelog
* Fri May 31 2013 David Scott <dave.scott@eu.citrix.com>
- Initial package
