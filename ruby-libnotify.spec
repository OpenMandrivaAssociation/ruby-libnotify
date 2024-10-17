%define name ruby-libnotify
%define version 0.5.0
%define release %mkrel 1

Summary: Libnotify bindings for Ruby
Name: %{name}
Version: %{version}
Release: %{release}
Group: Development/Ruby
License: BSD-like
URL: https://ruby-libnotify.rubyforge.org/
Source0: vargolo-ruby-libnotify-v%{version}-0-g95340d9.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-root
BuildRequires: ruby-devel
BuildRequires: ruby-RubyGems
BuildRequires: ruby-gnome2-devel 
BuildRequires: ruby-gtk2
BuildRequires: libnotify-devel

%description
Libnotify bindings for Ruby

%prep
%setup -qn vargolo-ruby-libnotify-3fc8bb8

%build
ruby setup.rb config --site-ruby=%ruby_vendorlibdir --so-dir=%ruby_vendorarchdir
ruby setup.rb setup

%install
rm -fr %buildroot
ruby setup.rb install --prefix=%buildroot

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
%doc AUTHORS.rdoc CHANGELOG.rdoc COPYING README.rdoc examples
%{ruby_vendorarchdir}/*.so
%{ruby_vendorlibdir}/*.rb

