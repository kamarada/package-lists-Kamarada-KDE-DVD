#
# spec file for package package-lists-openSUSE
#
# Copyright (c) 2011 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Url:            http://en.opensuse.org/Patterns

Name:           package-lists-openSUSE-KDE-cd
License:        BSD3c
Group:          Metapackages
AutoReqProv:    on
Summary:        Patterns for Installation (full ftp tree)
Version:        11.4
Release:        571.29.1
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source0:        packagelist
Source1:        list-requires
Source2:        package-lists-openSUSE-rpmlintrc
%define __find_requires perl %{S:1}
%define _use_internal_dependency_generator 0
ExclusiveArch:  %ix86 x86_64

%description
This is an internal package that is used to create the patterns as part
of the installation source setup.  Installation of this package does
not make sense.

%prep

%build

%install
mkdir -p $RPM_BUILD_ROOT/usr/share/suse/packages
install -D -m 644 %{SOURCE0} $RPM_BUILD_ROOT/usr/share/suse/packages/kde_cd.%{_target_cpu}.list

%files
%defattr(-,root,root)
%dir /usr/share/suse
%dir /usr/share/suse/packages
/usr/share/suse/packages/kde_cd.*.list

%changelog
