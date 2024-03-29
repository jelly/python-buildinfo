from buildinfo.parse import parse_buildinfo


def test_invalid():
    buildinfo = '''barbar
'''

    data, errors = parse_buildinfo(buildinfo)
    assert data['pkgname'] == ''
    assert 'failed to parse line' in errors[0]


def test_format0():
    buildinfo = '''builddir = /build
pkgbuild_sha256sum = f5b30f7505199a8cb174275a4d4f211d3978c748a2fdfe564f0cf0b0a050f9b5
buildenv = !distcc
buildenv = color
buildenv = !ccache
buildenv = check
buildenv = !sign
options = strip
options = docs
options = !libtool
options = !staticlibs
options = emptydirs
options = zipman
options = purge
options = !optipng
options = !upx
options = !debug
installed = acl-2.2.52-4
installed = archlinux-keyring-20170823-1
installed = attr-2.4.47-3
installed = autoconf-2.69-4
installed = automake-1.15.1-1
installed = bash-4.4.012-2
installed = binutils-2.28.0-4
installed = bison-3.0.4-3
installed = bzip2-1.0.6-6
installed = ca-certificates-20170307-1
installed = ca-certificates-cacert-20140824-4
installed = ca-certificates-mozilla-3.32-1
installed = ca-certificates-utils-20170307-1
installed = coreutils-8.27-1
installed = cracklib-2.9.6-1
installed = curl-7.55.1-2
installed = db-5.3.28-3
installed = diffutils-3.6-1
installed = e2fsprogs-1.43.5-1
installed = expat-2.2.3-1
installed = fakeroot-1.21-2
installed = file-5.31-1
installed = filesystem-2017.03-2
installed = findutils-4.6.0-2
installed = flex-2.6.4-1
installed = gawk-4.1.4-2
installed = gc-7.6.0-1
installed = gcc-7.1.1-4
installed = gcc-libs-7.1.1-4
installed = gdbm-1.13-1
installed = gettext-0.19.8.1-2
installed = glib2-2.52.3-1
installed = glibc-2.25-7
installed = gmp-6.1.2-1
installed = gnupg-2.1.23-1
installed = gnutls-3.5.15-1
installed = gpgme-1.9.0-3
installed = grep-3.1-1
installed = groff-1.22.3-7
installed = guile-2.2.2-1
installed = gzip-1.8-2
installed = iana-etc-20170512-1
installed = icu-59.1-2
installed = keyutils-1.5.10-1
installed = krb5-1.15.1-1
installed = less-487-1
installed = libarchive-3.3.2-1
installed = libassuan-2.4.3-1
installed = libatomic_ops-7.4.6-1
installed = libcap-2.25-1
installed = libcap-ng-0.7.8-1
installed = libffi-3.2.1-2
installed = libgcrypt-1.8.0-1
installed = libgpg-error-1.27-1
installed = libidn-1.33-2
installed = libksba-1.3.4-2
installed = libldap-2.4.44-5
installed = libmpc-1.0.3-2
installed = libnghttp2-1.23.1-1
installed = libpsl-0.18.0-1
installed = libsasl-2.1.26-11
installed = libsecret-0.18.5+14+g9980655-1
installed = libssh2-1.8.0-2
installed = libsystemd-234.11-8
installed = libtasn1-4.12-2
installed = libtirpc-1.0.2-1
installed = libtool-2.4.6-8
installed = libunistring-0.9.7-1
installed = libutil-linux-2.30.1-2
installed = linux-api-headers-4.10.1-1
installed = lz4-1:1.8.0-1
installed = m4-1.4.18-1
installed = make-4.2.1-2
installed = mpfr-3.1.5.p2-1
installed = ncurses-6.0+20170527-1
installed = nettle-3.3-1
installed = npth-1.5-1
installed = openssl-1.1.0.f-2
installed = p11-kit-0.23.7-1
installed = pacman-5.0.2-2
installed = pacman-mirrorlist-20170729-1
installed = pam-1.3.0-1
installed = pambase-20130928-1
installed = patch-2.7.5-1
installed = pcre-8.41-1
installed = perl-5.26.0-3
installed = pinentry-1.0.0-1
installed = pkg-config-0.29.2-1
installed = readline-7.0.003-1
installed = sed-4.4-1
installed = shadow-4.5-2
installed = sqlite-3.20.1-1
installed = sudo-1.8.20.p2-1
installed = tar-1.29-2
installed = texinfo-6.4-1
installed = tzdata-2017b-1
installed = util-linux-2.30.1-2
installed = which-2.21-2
installed = xz-5.2.3-1
installed = zlib-1:1.2.11-2
'''

    data, _ = parse_buildinfo(buildinfo)
    assert data['format'] == ''
    assert data['builddir'] == '/build'


def test_format1():
    buildinfo = """format = 1
pkgname = gap-doc
pkgbase = gap
pkgver = 4.10.2-1
pkgarch = x86_64
pkgbuild_sha256sum = a8c9c1a2c0434cded3904b0de19d512fdd8888172d312f9700481ad892b54c6e
packager = Antonio Rojas <arojas@archlinux.org>
builddate = 1561209733
builddir = /build
buildenv = !distcc
buildenv = color
buildenv = !ccache
buildenv = check
buildenv = !sign
options = strip
options = docs
options = !libtool
options = !staticlibs
options = emptydirs
options = zipman
options = purge
options = !debug
installed = acl-2.2.53-1-x86_64
installed = arb-2.16.0-1-x86_64
installed = archlinux-keyring-20190123-2-any
installed = argon2-20171227-3-x86_64
installed = attr-2.4.48-1-x86_64
installed = audit-2.8.5-2-x86_64
installed = autoconf-2.69-5-any
installed = automake-1.16.1-1-any
installed = bash-5.0.007-1-x86_64
installed = binutils-2.32-2-x86_64
installed = bison-3.3.2-1-x86_64
installed = boost-1.69.0-2-x86_64
installed = boost-libs-1.69.0-2-x86_64
installed = bzip2-1.0.6-8-x86_64
installed = c-xsc-2.5.4-1-x86_64
installed = ca-certificates-20181109-1-any
installed = ca-certificates-mozilla-3.44-1-x86_64
installed = ca-certificates-utils-20181109-1-any
installed = cddlib-1:0.94j-1-x86_64
installed = chrpath-0.16-2-x86_64
installed = coreutils-8.31-1-x86_64
"""

    data, _ = parse_buildinfo(buildinfo)
    assert data['format'] == '1'
    assert data['builddir'] == '/build'
