from parse import parse


lists = ['buildenv', 'options', 'installed']


def parse_buildinfo(source):
    lines = source.splitlines()

    errors = []
    buildinfo = {
        'options': [], 'buildenv': [], 'installed': [],
        'builddir': '', 'pkgbuild_sha256sum': '',
        'builddate': '', 'packager': '', 'pkgarch': '',
        'pkgver': '', 'pkgbase': '', 'pkgname': '', 'format': '',
    }

    for line in lines:
        parsed = parse('{} ={}', line)
        if not parsed:
            errors.append(f'failed to parse line "{line}"')
            continue

        key, value = parsed
        key = key.strip()
        value = value.strip()

        if key in lists:
            buildinfo[key].append(value)
        else:
            buildinfo[key] = value

    return (buildinfo, errors)
