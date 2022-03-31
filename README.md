# fedora-spec

Spec files for Fedora packages  
<https://copr.fedorainfracloud.org/coprs/mixwui/>

## Information on Spec Files and Building RPMs

Download source(s) (<https://stackoverflow.com/a/33177482>):

```shell
spectool -g -R --dryrun somename.spec
```

Source files can be manually placed as well.

Build with:

```shell
rpmbuild -ba somename.spec
```

Location of rpmbuild:  
`~/rpmbuild/*`  

Spec, source/tarball/archives, patch files, etc. go here:  
`~/rpmbuild/SOURCES/`  

Build directory:  
`~/rpmbuild/BUILD`  

RPMs directory:  
`~/rpmbuild/RPMS`  

### Useful References

🚚 Just dumping an F-ton of links here 🚚

Nice, brief overall explanation for COPR:  
<https://www.reddit.com/r/Fedora/comments/l5bzy0/need_help_creating_a_package_in_copr/gktslik/?utm_source=reddit&utm_medium=web2x&context=3>  

Fedora magazine article on creating RPM packages via spec files:  
<https://fedoramagazine.org/how-rpm-packages-are-made-the-spec-file/>  

Repos of a bunch of spec files, good examples:  
<https://github.com/audinux/fedora-spec>  
<https://github.com/ycollet/fedora-spec>  

<https://rpm-packaging-guide.github.io/>  

RPM spec wizard:
<http://frostyx.cz/posts/introducing-rpm-spec-wizard>  
<https://xsuchy.github.io/rpm-spec-wizard/>  

RPM/spec macros:  
<http://ftp.rpm.org/max-rpm/s1-rpm-inside-macros.html>  
<https://docs.fedoraproject.org/en-US/packaging-guidelines/RPMMacros/>  

RPM/spec with Rust:  
<https://msehnout.fedorapeople.org/rust-fedora.pdf>

## Creating Patch Files

Create patch file with:  

```shell
git diff some-file > patch-name.patch
```

Test with:  

```shell
git apply patch-name.patch
```

Multiple diffs/patches can be in the same patch file.

Be sure to use `-p1` flag e.g. `%patch0 -p1` if generating patch with `git diff`. Explained in the references below.  

### Useful References

<https://cromwell-intl.com/open-source/rpm-patch.html>  
<http://bradthemad.org/tech/notes/patching_rpms.php>  
