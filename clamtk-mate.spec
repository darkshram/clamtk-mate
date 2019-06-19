Name:              clamtk-mate
Version:           0.02.01
Release:           2%{?dist}
URL:               https://github.com/darkshram/clamtk-mate/
License:           GPLv2+/Artistic license
Summary:           ClamTk plugin for MATE Desktop.
Source0:           https://github.com/darkshram/clamtk-mate/releases/download/%{version}/%{name}-%{version}.tar.xz
BuildArch:         noarch

Requires:          python-caja
Requires:          clamtk
Requires:          clamav-update

%description
Clamtk-mate is a simple plugin to allow a right-click, context menu scan of
files or folders in MATE Desktop.

Clamtk-mate is based on clamtk-gnome.

%prep
%autosetup -p1

%build
# nothing to do

%install
%{__mkdir_p} %{buildroot}%{_datadir}/caja-python/extensions/
install -m 755 %{name}.py %{buildroot}%{_datadir}/caja-python/extensions/

for n in po/*.mo ; do
        install -p -D -m0644 $n %{buildroot}/%{_datadir}/locale/`basename $n .mo`/LC_MESSAGES/%{name}.mo
done

%find_lang %{name}

%files -f %{name}.lang
%doc NEWS.md README.md docs _img
%license LICENSE DISCLAIMER
%{_datadir}/caja-python/extensions/clamtk-mate.py*

%changelog
* Wed Jun 19 2019 Joel Barrios <http://www.alcancelibre.org/> - 0.02.01-2
- Rebuild for python-caja 1.22.0.

* Mon Dec 11 2017 Joel Barrios <http://www.alcancelibre.org/> - 0.02.01-1
- Update to 0.02.01

* Sun Sep 24 2017 Joel Barrios <http://www.alcancelibre.org/> - 0.02-1
- Initial build.
