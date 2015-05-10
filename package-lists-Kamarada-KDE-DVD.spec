#
# spec file for package package-lists-Kamarada-KDE-DVD
#
# Copyright (c) 2015 Projeto Kamarada, Aracaju, Brasil.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://github.com/kamarada
#


Url:            http://github.com/kamarada/package-lists-Kamarada-KDE-DVD

Name:           package-lists-Kamarada-KDE-DVD
License:        BSD3c
Group:          Metapackages
AutoReqProv:    on
Summary:        Lista de pacotes do LiveDVD do Kamarada Linux
Version:        13.2
Release:        1
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source0:        packagelist
Source1:        list-requires
Source2:        package-lists-Kamarada-KDE-DVD-rpmlintrc
%define __find_requires perl %{S:1}
%define _use_internal_dependency_generator 0
ExclusiveArch:  %ix86 x86_64

%description
Este é um pacote interno que é usado pelo Projeto Kamarada para criar o LiveDVD
do Kamarada Linux. Instalar esse pacote não faz sentido.


%prep


%build


%install
mkdir -p $RPM_BUILD_ROOT/usr/share/Kamarada/packages
install -D -m 644 %{SOURCE0} $RPM_BUILD_ROOT/usr/share/Kamarada/packages/KDE_DVD_%{_target_cpu}.list


%files
%defattr(-,root,root)
%dir /usr/share/Kamarada
%dir /usr/share/Kamarada/packages
/usr/share/Kamarada/packages/KDE_DVD_*.list


%changelog
