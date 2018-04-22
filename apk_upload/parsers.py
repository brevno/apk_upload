import apkutils
from rest_framework.exceptions import ParseError
from rest_framework.parsers import MultiPartParser


class APKParser(MultiPartParser):
    """ Upload parser with APK-parsing feature provided. """

    def parse(self, stream, media_type=None, parser_context=None):
        """ Parse uploaded APK files. """

        data_and_files = super().parse(stream, media_type, parser_context)

        files = data_and_files.files
        if len(files) > 1:
            raise ParseError('More then one file received.')
        file_desc = next(files.values())

        # read and parse app parameters from APK manifest
        try:
            apk = apkutils.APK(file_desc.file)
            manifest = apk.get_manifest()
            package_name = manifest.get('@package')
            package_version_code = manifest.get('@android:versionCode')
        except apkutils.apkfile.BadZipFile:
            raise ParseError('Failed to parse APK file: unknown file format.')

        # update the 'data' dict with new values from manifest
        data_and_files.data._mutable = True
        data_and_files.data['package_name'] = package_name
        data_and_files.data['package_version_code'] = package_version_code

        return data_and_files
