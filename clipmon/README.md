# fedora-spec

Spec file for clipmon  

## Source

<https://git.sr.ht/~whynothugo/clipmon>  

Thanks whynothugo!  

## SourceHut to Fedora Spec File Issue

I had to create a git submodule because SourceHut's archive link (<https://git.sr.ht/~whynothugo/clipmon/archive/main.tar.gz>) downloads as `clipmon-main.tar.gz`, not `main.tar.gz`.  

Sourcehut creates the filename by prepending the `name` of the repo to the `branch/commit`: `clipmon`-`main`.tar.gz.  

The downloaded tarball's name `clipmon-main.tar.gz` doesn't match the last section of the Source URL's path (.../archive/`main.tar.gz`), causing the Fedora Spec File `%setup` macro to break. Manual setup instead of using `%setup` seems to work innitially, but then breaks later in the build process. Lame on both fronts, sadface (unless I'm missing anything -- please let me know!).

See here for more info:  
<https://docs.fedoraproject.org/en-US/packaging-guidelines/SourceURL/#_troublesome_urls>

## Patches

`remove-superfluous-logging.patch`  

- Removes superfluous logging in journal.  
