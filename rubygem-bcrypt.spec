#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-bcrypt
Version  : 3.1.10
Release  : 8
URL      : https://rubygems.org/downloads/bcrypt-3.1.10.gem
Source0  : https://rubygems.org/downloads/bcrypt-3.1.10.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: rubygem-bcrypt-lib
BuildRequires : ruby
BuildRequires : rubygem-devise
BuildRequires : rubygem-diff-lcs
BuildRequires : rubygem-rake-compiler
BuildRequires : rubygem-rdoc
BuildRequires : rubygem-rspec
BuildRequires : rubygem-rspec-core
BuildRequires : rubygem-rspec-expectations
BuildRequires : rubygem-rspec-mocks
BuildRequires : rubygem-rspec-support

%description
# bcrypt-ruby
An easy way to keep your users' passwords secure.
* http://github.com/codahale/bcrypt-ruby/tree/master

%package lib
Summary: lib components for the rubygem-bcrypt package.
Group: Libraries

%description lib
lib components for the rubygem-bcrypt package.


%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n bcrypt-3.1.10
gem spec %{SOURCE0} -l --ruby > rubygem-bcrypt.gemspec

%build
gem build rubygem-bcrypt.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
bcrypt-3.1.10.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
pushd %{buildroot}%{gem_dir}/gems/bcrypt-3.1.10
rspec -I.:lib spec/
popd


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.3.0/cache/bcrypt-3.1.10.gem
/usr/lib64/ruby/gems/2.3.0/extensions/x86_64-linux/2.3.0/bcrypt-3.1.10/gem.build_complete
/usr/lib64/ruby/gems/2.3.0/extensions/x86_64-linux/2.3.0/bcrypt-3.1.10/gem_make.out
/usr/lib64/ruby/gems/2.3.0/gems/bcrypt-3.1.10/.gitignore
/usr/lib64/ruby/gems/2.3.0/gems/bcrypt-3.1.10/.rspec
/usr/lib64/ruby/gems/2.3.0/gems/bcrypt-3.1.10/.travis.yml
/usr/lib64/ruby/gems/2.3.0/gems/bcrypt-3.1.10/CHANGELOG
/usr/lib64/ruby/gems/2.3.0/gems/bcrypt-3.1.10/COPYING
/usr/lib64/ruby/gems/2.3.0/gems/bcrypt-3.1.10/Gemfile
/usr/lib64/ruby/gems/2.3.0/gems/bcrypt-3.1.10/Gemfile.lock
/usr/lib64/ruby/gems/2.3.0/gems/bcrypt-3.1.10/README.md
/usr/lib64/ruby/gems/2.3.0/gems/bcrypt-3.1.10/Rakefile
/usr/lib64/ruby/gems/2.3.0/gems/bcrypt-3.1.10/bcrypt.gemspec
/usr/lib64/ruby/gems/2.3.0/gems/bcrypt-3.1.10/ext/jruby/bcrypt_jruby/BCrypt.java
/usr/lib64/ruby/gems/2.3.0/gems/bcrypt-3.1.10/ext/mri/.RUBYARCHDIR.time
/usr/lib64/ruby/gems/2.3.0/gems/bcrypt-3.1.10/ext/mri/Makefile
/usr/lib64/ruby/gems/2.3.0/gems/bcrypt-3.1.10/ext/mri/bcrypt_ext.c
/usr/lib64/ruby/gems/2.3.0/gems/bcrypt-3.1.10/ext/mri/bcrypt_ext.o
/usr/lib64/ruby/gems/2.3.0/gems/bcrypt-3.1.10/ext/mri/crypt.c
/usr/lib64/ruby/gems/2.3.0/gems/bcrypt-3.1.10/ext/mri/crypt.h
/usr/lib64/ruby/gems/2.3.0/gems/bcrypt-3.1.10/ext/mri/crypt.o
/usr/lib64/ruby/gems/2.3.0/gems/bcrypt-3.1.10/ext/mri/crypt_blowfish.c
/usr/lib64/ruby/gems/2.3.0/gems/bcrypt-3.1.10/ext/mri/crypt_blowfish.o
/usr/lib64/ruby/gems/2.3.0/gems/bcrypt-3.1.10/ext/mri/crypt_gensalt.c
/usr/lib64/ruby/gems/2.3.0/gems/bcrypt-3.1.10/ext/mri/crypt_gensalt.o
/usr/lib64/ruby/gems/2.3.0/gems/bcrypt-3.1.10/ext/mri/extconf.rb
/usr/lib64/ruby/gems/2.3.0/gems/bcrypt-3.1.10/ext/mri/ow-crypt.h
/usr/lib64/ruby/gems/2.3.0/gems/bcrypt-3.1.10/ext/mri/wrapper.c
/usr/lib64/ruby/gems/2.3.0/gems/bcrypt-3.1.10/ext/mri/wrapper.o
/usr/lib64/ruby/gems/2.3.0/gems/bcrypt-3.1.10/lib/bcrypt.rb
/usr/lib64/ruby/gems/2.3.0/gems/bcrypt-3.1.10/lib/bcrypt/engine.rb
/usr/lib64/ruby/gems/2.3.0/gems/bcrypt-3.1.10/lib/bcrypt/error.rb
/usr/lib64/ruby/gems/2.3.0/gems/bcrypt-3.1.10/lib/bcrypt/password.rb
/usr/lib64/ruby/gems/2.3.0/gems/bcrypt-3.1.10/spec/TestBCrypt.java
/usr/lib64/ruby/gems/2.3.0/gems/bcrypt-3.1.10/spec/bcrypt/engine_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/bcrypt-3.1.10/spec/bcrypt/error_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/bcrypt-3.1.10/spec/bcrypt/password_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/bcrypt-3.1.10/spec/spec_helper.rb
/usr/lib64/ruby/gems/2.3.0/specifications/bcrypt-3.1.10.gemspec

%files lib
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.3.0/extensions/x86_64-linux/2.3.0/bcrypt-3.1.10/bcrypt_ext.so
/usr/lib64/ruby/gems/2.3.0/gems/bcrypt-3.1.10/ext/mri/bcrypt_ext.so
/usr/lib64/ruby/gems/2.3.0/gems/bcrypt-3.1.10/lib/bcrypt_ext.so
