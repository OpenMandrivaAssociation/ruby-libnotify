%define name ruby-libnotify
%define version 0.3.3
%define release %mkrel 2

Summary: Libnotify bindings for Ruby
Name: %{name}
Version: %{version}
Release: %{release}
Group: Development/Ruby
License: BSD-like
URL: http://ruby-libnotify.rubyforge.org/
Source0: %{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-root
BuildRequires: ruby-devel 
BuildRequires: ruby-gnome2-devel 
BuildRequires: ruby-gtk2
BuildRequires: libnotify-devel

%description
Libnotify bindings for Ruby

%prep
%setup -q

%build
ruby extconf.rb --vendor
make

%install
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
%doc AUTHORS COPYING ChangeLog README doc examples
%{ruby_vendorarchdir}/*.so
%{ruby_vendorlibdir}/*.rb

